from django import forms
from .models import SignatureComparison

class SignatureComparisonForm(forms.ModelForm):
    class Meta:
        model = SignatureComparison
        fields = ['original_image', 'signature_image']
