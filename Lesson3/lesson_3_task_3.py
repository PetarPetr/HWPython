from lesson_3_task_3 import Address, Mailing

to_address = Address("12345","Москва", "Улица1", "Дом2", "Квартира3")
from_address = Address("54321","Рязань", "Улица2", "Дом3", "Квартира4")

mailing_instance = Mailing(to_address,from_address, 500, "ABC321")

print("Адресс назначения:", mailing_instance.to_address.index,mailing_instance.to_address.city, mailing_instance.to_address.street, mailing_instance.to_address.house, mailing_instance.to_address.apartment)

print("Адресс отправителя:", mailing_instance.from_address.index,mailing_instance.from_address.city, mailing_instance.from_address.street, mailing_instance.from_address.house, mailing_instance.from_address.apartment)

print("Стоимость:", mailing_instance.cost)
print("Трек-номер:", mailing_instance.track)