import random

def get_random_password(len, count):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+`~[]{]\|;:,<.>/?'
    for i in range(count):
        password = ''
        for c in range(len):
            password += random.choice(valid_chars)
        print(password)


get_random_password(5,10)

