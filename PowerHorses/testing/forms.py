from django import forms

class paramForm(forms.form):
    temperature = forms.Int(label = 'temperature')
    humidity = forms.Int(label = 'humidity')
    light_intensity = forms.Int(label = 'light_intensity')
