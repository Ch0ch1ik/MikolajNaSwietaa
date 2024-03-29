"""MikolajNaSwieta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ManageTool import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.Test.as_view(), name='testowy'),
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    # path('register/', views.Register.as_view(), name='register'),
    path('users/', views.Users.as_view(), name='users'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('update_application/<int:pk>', views.UpdateApplication.as_view(), name='update_application'),
    path('deny_application/<int:id>', views.deny_application, name='deny_application'),
    path('confirm_appointment/<int:id>', views.confirm_appointment, name='confirm_appointment'),
    path('save_note/<int:id>', views.save_note, name='save_note'),
    path('confirm_payment/<int:id>', views.confirm_payment, name='confirm_payment'),
    path('confirm_order/<int:id>', views.confirm_order, name='confirm_order'),
    path('confirm_accomplished/<int:id>', views.confirm_accomplished, name='confirm_accomplished'),
    path('cancel_order/<int:id>', views.cancel_order, name='cancel_order'),
    path('update_order/<int:pk>', views.UpdateOrder.as_view(), name='update_view'),
    path('show_filtered_applications/', views.show_filtered_applications, name='show_filtered_applications'),
    path('show_filtered_orders/', views.show_filtered_orders, name='show_filtered_orders'),
    path('contracts/', views.ContractsListView.as_view(), name='contracts'),
    path('create_contract/<int:id>', views.CreateContractEmploymentView.as_view(), name='create_contract'),
    path('create_contract_for_user/<int:id>', views.CreateContractForUserView.as_view(), name='create_contract_by_user_id'),
    path('edit_contract/<int:id>', views.EditContractEmploymentView.as_view(), name='edit_contract'),
    path('sign_contract/<int:id>', views.SignContractView.as_view(), name='sign_contract'),
    path('contract_details/<int:pk>', views.ContractDetailsView.as_view(), name='contract_details'),
    path('show_contract/', views.show_contract, name='show_contract'),
    path('show_contract_pdf/<int:id>', views.GeneratePdf.as_view(), name='show_contract_pdf'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('update_all_data', views.update_all_data, name='update_all_data'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('set_passowrd', views.SetPasswordView.as_view(), name='set_password'),
]
