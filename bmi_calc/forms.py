from django import forms


class IMBForm(forms.Form):
	name = forms.CharField(max_length=50, label='name :')
	height = forms.FloatField(label='height :')
	weight = forms.FloatField(label='weight :')