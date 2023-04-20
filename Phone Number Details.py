import imp
from time import time
import phonenumbers
from phonenumbers import timezone , geocoder , carrier

user_number = input('Enter your number . with your contry code:')
phone = phonenumbers.parse(user_number)
timee= timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone , 'en')
reg=geocoder.description_for_number(phone,'en')

print(phone)
print(timee)
print(car)
print(reg)

