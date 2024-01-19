"""Form for software details."""
from django import forms
from .models import SoftwareDetails

class SoftwareDetailsForm(forms.ModelForm):
    """Software detail form."""

    class Meta:
        model = SoftwareDetails
        fields = '__all__'
        widgets = {
            'descriptions': forms.TextInput(attrs={'class': 'form-control'}),
            'yearly_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}),
            'support_end': forms.DateInput(attrs={'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'data-date-format': 'yyyy-mm-dd'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set 'remark' field as not required
        self.fields['remark'].required = False
