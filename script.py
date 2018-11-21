from contacts_app.models import Person, Address, Phone, Email, Groups

#
# # Person.objects.create(name= "Adam", surname="Adamka", description="Ziomek ze szkolenia")
#
#
#
# adr1 = Address.objects.create(city="Warszawa", street="Prosta", house="51")
# adr2 = Address.objects.create(city="Warszawa", street="Warszawska", house= 1, flat=2)
# adr3 = Address.objects.create(city="Kraków", street="Wawelska", house= 3, flat=55)
# adr4 = Address.objects.create(city="Gorzów Wielkopolski", street="Długa", house= 114, flat=12)
# adr5 = Address.objects.create(city="Hajnówka", street="Biebrzańska", house= 24)
#
#
# person1 = Person.objects.get(pk=1)
# person1.address = adr1
# person1.save()
#
#
# p1 = Person.objects.create(name= "Piotr", surname="Pietrzak", description="Kolejny dobry ziomek", address=adr1)
# p2 = Person.objects.create(name= "Kazimierz", surname="Staszewski", description="Kultowy ziom", address=adr2)
# p3 = Person.objects.create(name= "Grzegorz", surname="Brzęczyszczykiewicz", description="Ziomek z filmu", address=adr5)
# Person.objects.create(name= "Adam", surname="Małysz", description="Skoczek", address=adr3)
# Person.objects.create(name= "Michał", surname="Michalak", description="nie znam człowieka", address=adr4)
# Person.objects.create(name= "Karmnik", surname="Staniszewski", description="ziome z wywiadu", address=adr2)
# Person.objects.create(name= "Kuba", surname="Rozpruwacz", description="taki tam", address=adr5)
# Person.objects.create(name= "Gerwazy", surname="Gorczycki", description="Końpozytor", address=adr1)
# Person.objects.create(name= "Mikołaj", surname="Gomułka", description="Inszy końpozytor", address=adr1)
# Person.objects.create(name= "Fryderyk", surname="Szopen", description="Najlepsiejszy nasz końpozytor", address=adr1)
# Person.objects.create(name= "Halina", surname="Kiepska", description="Pielęgniarka jakich mało", address=adr1)
# Person.objects.create(name= "Rozalia", surname="Kiepska", description="Babka, kanalia i wrzód", address=adr1)
# Person.objects.create(name= "Mieczysław", surname="Władysławowski", description="taki tam", address=adr3)
# Person.objects.create(name= "Kocimir", surname="Kotowski", description="ktoś", address=adr3)
# Person.objects.create(name= "Kaczor", surname="Donald", description="srasznie sepleni", address=adr3)
# Person.objects.create(name= "Andy", surname="Anderson", description="..kiedy byłem na wojnie...", address=adr3)
# Person.objects.create(name= "Earl", surname="Hickey", description="dobry ziomek, choć jełop", address=adr3)
#
#
#
# Email.objects.create(email_adress="email@mail.com", email_description="jakis mail", person=p1)
# Email.objects.create(email_adress="email2tej@mail.com", email_description="email sluzbowy", person=p1)
# Email.objects.create(email_adress="inny@email.com", email_description="email", person=p2)
# Email.objects.create(email_adress="kolejny@email.com", email_description="email domowy", person=p3)
#
#
#
# Phone.objects.create(phone_number=12345678, phone_description="domowy", person=p1)
# Phone.objects.create(phone_number=12345328, phone_description="domowy in", person=p2)
# Phone.objects.create(phone_number=987654321, phone_description="sluzbowy", person=p2)
# Phone.objects.create(phone_number=333345678, phone_description="dommmowy", person=p3)
#


Groups.objects.create(group_name="Grupa pierwsza")
Groups.objects.create(group_name="Grupa druga")
Groups.objects.create(group_name="Grupa trzecia")
Groups.objects.create(group_name="Grupa czwarta")
