from django.shortcuts import render
from .forms import IMBForm


form_imb = {
	(0, 16): "Severe underweight",
	(16, 18.5): "Underweight",
	(18.5, 25): "Normal",
	(25, 30): "Overweight",
	(30, 35): "Obesity",
	(35, 40): "Obesity is sharp",
	(40, 99): "Very severe obesity",
}


def bmi_calc(request):
	context = {}
	if request.method == 'POST':
		form = IMBForm(request.POST)
		if form.is_valid():
			height = float(form.data.get('height')) / 100
			weight = float(form.data.get('weight'))
			imb_result = weight / height ** 2

			if imb_result < 18.5:
				kg = (18.5 - imb_result) * height ** 2
				context['imb_advise'] = f'It is better to get {kg:.2f} kg, to get normal IMB'

			elif imb_result > 25:
				kg = (imb_result - 25) * height ** 2
				context['imb_advise'] = f'It is better to reduce {kg:.2f} kg, to get normal IMB'

			else:
				context['imb_advise'] = f'Good job!!'

			for k, v in form_imb.items():
				if k[0] <= imb_result <= k[1]:
					context['imb_text'] = v
					break

			context['imb'] = imb_result
		context['form'] = form
		return render(request, 'bmi_calc/main.html', context)
	else:
		form = IMBForm()
		context['form'] = form
	return render(request, 'bmi_calc/main.html', context)
