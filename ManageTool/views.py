import json
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, ListView, CreateView, DetailView
from jsignature.forms import JSignatureField

from ManageTool.extract import json_extract
from ManageTool.forms import ContractEmploymentForm, ContractSignForm

from ManageTool.items_funcs import update_items
from ManageTool.models import Vs1YkBaformsSubmissions, Order, Applications, ContractEmployment


# Create your views here.
@method_decorator(login_required(login_url='accounts/login'), name='dispatch')
class IndexView(View):
    """Class based view for index page. It shows all orders and allows to assign them to users. """

    def get(self, request):
        user = request.user
        if user.is_superuser:
            # items = Vs1YkBaformsSubmissions.objects.all()
            # update_items(items)
            visit_types = ['Wizyta firmowa', 'Wizyta przedszkolna', 'Wizyta prywatna']
            orders = Order.objects.filter(type__in=visit_types).defer('order_details').order_by('cancelled',
                                                                                                'accomplished')
            total = 0
            for order in orders:
                for k, v in order.products.items():
                    if order.type != 'Wizyta prywatna':
                        total += (int(k) * int(v)) * 1.23
                    else:
                        total += int(k) * int(v)
            # provinces = Order.objects.values_list('province', flat=True).distinct()
            # print(provinces)
            provinces = ['mazowieckie', 'śląskie', 'pomorskie', 'dolnośląskie', 'kujawsko-pomorskie', 'lubelskie',
                         'lubuskie', 'łódzkie', 'małopolskie', 'opolskie', 'podkarpackie', 'podlaskie',
                         'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie']
            users = User.objects.all()
            # user list with contracts bounden to them
            santas = users.filter(order__assigned_to__isnull=False).distinct()
            users = users.filter(bounded_user__isnull=False).distinct()

            # show users with contracts bounden to them

            return render(request, 'index.html',
                          {'orders': orders, 'total': total, 'provinces': provinces, "users": users,
                           'visit_types': visit_types, 'santas': santas})
        else:
            orders = Order.objects.filter(assigned_to=user).order_by('cancelled', 'accomplished')
            contracts = ContractEmployment.objects.filter(bounded_user=user)
            # check if user has any contract without signature
            for contract in contracts:
                if contract.signature is None:
                    message = f'Masz niepodpisaną umowę nr {contract.id} . Proszę o uzupełnienie danych i podpis.'
            return render(request, 'user_main.html', {'orders': orders, 'contracts': contracts, 'message': message})

    def post(self, request):
        user_id = int(request.POST['assign'])
        id = request.POST['order_id']
        order = Order.objects.get(id=id)
        order.assigned_to.clear()
        order.assigned_to.add(user_id)
        order.save()
        return redirect('index')


# class Login(View):
#     def get(self, request):
#         return render(request, 'registration/login.html')
#
#     def post(self, request):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(username=email, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('index')
#             else:
#                 return redirect('testowy')
#         else:
#             return redirect('register')
#
#
# class Register(View):
#     def get(self, request):
#         return render(request, 'registration/register.html')
#
#     def post(self, request):
#         first_name = request.POST['name']
#         last_name = request.POST['surname']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         if password == password2 and first_name and last_name and email and password:
#             User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name,
#                                      password=password)
#             return redirect('login')
#         else:
#             msg = 'Niepoprawne dane'
#             return render(request, 'registration/register.html', {'msg': msg})
#
#
# class Logout(View):
#     def get(self, request):
#         logout(request)
#         return redirect('index')


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


def confirm_appointment(request, id):
    """Confirm application appointment with given id and redirect to applications page"""
    application = Applications.objects.get(id=id)
    application.appointment_made = True
    application.save()
    return redirect('applications')


class UpdateOrder(UpdateView):
    model = Order
    fields = ['type', 'province', 'city', 'district', 'facility_name', 'street', 'street_number', 'house_number',
              'zip_code', 'town', 'arrival_fee', 'company_name', 'name_surname', 'nip', 'facility_address', 'phone',
              'email', 'visit_length', 'visit_date', 'visit_time']
    template_name = 'order_update_form.html'
    success_url = "/"


