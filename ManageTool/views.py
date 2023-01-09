import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView

from ManageTool.extract import json_extract
from ManageTool.models import Vs1YkBaformsSubmissions, Order


# Create your views here.
@method_decorator(login_required(login_url='/login'), name='dispatch')
class IndexView(View):

    def get(self, request):
        items = Vs1YkBaformsSubmissions.objects.all()
        user = request.user
        if user.is_superuser:
            # products = Vs1YkBaformsItems.objects.all()
            # for product in products:
            #     # new_product, created = Product.objects.get_or_create(bounded_id=product.id)
            #     # x = eval(product.options)
            #     if product.options.__contains__('product'):
            #         data = json.loads(product.options)['items']
            #         # print(data)
            #         # print(json_extract(data, 'title'))
            #         arr = []
            #         x = json_extract(data, 'title')
            #         for item in x:
            #             try:
            #                 for _ in eval(item):
            #                     arr.append(_)
            #                     # arr.append(item.split(','))
            #                     # # print(type(eval(item)))
            #                     # # splitted_item = item.split(',')
            #                     # # arr.append(splitted_item)
            #                     # arr.append(item)
            #             except SyntaxError:
            #                 arr.append(item)
            # print(arr)
            # print(arr)
            # print(type(x))
            # data = json.loads(product.options)['title']
            # print(data)
            # data = json.loads(product.options)['title']
            # print(data)
            # for item in json_extract(data, 'product'):
            #     print(item)
            # for k, v in item:
            #     print(k+'TO'+v)
            # print(json_extract(data, 'title'))
            for item in items:
                new_order, created = Order.objects.get_or_create(bounded_to=item.id)
                if created:
                    new_order.type = item.title
                    new_order.created = item.date_time
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
                                fee = 0
                                if value.__contains__('"84":{}'):
                                    fee = 0
                                elif value.__contains__('84":{"3"'):
                                    fee = 120
                                elif value.__contains__('84":{"2"'):
                                    fee = 80
                                elif value.__contains__('84":{"1"'):
                                    fee = 40
                                elif value.__contains__('"196":{}'):
                                    fee = 0
                                elif value.__contains__('196":{"3"'):
                                    fee = 120
                                elif value.__contains__('196":{"2"'):
                                    fee = 80
                                elif value.__contains__('196":{"1"'):
                                    fee = 40
                                elif value.__contains__('"257":{}'):
                                    fee = 0
                                elif value.__contains__('257":{"3"'):
                                    fee = 120
                                elif value.__contains__('257":{"2"'):
                                    fee = 80
                                elif value.__contains__('257":{"1"'):
                                    fee = 40
                                new_order.arrival_fee = fee
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
                                # if value.__contains__('"205":{"2":'):
                                #     price = 290
                                #     product = 'Przedszkole WizytaStandard (do 60 min.)'
                                # else:
                                #     price = 0

                                new_order.order_details = value

                                # products = (eval(value)['products'])
                                # cos = json_extract(products, 'title')
                                # for _ in cos:
                                #     new_order.products += _+','
                            elif key == '':
                                break
                            else:
                                print('NIE PYKŁO:', key, value)
                    new_order.save()
                else:
                    pass
                    # data = json.loads(item.message)
                    # for mess in data:
                    #     titles = []
                    #     values = []
                    #     titles.append(mess['title'])
                    #     values.append(mess['message'])
                    #     result = dict(zip(titles, values))
                    #     for key, value in result.items():
                    #         if key == 'Szczegóły zamówienia':
                    #             true = True
                    #             false = False
                    #             # print(eval(value))
                    #             products = (eval(value)['products'])
                    #             # print(products)
                    #             cos = json_extract(products, 'title')
                    #             print(cos)

                    # for i in data:
                    #     print(i['message'])
                    # print(data['products'])
                    # info = json_extract(data, 'products')
                    # print(info)
                    # for mess in data:
                    #     titles = []
                    #     values = []
                    #     titles.append(mess['title'])
                    #     values.append(mess['message'])
                    #     result = dict(zip(titles, values))
                    #     for key, value in result.items():
                    #         if key == 'Szczegóły zamówienia':
                    #             true = True
                    #             false = False
                    #             for i in list(eval(value)):
                    #                 if i == 'products':
                    #                     x = eval(value)[i]
                    #                     z = []
                    #                     for y in x:
                    #                         z.append(y)
                    #                         print(z)

            # products = Order.objects.all()
            # print(orders.first().products)
            orders = Order.objects.all()
            for order in orders:
                if type(order.order_details) == str:
                    true = True
                    false = False
                    data = [json.loads(order.order_details)]
                    # print(json_extract(data, 'price'))
                    # print(json_extract(data, 'quantity'))
                    quantities = [int(item) for item in json_extract(data, 'quantity')]
                    prices = [int(item) for item in json_extract(data, 'price')]
                    # print(type(dict(zip(prices, quantities))))
                    prices_quantites = dict(zip(prices, quantities))
                    order.products = prices_quantites

                elif type(order.order_details) == dict:
                    true = True
                    false = False
                    data = order.order_details
                    quantities = [int(item) for item in json_extract(data, 'quantity')]
                    prices = [int(item) for item in json_extract(data, 'price')]
                    prices_quantites = dict(zip(prices, quantities))
                    order.products = prices_quantites
                order.save()
            orders = Order.objects.all().order_by('cancelled', 'accomplished')
            total = 0
            for order in orders:
                for k, v in order.products.items():
                    if order.type != 'Wizyta prywatna':
                        total += (int(k) * int(v)) * 1.23
                    else:
                        total += int(k) * int(v)
            provinces = Order.objects.values_list('province', flat=True).distinct()
            users = User.objects.all()

            # json_extract(test, "products")
            #     # test = json_extract(test, 'quantity')
            #     print(test)
            #     true = True
            #     false = False
            #     # test = json_extract(eval(test), '"84"')
            #     if test.__contains__('"84":{}'):
            #         print('Bez dowozu: '+test)
            #     elif test.__contains__('84":{"3"'):
            #         print('Dowóz - do 30 km - 120: '+test)
            #     elif test.__contains__('84":{"2"'):
            #         print('Dowóz - do 20 km - 80: '+test)
            #     elif test.__contains__('84":{"1"'):
            #         print('Dowóz - do 10 km - 40: '+test)
            return render(request, 'index.html',
                          {'orders': orders, 'total': total, 'provinces': provinces, "users": users})
        else:
            return redirect('testowy')

    def post(self, request):
        user = request.POST['assign']
        id = request.POST['order_id']
        order = Order.objects.get(id=id)
        order.assigned_to.set(user)
        order.save()
        return redirect('index')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('index')
            else:
                return redirect('testowy')
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


