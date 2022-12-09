import string
import random


# import Num & Caracters
digits = list(string.digits)
str_uper = list(string.ascii_uppercase)
str_lower = list(string.ascii_lowercase)
punctuation = list(string.punctuation)

# Note..
# str_uper_lower = list(string.ascii_letters)
# ascii_letters = ascii_uppercase & ascii_lowercase

# shuffle Every thing first
random.shuffle(digits)
random.shuffle(str_uper)
random.shuffle(str_lower)
random.shuffle(punctuation)

# Total Num Of Password
pass_num = 20


# Num Of Every Part In Password
digits_num = round(pass_num*(30/100))
uper_num = round(pass_num*(30/100))
lower_num = round(pass_num*(30/100))
punctuation_num = round(pass_num*(10/100))

# Password List
password = []

# loop to make password
for i in range(digits_num):
    password.append(digits[i])
    password.append(str_uper[i])
    password.append(str_lower[i])
for i in range(punctuation_num):
    password.append(punctuation[i])


# shuffle password
random.shuffle(password)

# join password as string
password = ''.join(password)


print(f'Your password:\n{password}')
print(f'password Length: {len(password)}')
