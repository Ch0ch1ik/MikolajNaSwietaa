from django.forms import ModelForm, DateInput, NumberInput

from jsignature.widgets import JSignatureWidget

from ManageTool.models import ContractEmployment


#


class ContractEmploymentForm(ModelForm):
    class Meta:
        model = ContractEmployment
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
            'signature': JSignatureWidget(attrs={'width': '100%', 'height': '200px'}),
            'fuel_refund': NumberInput(attrs={'step': '0.01', 'min': '0.00', 'value': '0.75'})
        }
