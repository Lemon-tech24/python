import time
import phonenumbers
from phonenumbers import geocoder

try_again = True
while try_again:
    print("Mobile Number locator")
    given = str(input("Enter Number: "))
    if given != 0:
        ch_number = phonenumbers.parse((" +"+given),"CH")
        number= geocoder.description_for_number(ch_number, "en")
        print(number)
        time.sleep(1000)
    else:
        try_again = False
