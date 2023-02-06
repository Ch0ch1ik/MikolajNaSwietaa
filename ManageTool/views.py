import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView

from ManageTool.extract import json_extract
from ManageTool.items_funcs import update_items
from ManageTool.models import Vs1YkBaformsSubmissions, Order, Applications


# Create your views here.
@method_decorator(login_required(login_url='/login'), name='dispatch')
class IndexView(View):
    """Class based view for index page. It shows all orders and allows to assign them to users. """

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
            update_items(items)

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
    """Confirm accomplished order with given id and redirect to index page"""
    order = Order.objects.get(id=id)
    order.accomplished = True
    order.save()
    return redirect('index')


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
        orders = Vs1YkBaformsSubmissions.objects.all().first()

        message = eval(orders.message)
        for mess in message:
            for k, v in mess.items():

                if k == 'message' and len(v) > 300:
                    # print(v)
                    true = True
                    false = False

                    for kk, vv in eval(v).items():
                        # print(type(vv))
                        if isinstance(vv, dict):
                            for key, value in vv.items():
                                print(key, value)

        orders = Order.objects.all().order_by('cancelled', 'accomplished')

        return render(request, 'testowy.html', {'orders': orders})


# write a test function to test IndexView
# def test_index_view(self):
#     # create a request
#     request = self.factory.get(reverse('index'))
#     # get the response
#     response = IndexView.as_view()(request)
#     # test the response
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'index.html')
#     self.assertContains(response, 'Zamówienia')
#     self.assertNotContains(response, 'Hello World!')
#
#     # test the context
#     self.assertEqual(response.context_data['orders'].count(), 3)
#     self.assertEqual(response.context_data['total'], 3)
#     self.assertEqual(response.context_data['provinces'].count(), 2)
#     self.assertEqual(response.context_data['users'].count(), 2)
#
#     # test the queryset
#     self.assertQuerysetEqual(response.context_data['orders'],
#                              ['<Order: Order 1>', '<Order: Order 2>', '<Order: Order 3>'])
#     self.assertQuerysetEqual(response.context_data['provinces'],
#                              ['<Province: Dolnośląskie>', '<Province: Kujawsko-pomorskie>'])
#     self.assertQuerysetEqual(response.context_data['users'], ['<User: admin>', '<User: test>'])
#
#     # test the html
#     self.assertContains(response, '<h1>Zamówienia</h1>')
#     self.assertContains(response, '<h2>Wszystkie zamówienia</h2>')
#     self.assertContains(response, '<h2>Województwa</h2>')
#     self.assertContains(response, '<h2>Pracownicy</h2>')
#     self.assertContains(response, '<h3>Województwo: Dolnośląskie</h3>')
#     self.assertContains(response, '<h3>Województwo: Kujawsko-pomorskie</h3>')
#     self.assertContains(response, '<h3>Pracownik: admin</h3>')
#     self.assertContains(response, '<h3>Pracownik: test</h3>')
#     self.assertContains(response, '<td>Order 1</td>')
#     self.assertContains(response, '<td>Order 2</td>')
#     self.assertContains(response, '<td>Order 3</td>')
#     self.assertContains(response, '<td>admin</td>')
#     self.assertContains(response, '<td>test</td>')
#     self.assertContains(response, '<td>1</td>')
#     self.assertContains(response, '<td>2</td>')
#     self.assertContains(response, '<td>3</td>')

@method_decorator(login_required, name='dispatch')
class ApplicationsView(View):
    def get(self, request):
        items = Vs1YkBaformsSubmissions.objects.all()
        user = request.user
        if user.is_superuser:
            update_items(items)
            applications = Applications.objects.all().order_by('hired')
            regions = Applications.objects.values_list('work_region', flat=True).distinct()
            return render(request, 'applications.html', {'applications': applications, 'regions': regions})
        else:
            return redirect('testowy')
