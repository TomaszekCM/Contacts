from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from contacts_app.models import Person, Phone, Email, Address, Groups


def main_page_view(request):
    all_persons = Person.objects.all().order_by("surname")

    return render(request, "all contacts.html", {'persons': all_persons})


def new_person_view(request):
    if request.method == "POST":

        new_name = request.POST.get('name')
        new_surname = request.POST.get('surname')
        new_description = request.POST.get('description')

        if not new_name or not new_surname:

            wrong_data = "wrong!"

            return render(request, "new_person.html", {"wrong_data": wrong_data})


        else:
            new_person = Person.objects.create(name=new_name, surname=new_surname, description=new_description)

            new_id = new_person.id

            return HttpResponseRedirect("../show/%s/" % new_id)

    elif request.method == "GET":

        return render(request, "new_person.html")


def modify_person_view(request, id):
    if request.method == "POST":

        new_name = request.POST.get('name')
        new_surname = request.POST.get('surname')
        new_description = request.POST.get('description')

        if not new_name or not new_surname:
            return HttpResponseRedirect("../show/%s/" % id)

        else:
            person = Person.objects.get(id=id)

            person.name = new_name
            person.surname = new_surname
            person.description = new_description
            person.save()

            return HttpResponseRedirect("../../show/%s/" % id)

    elif request.method == "GET":

        person = Person.objects.get(id=id)

        return render(request, "modify_person.html", {"person": person})


def delete_person_view(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect("../../")


def delete_phone(request, id, id2):
    number_to_remove = Phone.objects.get(id=id)
    number_to_remove.delete()
    person = Person.objects.get(id=id2)
    return HttpResponseRedirect("../../../show/%s/" % person.id)


def delete_email(request, id, id2):
    mail_to_remove = Email.objects.get(id=id)
    mail_to_remove.delete()
    person = Person.objects.get(id=id2)

    return HttpResponseRedirect("../../../show/%s/" % person.id)


def delete_address(request, id2):
    person = Person.objects.get(id=id2)
    person.address.delete()
    # w naszej aplikacji nie obsługujemy zapisywania wielu osób pod tym samym, jednym adresem
    # czyli np nie robimy wyszukiwarki osób mieszkających pod danym adresem, więc można śmiało
    # usunąć ten konkretny obiekt (w tym konkretny przypadku, nie mając potrzeby powyższego, nie
    # ma sensu przepisywać wszystkiego, bo zajęło by to zbyt dużo czasu, a kożyść by była żadna).

    return HttpResponseRedirect("../../../show/%s/" % person.id)


def show_person_view(request, id):
    person = Person.objects.get(id=id)

    phones = Phone.objects.filter(person=person)

    emails = Email.objects.filter(person=person)

    ctx = {
        "person": person,
        "phones": phones,
        "emails": emails
    }

    return render(request, "contact_details.html", ctx)


def add_address_view(request, id):
    if request.method == "POST":
        street = request.POST.get("street")
        house = request.POST.get("house")
        flat = request.POST.get("flat")
        city = request.POST.get("city")

        person = Person.objects.get(id=id)

        if flat:
            new_address = Address.objects.create(city=city, house=house, flat=flat, street=street)
            person.address = new_address
            person.save()


        else:
            new_address = Address.objects.create(city=city, house=house, street=street)
            person.address = new_address
            person.save()

        return HttpResponseRedirect("../../show/%s/" % person.id)

    elif request.method == "GET":
        person = Person.objects.get(id=id)

        return render(request, "add_address.html", {'person': person})


def add_phone_view(request, id):
    #  nie robimy walidacji z powodów opisanych w modelach: użytkownik może chcieć wpisać numery z "+" na początku,
    # czy z innymi "#", co będzie poprawne, a walidacja nie pozwoli na wpisanie takiego numeru;
    # przez tak zrobioną walidację, kiedyś nie udało się kupić laptopa Dell'a w USA (był problem właśnie z numerem
    # telefonu, przez co nie dało się zapisać formularza).
    if request.method == "POST":
        new_number = request.POST.get('number')
        new_description = request.POST.get('description')

        person = Person.objects.get(id=id)

        Phone.objects.create(phone_number=new_number, phone_description=new_description, person=person)

        return HttpResponseRedirect("../../show/%s/" % id)

    elif request.method == "GET":
        person = Person.objects.get(id=id)

        return render(request, "add_phone.html", {'person': person})


def add_email_view(request, id):
    if request.method == "POST":
        new_email = request.POST.get('mail')
        new_description = request.POST.get('description')

        person = Person.objects.get(id=id)

        Email.objects.create(email_adress=new_email, email_description=new_description, person=person)

        return HttpResponseRedirect("../../show/%s/" % id)


    elif request.method == "GET":
        person = Person.objects.get(id=id)

        return render(request, "add_email.html", {'person': person})


def all_groups_view(request):
    groups = Groups.objects.all()

    return render(request, "all groups.html", {"groups": groups})


def modify_group_view(request, id):
    if request.method == "POST":

        new_name = request.POST.get("name")

        group = Groups.objects.get(id=id)

        group.group_name = new_name
        group.save()

        return HttpResponseRedirect("../../../groups/")

    elif request.method == "GET":
        group = Groups.objects.get(id=id)

        return render(request, "modify_group.html", {"group": group})


def delete_group_view(request, id):
    group_to_delete = Groups.objects.get(id=id)
    group_to_delete.delete()

    return HttpResponseRedirect("../../../groups/")


def new_group_view(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        Groups.objects.create(group_name=new_name)

        return HttpResponseRedirect("../groups/")

    elif request.method == "GET":

        return render(request, "add_group.html")


def group_details_view(request, id):
    group = Groups.objects.get(id=id)
    all_contacts_in_group = group.person.all()

    return render(request, "group_details.html", {"group": group, "persons": all_contacts_in_group})


def add_person_to_group(request, id):
    if request.method == "POST":
        group_id = request.POST.get("group")
        specific_group = Groups.objects.get(id=group_id)
        person = Person.objects.get(id=id)
        person.groups_set.add(specific_group)
        person.save()

        return HttpResponseRedirect("../../show/%s" % person.id)

    elif request.method == "GET":
        person = Person.objects.get(id=id)
        all_groups = Groups.objects.all()
        ctx = {
            "person": person,
            "all_groups": all_groups,
        }
        return render(request, "add_to_group.html", ctx)


def delete_from_grp(request, id, id2):
    person = Person.objects.get(id=id2)
    group = Groups.objects.get(id=id)
    person.groups_set.remove(group)

    return HttpResponseRedirect("../../../show/%s" % id2)


def person_search_view(request):
    if request.method == "POST":

        search_name = request.POST.get("name")
        search_surname = request.POST.get("surname")
        all_persons = Person.objects.all()

        if not search_name and not search_surname:
            return render(request, "person_search.html")


        elif search_name:
            contacts_with_name = []
            for contact in all_persons:
                if search_name in contact.name:
                    contacts_with_name.append(contact)

            num_of_results = len(contacts_with_name)

            ctx = {
                "contacts": contacts_with_name,
                "name": search_name,
                "num_of_results": num_of_results,

            }

            return render(request, "search_results.html", ctx)


        elif search_surname:
            contacts_with_surname = []
            for contact in all_persons:
                if search_surname in contact.surname:
                    contacts_with_surname.append(contact)

            num_of_results = len(contacts_with_surname)

            ctx = {
                "contacts": contacts_with_surname,
                "name": search_surname,
                "num_of_results": num_of_results,
            }

            return render(request, "search_results.html", ctx)

    else:
        return render(request, "person_search.html")
