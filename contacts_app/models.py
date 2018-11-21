from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)

    surname = models.CharField(max_length=100)

    description = models.TextField()

    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)


#     relacja jest tutaj, gdyż konstruując model, zamysł był taki, że można mieszkać tylko pod jednym adresem
#     a, pod tym adresem może mieszkać wiele osób. Teoretycznie możnaby się pokusić o dodanie relacji wiele do wielu,
#     ale na tym etapie pracy, spowodowałoby to zbyt wiele komplikacji (a wartość dodana byłaby niewielka)


class Address(models.Model):
    city = models.CharField(max_length=100)

    street = models.CharField(max_length=100)

    house = models.CharField(max_length=50)

    flat = models.CharField(max_length=50, null=True)


#     dwa ostatnie na wypadek, gdyby ktoś mieszkał np pod "7b", lokal "23 (trzeci pokój po lewej)"


class Phone(models.Model):
    phone_number = models.CharField(max_length=25)
    # próbowałem integerem, ale ma to swoje wady: nie dałoby się zapisać wszelkich "+", "00", "*" i innych znaków specjalnych

    phone_description = models.CharField(max_length=150)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    email_adress = models.EmailField()

    email_description = models.CharField(max_length=100)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Groups(models.Model):
    group_name = models.CharField(max_length=100)

    person = models.ManyToManyField(Person)
