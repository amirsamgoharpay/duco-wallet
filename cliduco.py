import requests
import os
import time
import json
import re
from keyboard import is_pressed
from colorama import *
cl = None
strt = "https://server.duinocoin.com"
init(autoreset=True)
print(Fore.BLUE + "hello welcome to cmd wallet")
oper = int(input(Fore.LIGHTCYAN_EX + """please choose your os : 
[1] windows
[2] linux , mac
 """))
if oper == 1 :
    cl = "cls"
if oper == 2 :
    cl = "clear"
os.system(cl)
print(Fore.BLUE +"press enter to enter")
print(Fore.BLUE +"if you want to exit press Esc")
while True :
    if is_pressed("enter"):
        os.system(cl)
        break
    if is_pressed("Esc"):
        os.system(cl)
        print(Fore.MAGENTA + "Good Bye")
        exit()

for i in range(0 , 110 , 10):
    print(Fore.BLACK + Back.YELLOW +f'loading | {i}% | ')
    time.sleep(0.2)
    os.system(cl)

if os.path.exists("ducouser.txt") : 
    with open("ducouser.txt" , "r") as fl :
        cont = fl.read()
        username = re.findall("username : (.*)" , cont)
        username = username[0]
        print(Fore.CYAN + f"welcome back my friend {username}")

else :
    print(Fore.CYAN + "hello , would you please tell your username?")
    input("")
    username= input(Fore.GREEN + "username : ")
    check = (requests.get(f"{strt}/users/{username}")).json()
    check1 = check["success"]
    verify = check["result"]["balance"]["verified"]
    if check1 == True :
        print(Fore.CYAN + f"hello {username}")
    else :
        os.system(cl)
        print(Fore.RED + "sorry but this account is unvalid")
        exit()
    if verify == "yes" :
        verify = True
    else :
        print(Fore.RED + "sorry but your account isn't verified")
        exit()

    print(Fore.CYAN +"""if you want to save your account type yes 
if you dont want type anything you want or nothing :D""")
    save = input(Fore.CYAN +"(yes/no) : ")
    if save == "yes" or save == "y" or save == "Yes" or save == "YES" :
        print(Fore.CYAN +"your username has been saved , you can find it in hidden files")
        with open("ducouser.txt" , "w") as fil :
            fil.write(f"username : {username}")
            os.system("attrib +h ducouser.txt")
    else :
        print(Fore.CYAN +"okay , but you have to type your username when you come to app :d")

#defs 
def balance(user):
    res = requests.get(f"{strt}/users/{user}")
    res = res.json()
    balance = res["result"]["balance"]["balance"]
    return Fore.LIGHTCYAN_EX + f"you have {balance} duco"
#def miners(user):
def donation(username , password , amount ):
    res = requests.get(f"{strt}/transaction?username={username}&password={password}&recipient=Amirsam86&amount={amount}&memo=memo")
    res = res.json()
    if res["success"] == True :
        res = res["result"]
        hash = re.findall("OK,Successfully transferred funds,(.*)" , res)
        return f"thank you so much for donation heres the hash : {hash[0]} "
    if res["success"] == False :
        return "sorry there is an error in transaction"

def transaction(username , password , recipient , amount , memo="memo"):
    res = requests.get(f"{strt}/transaction?username={username}&password={password}&recipient={recipient}&amount={amount}&memo={memo}")
    res = res.json()
    if res["success"] == True :
        res = res["result"]
        hash = re.findall("OK,Successfully transferred funds,(.*)" , res)
        return f"your transaction was successfully , heres the hash : {hash[0]} "
    if res["success"] == False :
        return "sorry there is an error in transaction"
