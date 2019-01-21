#!/usr/bin/python3.6
from random import choices 
from string import punctuation,ascii_letters,digits

def request_username():
    while True:
        username=str(input("enter at least 6 character and below than 14 characters  for username >>> ").lower())
        if len(username) < 5 or len(username) > 14:
            print("The user must fill more than 5 characters and bellow than 14")
            continue
        break
    return username
def gen_password():
    answer=int(input("Enter your length for generate pass >>> "))
    for i in range(10):
        password="".join(choices(digits+punctuation+ ascii_letters,k=answer))
        print("{}). {}".format(i+1,password))
def sim_gen_password():
    charlist={
          'a':('A','a','@','/\\','/-\\','4'),'b':('b','B','8','|3','13','!3','(3','|-]','j3'),
          'c':('c','C','(','<','[','{'),'d':('d','D','|)','T)','|>','17','cI'),
          'e':('e','E','3','[-','|=-'),'f':('F','f','|=','|#'),
          'g':('g','G','6','9','C-','gee','(_+'),'h':('h','H','#','|-|',']-[',':-:','|~|','1-1','(-)'),
          'i':('i','L','1','[]','|','!','eye','3y3',']['), 'j':('J','j',',_|','_|','._|','._]'),
          'k':('K','k','>|','|<','/<','1<','|c','|C'),'l':('L','l','|_','7','|'),
          'm':('M','m','nn','JVl','Jv|','|\\/|','^^'),'n':('N','n','^','^','|V','|\\|','{\\}','^/'),
          'o':('O','o','0','Q','()','<>','[]'),'p':('|*','|O','|o','9','|>','|7'),
          'q':('Q','q','<|','&','0_'),'r':('R','r','12','|^','|2','I2'),
          's':('S','s','$','z','2'),'t':('T','t','+','7','"|"','-|-'),
          'u':('U','u','(_)','|_|','V','v',),'v':('V','v'),
          'w':('w','W','1N','\\N','(n)'),'x':('X','x','ecks',')(','><','}{'),
          'y':('Y','y','j','4','7'),'z':('Z','z','2','7_','s','%','-|_')
          }
    gen_pass_list=[]
    password=[]
    print("You Username is {} choice from below list ")
    for i  in range(10):
        for char in username:
            password+=random.choice(charlist[char])
        gen_pass_list.append(''.join(password))
        password=[]
        print("{}). {}".format(i+1,gen_pass_list[i]))
def help():
    while True:
        answer=int(input("1.simple and wihtout remember format with optional lenght.\n2.strong and with remember format with system set lenght.\n>>>"))
        if answer==1:
            return 1
        elif answer ==2:
            return 2
        else:
            continue  
    
username=request_username()
if help() == 1:
    sim_gen_password()
else:
    gen_password()
