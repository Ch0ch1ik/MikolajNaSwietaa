import json
from collections import defaultdict

from django.core.exceptions import ObjectDoesNotExist

from ManageTool.extract import json_extract
from ManageTool.models import Order, Applications, Province


def update_items1(items):
    def update_items1(items):
        for item in items:
            if item.title == 'Praca':
                try:
                    application = Applications.objects.get(bounded_to=item.id)
                except ObjectDoesNotExist:
                    new_application = Applications.objects.create(bounded_to=item.id)
                    new_application.created = item.date_time
                    new_application.score = 0
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
                                if value == 'TAK':
                                    new_application.score += 1
                                    new_application.experience = True
                                new_application.worked_with_children = value
                            elif key == 'Pracowałeś/aś jako Świety Mikołaj/Elf/Śniezynka?':
                                if value == 'TAK':
                                    new_application.score += 1
                                new_application.similar_work_experience = value
                            elif key == 'Posiadasz prawo jazdy Kat. B?':
                                if value == 'TAK':
                                    new_application.score += 2
                                new_application.driver_license = value
                            elif key == 'Czy posiadasz własny środek transportu? (samochód)':
                                if value == 'TAK':
                                    new_application.score += 2
                                new_application.car = value
                            elif key == 'Czy praca w Wigilię 24 grudnia również Cię interesuje?':
                                if value == 'TAK':
                                    new_application.score += 3
                                new_application.work_24_12 = value
                            elif key == 'Opisz siebie i swoje doświadczenie w kilku słowach':
                                new_application.desc_and_experience = value.encode('unicode_escape')
                            elif key == 'CV (nie wymagane)':
                                pass
                            elif key == '':
                                pass
                            else:
                                print('Unknown key: {}'.format(key))

                    new_application.save()

            elif item.title == 'Umowa o dzieło stawka godzinowa':
                pass
            elif item.title == 'Umowa o dzieło stawka za wizytę':
                pass
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
                                # print('Unknown key: {}'.format(key))
                    set_product(new_order)
        return items


