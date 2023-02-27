from django.forms import ModelForm, DateInput, NumberInput
from django import forms
from jsignature.widgets import JSignatureWidget

from ManageTool.models import ContractEmployment


#


class ContractEmploymentForm(ModelForm):
    class Meta:
        model = ContractEmployment
        fields = '__all__'
        exclude = ['created']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'signature': JSignatureWidget(attrs={'width': '100%', 'height': '200px', 'style': 'border: 1px solid black;'}),
            'fuel_refund': forms.NumberInput(attrs={'step': '0.01', 'min': '0.00', 'value': '0.75'})
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
            'start_date': forms.DateInput(attrs={'type': 'date', 'required': 'required'}),
            'concluded_date': forms.DateInput(attrs={'type': 'date', 'required': 'required'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'required': 'required'}),
            'signature': JSignatureWidget(attrs={'width': '100%', 'height': '200px', 'style': 'border: 1px solid black;', 'required': 'required'}),
            'name_surname': forms.TextInput(attrs={'placeholder': 'Imię i nazwisko*', 'required': 'required'}),
            'street': forms.TextInput(attrs={'placeholder': 'Ulica*', 'required': 'required'}),
            'street_number': forms.TextInput(attrs={'placeholder': 'Numer domu*', 'required': 'required'}),
            'house_number': forms.TextInput(attrs={'placeholder': 'Numer lokalu'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Kod pocztowy*', 'required': 'required'}),
            'town': forms.TextInput(attrs={'placeholder': 'Miejscowość*', 'required': 'required'}),
            'id_number': forms.TextInput(attrs={'placeholder': 'Nr dowodu/paszportu*', 'required': 'required'}),
            'pesel': forms.TextInput(attrs={'placeholder': 'nr PESEL*', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Numer telefonu*', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adres e-mail*', 'required': 'required'}),
            'account_number': forms.TextInput(attrs={'placeholder': 'Numer konta bankowego*', 'required': 'required', 'pattern': '([0-9]{26})(-[0-9]{2})?'}),
            'transport_form': forms.Select(attrs={'required': 'required'}),
        }
