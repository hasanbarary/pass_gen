#!/usr/bin/python3.6
from random import randint
def upper():
    return chr(randint(65,90))
def lower():
    return chr(randint(97,122))
def other():
    return chr(randint(33,42))
def number():
    return str(randint(0,9))
def request_username():
    while True:
        username=str(input("enter at least 6 character and below than 14 characters  for username >>> ").lower())
        if len(username) < 5 or len(username) > 14:
            print("The user must fill more than 5 characters and bellow than 14")
            continue
        break
    return username
password_list=[]
count_pass='default'
username=request_username()
while True:
    try:
        count_pass=int(input("Enter your Password count >>> "))
        break
    except:
        print("Please Enter number for Count >>> ")
        continue
for count in range(0,10):
    gen_password=[]
    for i in range(0,int(count_pass)):
        rand=randint(1,4)
        if rand == 1:
            gen_password.append(upper())
        elif rand == 2:
            gen_password.append(lower())
        elif rand == 3:
            gen_password.append(other())
        else:
            gen_password.append(number())
    password_list.append(''.join(gen_password))
print("\n you choise from below list \n")
for pass_list_number in range(0,10):
    print('| {}) {} | \n'.format(pass_list_number+1,password_list[pass_list_number]))
