from django import forms

class CaesarCipherForm(forms.Form):
    MODE_CHOICES = [
        ('encrypt', 'Encrypt'),
        ('decrypt', 'Decrypt'),
    ]
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Message'
    )
    key = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 25}),
        label='Key (0-25)',
        min_value=0,
        max_value=25
    )
    mode = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        choices=MODE_CHOICES,
        label='Mode',
        initial='encrypt'
    )