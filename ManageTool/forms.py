from django.forms import ModelForm, DateInput
from jsignature.forms import JSignatureField

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
        }
