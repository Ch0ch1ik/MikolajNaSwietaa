import json

from django.core.exceptions import ObjectDoesNotExist

from ManageTool.models import Order, Applications


def update_items(items):
    for item in items:
        if item.title == 'Praca':
            try:
                application = Applications.objects.get(bounded_to=item.id)
            except ObjectDoesNotExist:
                new_application = Applications.objects.create(bounded_to=item.id)
                new_application.created = item.date_time
                data = json.loads(item.message)
                for mess in data:
                    titles = []
                    values = []
                    titles.append(mess['title'])
                    values.append(mess['message'])
                    result = dict(zip(titles, values))
                    for key, value in result.items():
                        # TODO: reformat below to switch cases
                        if key == 'Imię i Nazwisko':
                            new_application.name_surname = value
                        elif key == 'Nr telefonu':
                            new_application.phone = value
                        elif key == 'e-mail':
                            new_application.email = value
                        elif key == 'Praca jako':
                            new_application.position = value
                        elif key == 'Gdzie chcesz pracować?':
                            new_application.work_region = value
                        elif key == 'Ile masz lat?':
                            new_application.age = value
                        elif key == 'Wzrost (cm)':
                            new_application.height = value
                        elif key == 'Waga (kg)':
                            new_application.weight = value
                        elif key == 'Czy masz doświadczenie w pracy z dziećmi?':
                            new_application.worked_with_children = value
                        elif key == 'Pracowałeś/aś jako Świety Mikołaj/Elf/Śniezynka?':
                            new_application.similar_work_experience = value
                        elif key == 'Posiadasz prawo jazdy Kat. B?':
                            new_application.driver_license = value
                        elif key == 'Czy posiadasz własny środek transportu? (samochód)':
                            new_application.car = value
                        elif key == 'Czy praca w Wigilię 24 grudnia również Cię interesuje?':
                            new_application.work_24_12 = value
                        elif key == 'Opisz siebie i swoje doświadczenie w kilku słowach':
                            new_application.desc_and_experience = value
                        elif key == 'CV (nie wymagane)':
                            pass
                        elif key == '':
                            pass
                        else:
                            print('Unknown key: {}'.format(key))

                new_application.save()

        else:
            try:
                order = Order.objects.get(bounded_to=item.id)
            except ObjectDoesNotExist:
                new_order = Order.objects.create(bounded_to=item.id)
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
                        # TODO: reformat below to switch cases
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
                            pass
                        else:
                            pass

                new_order.save()

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
    return items
