import pandas as pd

import Accounts

exec(open("Menu.py").read())

file = pd.read_csv("credentials.csv")
headerList = ['Email_ID','Password']
file.to_csv("credentials.csv", header=headerList, index=False)

while 1:
    ch = int(input("Enter your choice: "))
    if ch==1:
        Accounts.login()
    elif ch==2:
        Accounts.signup()
    elif ch==3:
        Accounts.reset()
    elif ch==4:
        exit()
    else:
        print("Wrong Choice")