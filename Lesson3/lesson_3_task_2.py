from smartphone import Smartphone

catalog = []


phone1 = Smartphone("Samsung", "Galaxy S21", "+79260236040")
phone2 = Smartphone("Nokia", "Model 3", "+79261235040")
phone3 = Smartphone("Apple", "Iphone 11", "+79170237040")
phone4 = Smartphone("Google", "Pixel 5", "+79300231240")
phone5 = Smartphone("Xiaomi", "Redmi Note 10", "+79097076040")


catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)


for phone in catalog:
    print(f"{phone.brand} {phone.model} - {phone.phone_number}")