@method_decorator(login_required, name='dispatch')
class ApplicationsView(View):
    def get(self, request):

        user = request.user
        if user.is_superuser:
            # items = Vs1YkBaformsSubmissions.objects.all()
            # update_items(items)

            positions = Applications.objects.values_list('position', flat=True).distinct()
            applications = Applications.objects.all().filter(position=positions[0]).order_by('denied',
                                                                                             'appointment_made',
                                                                                             '-created')
            regions = Applications.objects.values_list('work_region', flat=True).distinct()
            return render(request, 'applications.html',
                          {'applications': applications, 'regions': regions, 'positions': positions})
        else:
            return redirect('testowy')


class UpdateApplication(UpdateView):
    model = Applications
    fields = ['name_surname', 'phone', 'email', 'position', 'work_region', 'age', 'height', 'weight',
              'worked_with_children',
              'similar_work_experience', 'driver_license', 'car', 'work_24_12', 'desc_and_experience', 'hired',
              'denied', 'score',
              'appointment_made', 'own_notes']
    template_name = 'application_update_form.html'
    success_url = "/applications"


def deny_application(request, id):
    """Deny application with given id and redirect to applications page"""
    application = Applications.objects.get(id=id)
    if not application.denied:
        application.denied = True
    else:
        application.denied = False
    application.save()
    return redirect('applications')


def save_note(request, id):
    """Save note for application with given id and redirect to applications page"""
    application = Applications.objects.get(id=id)
    note_id = 'own_notes' + str(id)
    note = request.GET[note_id]
    application.own_notes = note
    application.save()
    return redirect('applications')


def show_filtered_applications(request):
    """Show filtered applications"""
    checkboxes = request.GET.getlist('filter_by')
    applications = Applications.objects.all()
    score = request.GET.get('score')
    region = request.GET.get('region')
    position = request.GET.get('position')
    if region is not None:
        if region == 'Wszystkie':
            pass
        else:
            applications = applications.filter(work_region=region)
    if position is not None:
        applications = applications.filter(position=position)
    if score is not None:
        applications = applications.filter(score__gte=score)
    if checkboxes is not None:
        if 'work_24_12' in checkboxes:
            applications = applications.filter(work_24_12='TAK')
        if 'not_appointment_made' in checkboxes:
            applications = applications.filter(appointment_made=False)
        if 'year' in checkboxes:
            curr_year = datetime.now().year
            applications = applications.filter(created__startswith=str(curr_year))
        if 'driver_license' in checkboxes:
            applications = applications.filter(driver_license='TAK')
        if 'car' in checkboxes:
            applications = applications.filter(car='TAK')

    applications.order_by('denied', 'appointment_made', '-created')
    regions = Applications.objects.values_list('work_region', flat=True).distinct()
    return render(request, 'apps_table_body.html', {'applications': applications, 'regions': regions})


def show_filtered_orders(request):
    """Show filtered applications"""
    checkboxes = request.GET.getlist('filter_by')
    visit_types = ['Wizyta firmowa', 'Wizyta przedszkolna', 'Wizyta prywatna']
    orders = Order.objects.filter(type__in=visit_types).defer('order_details')
    region = request.GET.get('region')
    type = request.GET.get('type')
    bounded_santa = request.GET.get('bounded_santa')
    if region is not None:
        if region == 'Wszystkie':
            pass
        else:
            orders = orders.filter(province=region)
    if type is not None and type != '':
        orders = orders.filter(type=type)
    if bounded_santa is not None and bounded_santa != '':
        orders = orders.filter(assigned_to=bounded_santa)
    if checkboxes is not None:
        if 'not_confirmed' in checkboxes:
            orders = orders.filter(confirmed=False)
        if 'year' in checkboxes:
            curr_year = datetime.now().year
            orders = orders.filter(created__startswith=str(curr_year))
        if 'not_paid' in checkboxes:
            orders = orders.filter(paid_made=False)
        if 'santa' in checkboxes:
            orders = orders.filter(assigned_to__isnull=True)
    total = 0
    for order in orders:
        for k, v in order.products.items():
            if order.type != 'Wizyta prywatna':
                total += (int(k) * int(v)) * 1.23
            else:
                total += int(k) * int(v)
    users = User.objects.all()
    santas = users.filter(order__assigned_to__isnull=False).distinct()
    users = users.filter(bounded_user__isnull=False).distinct()
    orders.order_by('cancelled', 'accomplished', '-created')
    provinces = Order.objects.values_list('province', flat=True).distinct()
    return render(request, 'orders_table_body.html',
                  {'orders': orders, 'provinces': provinces, 'users': users, 'visit_types': visit_types,
                   'total': total, 'san': santas})