def update_items(items):
    for item in items:
        if item.title == 'Praca':
            pass
            # try:
            #     application = Applications.objects.get(bounded_to=item.id)
            # except ObjectDoesNotExist:
            #     new_application = Applications.objects.create(bounded_to=item.id)
            #     new_application.created = item.date_time
            #     new_application.score = 0
            #     data = json.loads(item.message)
            #     for mess in data:
            #         titles = []
            #         values = []
            #         titles.append(mess['title'])
            #         values.append(mess['message'])
            #         result = dict(zip(titles, values))
            #         for key, value in result.items():
            #             # TODO: reformat below to switch cases
            #             if key == 'Imię i Nazwisko':
            #                 new_application.name_surname = value
            #             elif key == 'Nr telefonu':
            #                 new_application.phone = value
            #             elif key == 'e-mail':
            #                 new_application.email = value
            #             elif key == 'Praca jako':
            #                 new_application.position = value
            #             elif key == 'Gdzie chcesz pracować?':
            #                 new_application.work_region = value
            #             elif key == 'Ile masz lat?':
            #                 new_application.age = value
            #             elif key == 'Wzrost (cm)':
            #                 new_application.height = value
            #             elif key == 'Waga (kg)':
            #                 new_application.weight = value
            #             elif key == 'Czy masz doświadczenie w pracy z dziećmi?':
            #                 if value == 'TAK':
            #                     new_application.score += 1
            #                     new_application.experience = True
            #                 new_application.worked_with_children = value
            #             elif key == 'Pracowałeś/aś jako Świety Mikołaj/Elf/Śniezynka?':
            #                 if value == 'TAK':
            #                     new_application.score += 1
            #                 new_application.similar_work_experience = value
            #             elif key == 'Posiadasz prawo jazdy Kat. B?':
            #                 if value == 'TAK':
            #                     new_application.score += 2
            #                 new_application.driver_license = value
            #             elif key == 'Czy posiadasz własny środek transportu? (samochód)':
            #                 if value == 'TAK':
            #                     new_application.score += 2
            #                 new_application.car = value
            #             elif key == 'Czy praca w Wigilię 24 grudnia również Cię interesuje?':
            #                 if value == 'TAK':
            #                     new_application.score += 3
            #                 new_application.work_24_12 = value
            #             elif key == 'Opisz siebie i swoje doświadczenie w kilku słowach':
            #                 new_application.desc_and_experience = value.encode('unicode_escape')
            #             elif key == 'CV (nie wymagane)':
            #                 pass
            #             elif key == '':
            #                 pass
            #             else:
            #                 print('Unknown key: {}'.format(key))
            #
            #     new_application.save()

        elif item.title == 'Umowa o dzieło stawka godzinowa':
            pass
        elif item.title == 'Umowa o dzieło stawka za wizytę':
            pass
        elif item.title == 'Umowa o dzie?o stawka godzinowa':
            pass
        elif item.title == 'Umowa o dzie?o stawka za wizyt?':
            pass
        else:
            try:
                order = Order.objects.get(bounded_to=item.id)
            except ObjectDoesNotExist:
                new_order = Order.objects.create(bounded_to=item.id)
                new_order.type = item.title
                new_order.created = item.date_time

                data = json.loads(item.message)
                d = defaultdict(str)
                for mess in data:

                    if ("35" or "226" or "164") in mess['field_id']:
                        new_order.marketing_approval = True
                    if ("36" or "227" or "165") in mess['field_id']:
                        new_order.reminder_approval = True
                    if mess['title'] == "Województwo":
                        try:
                            new_order.province = Province.objects.get(name=mess['message'])
                        except ObjectDoesNotExist:
                            new_province = Province.objects.create(name=mess['message'])
                            new_order.province = new_province
                    else:
                        d[mess['title']] = mess['message']

                new_order.city = d['Miasto']
                new_order.district = d['Dzielnica']
                new_order.facility_name = d['Nazwa placówki']
                new_order.street = d['Ulica']
                new_order.street_number = d['Nr domu']
                new_order.house_number = d['Nr mieszkania']
                new_order.zip_code = d['Kod pocztowy']
                new_order.town = d['Miejscowość']
                new_order.arrival_fee = d['Opłata dojazdowa']
                new_order.company_name = d['Nazwa firmy']
                new_order.name_surname = d['Imię i nazwisko zamawiającego']
                new_order.nip = d['NIP']
                new_order.facility_address = d['Adres siedziby']
                new_order.phone = d['Telefon kontaktowy']
                new_order.email = d['Adres e-mail']
                new_order.visit_length = d['Długość wizyty Mikołaja']
                new_order.visit_date = d['Data wizyty']
                new_order.visit_time = d['Przedział godzinowy wizyty']
                new_order.pref_visit_time = d['Preferowana godzina wizyty']
                new_order.additional_info = d['Informacje dodatkowe']
                true = True
                false = False
                new_order.order_details = d['Szczegóły zamówienia']
                new_order.arrival_fee = d['Opłata dojazdowa']
                new_order.save()
                products = json.loads(new_order.order_details)
                print(products)



                #     titles = []
                #     values = []
                #     titles.append(mess['title'])
                #     values.append(mess['message'])
                #     result = dict(zip(titles, values))
                #     for key, value in result.items():
                #         # TODO: reformat below to switch cases
                #
                #
                #         elif 'Opłata dojazdowa' in key:
                #             fee = 0
                #             if value.__contains__('"84":{}'):
                #                 fee = 0
                #             elif value.__contains__('84":{"3"'):
                #                 fee = 120
                #             elif value.__contains__('84":{"2"'):
                #                 fee = 80
                #             elif value.__contains__('84":{"1"'):
                #                 fee = 40
                #             elif value.__contains__('"196":{}'):
                #                 fee = 0
                #             elif value.__contains__('196":{"3"'):
                #                 fee = 120
                #             elif value.__contains__('196":{"2"'):
                #                 fee = 80
                #             elif value.__contains__('196":{"1"'):
                #                 fee = 40
                #             elif value.__contains__('"257":{}'):
                #                 fee = 0
                #             elif value.__contains__('257":{"3"'):
                #                 fee = 120
                #             elif value.__contains__('257":{"2"'):
                #                 fee = 80
                #             elif value.__contains__('257":{"1"'):
                #                 fee = 40
                #             new_order.arrival_fee = fee
                #
                #
                #
                #
                #         if key == 'Szczegóły zamówienia':
                #             # if value.__contains__('"205":{"2":'):
                #             #     price = 290
                #             #     product = 'Przedszkole WizytaStandard (do 60 min.)'
                #             # else:
                #             #     price = 0
                #
                #             new_order.order_details = value
                #
                #             # products = (eval(value)['products'])
                #             # cos = json_extract(products, 'title')
                #             # for _ in cos:
                #             #     new_order.products += _+','
                #         elif key == '':
                #             pass
                #         else:
                #             pass
                #             # print('Unknown key: {}'.format(key))
                # set_product(new_order)
    return items


def set_product(order):
    if type(order.order_details) == str:
        true = True
        false = False
        data = [json.loads(order.order_details)]
        quantities = [int(item) for item in json_extract(data, 'quantity')]
        prices = [int(item) for item in json_extract(data, 'price')]
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