def miners(username):
    res = requests.get(f"{strt}/miners/{username}")
    res = res.json()
    if res["success"] == False :
        print(Fore.RED + f"there is no miner for {username}")
    if res["success"] == True :
        res = res["result"]
        print( Fore.GREEN +"-----------------------------")
        for i in res :
            print( Fore.GREEN + f"""
accepted : {i["accepted"]}
rejected : {i["rejected"]}
difficulty : {i["diff"]}
hashrate : {i["hashrate"]}
pool : {i["pool"]}
thread id : {i["threadid"]}
software : {i["software"]}
-----------------------------
""")
def checktransac(info , ih):
    if ih == 1 :
        res = requests.get(f"{strt}/transactions/{info}")
    if ih == 2 :
        res = requests.get(f"{strt}/id_transactions/{info}")
    res = res.json()
    if res["success"] == True :
        print(Fore.LIGHTGREEN_EX + f"""
recipient : {res["result"]["recipient"]}
sender : {res["result"]["sender"]}
amount : {res["result"]["amount"]}
id : {res["result"]["id"]}
hash : {res["result"]["hash"]}

    """)
    else :
        print(Fore.LIGHTGREEN_EX + "this transaction is not available")

def checkall(username):
    res = requests.get(f"{strt}/user_transactions/{username}")
    res = res.json()
    res = res["result"]
    print( Fore.GREEN +"-----------------------------")
    for i in res :
        print(Fore.GREEN + f"""
amount : {i["amount"]}
date time : {i["datetime"]}
recipient : {i["recipient"]}
sender : {i["sender"]}
id : {i["id"]}
hash : {i["hash"]}
memo : {i["memo"]}
-----------------------------
        """)

#def shop():
#def shopbuy(password):
while True : 
    try :
        print(Fore.GREEN + "what do you want me to do for you ?")
        listdo = Fore.LIGHTMAGENTA_EX + """
[1] remove saved username
[2] check balance
[3] check miners
[4] do transaction
[5] check transaction with hash or id
[6] check recent transaction you have made
[7] shop - coming soon :)
[8] buy from shop - coming soon :)
[9] exit
[10] donation :D"""
        print(listdo)
        dot = input("")
        if dot == "1" :
            try :
                os.remove("ducouser.txt")
                print("your username has been deleted ")
            except FileNotFoundError as error :
                print(Fore.RED + "you didnt save your username so i cant delete it XD")
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "2" :
            balance = balance(username)
            print(Fore.LIGHTCYAN_EX + balance)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "3" :
            miners(username)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "4" :
            amount = input(Fore.LIGHTBLUE_EX + "please enter the amount you want to send :")
            password = input(Fore.LIGHTBLUE_EX + "please enter your password : ")
            recipient = input(Fore.LIGHTBLUE_EX + "please enter the recipient username :  ") 
            memo = input(Fore.LIGHTBLUE_EX + "please enter memo : ")
            resal = transaction(username , password , recipient , amount , memo)
            print(resal)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "5" :
            print(Fore.LIGHTGREEN_EX + "you want to check transaction with hash or id ?")
            ih = int(input(Fore.LIGHTGREEN_EX + """
[1] hash
[2] id
: """))
            if ih == 1 :
                info = input(Fore.LIGHTGREEN_EX + "please enter the hash : ")
            elif ih == 2 :
                info = input(Fore.LIGHTGREEN_EX + "please enter the id : ")
            checktransac(info , ih)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "6" :
            checkall(username)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        elif dot == "7" :
            print(Fore.RED + "coming soon")
        elif dot == "8" :
            print(Fore.RED + "coming soon")
        elif dot == "9" :
            os.system(cl)
            exit()
        elif dot == "10" :

            amount = int(input(Fore.LIGHTBLUE_EX + "please enter the amount you want to donate :"))
            password = input(Fore.LIGHTBLUE_EX + "please enter your password : ")
            resa = donation(username , password , amount )
            print(resa)
            input(Fore.LIGHTGREEN_EX + "press enter")
            os.system(cl)
        else : 
            os.system(cl)

    except KeyboardInterrupt as keyerror :
        os.system(cl)
        print(Fore.MAGENTA + "oh , okay good bye :)")
        exit()