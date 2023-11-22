import os as o
import time as t
import sys as s
import random as r
from colorama import init, Fore
init(autoreset=True)
print("Welcome to Strong Password")
print("Create New Account With 1")
username = input("Username:")
if username == "1":
    newusername = input("New Username:")
    newpassword = input("New Password:")
    o.mkdir(newusername)
    o.chdir(newusername)
    passfile = "pass.key"
    usrfile = "usr.key"
    passfile2 = open(passfile, "w")
    usrfile2 = open(usrfile, "w")
    usrfile2.write(newusername)
    passfile2.write(newpassword)
    t.sleep(10)
    print(Fore.GREEN + "Created")
    t.sleep(1)
    if s.platform == "win32":
        o.system("cls")
        quit()
    else:
        o.system("clear")
        quit()
else:
    password = input("Password:")
    o.chdir(username)
    usrfile3 = "usr.key"
    passfile3 = "pass.key"
    usr2file = open(usrfile3, "r")
    pass2file = open(passfile3, "r")
    if usr2file.read() == username:
        if pass2file.read() == password:
            if s.platform == "win32":
                o.system("cls")
                name = input("Your Name (For Strong Password):")
                age = input("Your Age (For Strong Password):")
                note = input("Note From You:")
                smallabc = input("Select A Small ABC:")
                marks = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")" , "_", "-", "+", "="]
                numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "1000", "100", "200", "300", "4000000000000000000000000", "600000000000000000000000000000000", "000000000000000000000000000000000", "33333333333333333"]
                marksr = r.choice(marks)
                numbersr = r.choice(numbers)
                print(f"Your Strong Password Is: {name}{age}{note}{marksr}{numbersr}{smallabc}")
                passwordtxt = "password.txt"
                passtxt = open(passwordtxt, "a")
                passtxt.write(f"\nPassword: {name}{age}{note}{marksr}{numbersr}{smallabc}")