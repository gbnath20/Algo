from django import forms

class StockDetailsForm(forms.Form):
    symbol = forms.CharField(label='Symbol', max_length=100)
    time_from = forms.DateField(label='Time From')
    time_to = forms.DateField(label='Time To')