class Users(View):
    def get(self, request):
        users = User.objects.all()
        if request.user.is_superuser:
            return render(request, 'users.html', {'users': users})
        else:
            return redirect('testowy')


def confirm_payment(request, id):
    """Confirm payment for order with given id and redirect to index page"""
    order = Order.objects.get(id=id)
    order.paid_made = True
    order.save()
    return redirect('index')


def confirm_order(request, id):
    """Confirm order with given id and redirect to index page"""
    order = Order.objects.get(id=id)
    order.confirmed = True
    order.save()
    return redirect('index')


def cancel_order(request, id):
    """Cancel order with given id and redirect to index page"""
    order = Order.objects.get(id=id)
    order.cancelled = True
    order.save()
    return redirect('index')


def confirm_accomplished(request, id):
    """Confirm accomplished order with given id and redirect to testowy page"""
    order = Order.objects.get(id=id)
    order.accomplished = True
    order.save()
    return redirect('testowy')


class UpdateOrder(UpdateView):
    model = Order
    fields = ['type', 'province', 'city', 'district', 'facility_name', 'street', 'street_number', 'house_number',
              'zip_code', 'town', 'arrival_fee', 'company_name', 'name_surname', 'nip', 'facility_address', 'phone',
              'email', 'visit_length', 'visit_date', 'visit_time']
    template_name = 'order_update_form.html'
    success_url = "/"


class Test(View):
    def get(self, request):
        user = request.user
        orders = Order.objects.all().filter(assigned_to=user)

        messages = Vs1YkBaformsSubmissions.objects.first()
        message = messages.message

        print(json_extract(message, 'products'))

        return render(request, 'testowy.html', {'orders': orders})