class Test(View):
    def get(self, request):
        # from ManageTool.forms import ContractEmploymentForm
        # form = ContractEmploymentForm()

        return render(request, 'testowy.html')

    def post(self, request):
        return redirect('testowy')


class ContractsListView(View):
    def get(self, request):
        user = request.user
        if user.is_superuser:
            contracts = ContractEmployment.objects.all()
        else:
            contracts = ContractEmployment.objects.filter(bounded_user=user)
        return render(request, 'contracts.html', {'contracts': contracts})



class CreateContractEmploymentView(View):

    def get(self, request, id):
        application = Applications.objects.get(id=id)
        try:
            user = User.objects.get(username=application.email)
        except User.DoesNotExist:
            user = User.objects.create_user(username=application.email, email=application.email)
            user.password = f'User{application.id}password'
            user.save()
        form = ContractEmploymentForm(initial={'bounded_user': user, 'email': user.email})
        form.save(commit=False)
        return render(request, 'contract_employment_form.html', {'form': form, 'application': application})

    def post(self, request, id):
        form = ContractEmploymentForm(request.POST)
        application = Applications.objects.get(id=id)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            application.hired = True
            application.save()
            return redirect('applications')
        else:
            return render(request, 'contract_employment_form.html', {'form': form})


class SearchView(View):
    def get(self, request):
        data = self.request.GET['search_box']
        search_in_applications = Applications.objects.filter(Q(name_surname__icontains=data) | Q(
            phone__icontains=data) | Q(email__icontains=data))
        search_in_orders = Order.objects.filter(Q(bounded_to__icontains=data) | Q(name_surname__icontains=data) | Q(
            phone__icontains=data) | Q(email__icontains=data))
        search_in_users = User.objects.filter(Q(first_name__icontains=data) | Q(last_name__icontains=data) | Q(
            email__icontains=data))
        return render(request, 'search.html',
                      {'search_in_applications': search_in_applications, 'search_in_orders': search_in_orders,
                       'search_in_users': search_in_users})


def update_all_data(request):
    items = Vs1YkBaformsSubmissions.objects.all()
    update_items(items)
    return redirect('index')


class ContractDetailsView(DetailView):
    template_name = 'contract_details.html'
    model = ContractEmployment
    context_object_name = 'contract'


class EditContractEmploymentView(View):
    def get(self, request, id):
        contract = ContractEmployment.objects.get(id=id)
        form = ContractEmploymentForm(instance=contract)
        return render(request, 'contract_employment_form.html', {'form': form, 'contract': contract})

    def post(self, request, id):
        contract = ContractEmployment.objects.get(id=id)
        form = ContractEmploymentForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contracts')
        else:
            return render(request, 'contract_employment_form.html', {'form': form, 'contract': contract})




class CreateUserView(View):
    pass


class CreateContractForUserView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = ContractEmploymentForm(initial={'bounded_user': user, 'email': user.email})
        form.save(commit=False)
        return render(request, 'contract_employment_form.html', {'form': form, 'user': user})

    def post(self, request, id):
        form = ContractEmploymentForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('users')
        else:
            return render(request, 'contract_employment_form.html', {'form': form})


class SignContractView(View):
    def get(self, request, id):
        user = request.user
        if user.is_authenticated:
            contract = ContractEmployment.objects.get(id=id)
            form = ContractSignForm()
            return render(request, 'sign_contract.html', {'contract': contract, 'form': form})
        else:
            return redirect('login')
