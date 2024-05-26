import re
from .models import *
import telebot


def validate_phone_number(phone_number):
    uzbek_phone_pattern = re.compile(r'^998\d{9}$')
    return bool(re.match(uzbek_phone_pattern, phone_number))

def validate_student(phone_number):
    phone_number = RegisterStudent.objects.filter(phone_number=phone_number).exists()
    return not phone_number




    