import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from ManageTool.models import Vs1YkBaformsSubmissions, Order


# Create your views here.
@method_decorator(login_required(login_url='/login'), name='dispatch')
class IndexView(View):
    def get(self, request):
        items = Vs1YkBaformsSubmissions.objects.all()
        for item in items:
            new_order, created = Order.objects.get_or_create(bounded_to=item.id)
            if created:
                new_order.type = item.title
                if item.message.__contains__('"field_id":"35"' or '"field_id":"226"' or '"field_id":"164"'):
                    new_order.marketing_approval = True
                if item.message.__contains__('"field_id":"36"' or '"field_id":"227"' or '"field_id":"165"'):
                    new_order.reminder_approval = True
                data = json.loads(item.message)
                for mess in data:
                    titles = []
                    values = []
                    titles.append(mess['title'])
                    values.append(mess['message'])
                    result = dict(zip(titles, values))
                    for key, value in result.items():
                        if key == 'Województwo':
                            new_order.province = value
                        elif 'Miasto' in key:
                            new_order.city = value
                        elif 'Dzielnica' in key:
                            new_order.district = value
                        elif key == 'Nazwa placówki':
                            new_order.facility_name = value
                        elif key == 'Ulica':
                            new_order.street = value
                        elif key == 'Nr domu':
                            new_order.street_number = value
                        elif key == 'Nr mieszkania':
                            new_order.house_number = value
                        elif key == 'Kod pocztowy':
                            new_order.zip_code = value
                        elif key == 'Miejscowość':
                            new_order.town = value
                        elif 'Opłata dojazdowa' in key:
                            new_order.arrival_fee = value
                        elif key == 'Nazwa firmy':
                            new_order.company_name = value
                        elif key == 'Imię i nazwisko zamawiającego':
                            new_order.name_surname = value
                        elif key == 'NIP':
                            new_order.nip = value
                        elif key == 'Adres siedziby':
                            new_order.facility_address = value
                        elif key == 'Telefon kontaktowy':
                            new_order.phone = value
                        elif key == 'Adres e-mail':
                            new_order.email = value
                        elif key == 'Długość wizyty Mikołaja':
                            new_order.visit_length = value
                        elif key == 'Data wizyty':
                            new_order.visit_date = value
                        elif key == 'Przedział godzinowy wizyty':
                            new_order.visit_time = value
                        elif key == 'Preferowana godzina wizyty':
                            new_order.pref_visit_time = value
                        elif key == 'Informacje dodatkowe':
                            new_order.additional_info = value
                        elif key == 'Szczegóły zamówienia':
                            new_order.order_details = value
                            true = True
                            false = False
                            res = list(eval(value)['products'].keys())[0]
                            print(res)
                        elif key == '':
                            break
                        else:
                            print('NIE PYKŁO:', key, value)
                new_order.save()
            else:
                pass
        orders = Order.objects.all()
        return render(request, 'index.html', {'orders': orders})


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('register')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2 and first_name and last_name and email and password:
            User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name,
                                     password=password)
            return redirect('login')
        else:
            msg = 'Niepoprawne dane'
            return render(request, 'register.html', {'msg': msg})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Test(View):
    def get(self, request):
        items = Vs1YkBaformsSubmissions.objects.all()
        for item in items:
            new_order, created = Order.objects.get_or_create(bounded_to=item.id)
            if created:
                new_order.type = item.title
                if item.message.__contains__('"field_id":"35"' or '"field_id":"226"' or '"field_id":"164"'):
                    new_order.marketing_approval = True
                if item.message.__contains__('"field_id":"36"' or '"field_id":"227"' or '"field_id":"165"'):
                    new_order.reminder_approval = True
                data = json.loads(item.message)
                for mess in data:
                    titles = []
                    values = []
                    titles.append(mess['title'])
                    values.append(mess['message'])
                    result = dict(zip(titles, values))
                    for key, value in result.items():
                        if key == 'Województwo':
                            new_order.province = value
                        elif 'Miasto' in key:
                            new_order.city = value
                        elif 'Dzielnica' in key:
                            new_order.district = value
                        elif key == 'Nazwa placówki':
                            new_order.facility_name = value
                        elif key == 'Ulica':
                            new_order.street = value
                        elif key == 'Nr domu':
                            new_order.street_number = value
                        elif key == 'Nr mieszkania':
                            new_order.house_number = value
                        elif key == 'Kod pocztowy':
                            new_order.zip_code = value
                        elif key == 'Miejscowość':
                            new_order.town = value
                        elif 'Opłata dojazdowa' in key:
                            new_order.arrival_fee = value
                        elif key == 'Nazwa firmy':
                            new_order.company_name = value
                        elif key == 'Imię i nazwisko zamawiającego':
                            new_order.name_surname = value
                        elif key == 'NIP':
                            new_order.nip = value
                        elif key == 'Adres siedziby':
                            new_order.facility_address = value
                        elif key == 'Telefon kontaktowy':
                            new_order.phone = value
                        elif key == 'Adres e-mail':
                            new_order.email = value
                        elif key == 'Długość wizyty Mikołaja':
                            new_order.visit_length = value
                        elif key == 'Data wizyty':
                            new_order.visit_date = value
                        elif key == 'Przedział godzinowy wizyty':
                            new_order.visit_time = value
                        elif key == 'Preferowana godzina wizyty':
                            new_order.pref_visit_time = value
                        elif key == 'Informacje dodatkowe':
                            new_order.additional_info = value
                        elif key == 'Szczegóły zamówienia':
                            new_order.order_details = value
                            true = True
                            false = False
                            res = list(eval(value)['products'].keys())[0]
                            print(res)
                        elif key == '':
                            break
                        else:
                            print('NIE PYKŁO:', key, value)
                new_order.save()
            else:
                pass
        orders = Order.objects.all()
        return render(request, 'test.html', {'orders': orders})