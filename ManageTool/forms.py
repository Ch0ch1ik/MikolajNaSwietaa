from django.forms import ModelForm, DateInput, NumberInput

from jsignature.widgets import JSignatureWidget

from ManageTool.models import ContractEmployment


#


class ContractEmploymentForm(ModelForm):
    class Meta:
        model = ContractEmployment
        fields = '__all__'
        exclude = ['created']

        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
            'signature': JSignatureWidget(attrs={'width': '100%', 'height': '200px', 'style': 'border: 1px solid black;'}),
            'fuel_refund': NumberInput(attrs={'step': '0.01', 'min': '0.00', 'value': '0.75'})
        }


class ContractSignForm(ModelForm):
    class Meta:
        model = ContractEmployment
        fields = '__all__'
        exclude = ['bounded_user', 'created', 'fuel_refund',
                   'hourly_rate_own_car',
                   'hourly_rate_company_car',
                   'visit_rate_own_car_firm',
                   'visit_rate_own_car_private_10min',
                   'visit_rate_own_car_private_20min',
                   'visit_rate_own_car_private_30min',
                   'visit_rate_own_car_private_60min',
                   'visit_rate_company_car_firm',
                   'visit_rate_company_car_private_10min',
                   'visit_rate_company_car_private_20min',
                   'visit_rate_company_car_private_30min',
                   'visit_rate_company_car_private_60min',
                   'employer',
                   'last_edit',
                   'signed_by_employer'
                   ]

        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
            'signature': JSignatureWidget(attrs={'width': '100%', 'height': '200px', 'style': 'border: 1px solid black;'}),
        }
