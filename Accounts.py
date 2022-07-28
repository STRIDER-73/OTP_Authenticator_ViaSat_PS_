import hashlib
import csv
import os
import stdiomask
import Password_Validity
import pandas as pd
import OTP_Auth


def signup():
    email = input("Enter email address: ")
    msg = """Please ensure that the Password has the following combination
              Minimum 8 characters.
              The alphabet must be between [a-z]
              At least one alphabet should be of Upper Case [A-Z]
              At least 1 number or digit between [0-9].
              At least 1 character from [ _ or @ or $ or &]. 
        """
    print(msg)
    pwd = stdiomask.getpass()
    while 1:
        if Password_Validity.password_check(pwd):
            break
        else:
            pwd = stdiomask.getpass("Enter a valid Password : ")
    conf_pwd = stdiomask.getpass("Confirm Password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        # open the file in the write mode
        hash1 = hashlib.md5(enc).hexdigest()
        with open('credentials.csv', 'a', encoding='UTF8') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a row to the csv file
            data = [email, hash1]
            writer.writerow(data)
            f.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have registered successfully!")
        exec(open("MainDriver.py").read())
    else:
        print("Password is not same as above! \n")


def login():
    email = input("Enter email: ")
    filename = 'credentials.csv'
    df = pd.read_csv(filename)
    flag=0
    for i in range(len(df.Email_ID)):
        if email == df.Email_ID[i]:
            index = i
            flag = 1
    if flag == 0:
        print(" Email not present in the Database, Create a new account \n")
        exec(open("MainDriver.py").read())
    pwd = stdiomask.getpass()
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    file = pd.read_csv("credentials.csv")
    headerList = ['Email_ID','Password']
    file.to_csv("credentials.csv", header=headerList, index=False)
    df = pd.read_csv('credentials.csv')
    df.to_csv('credentials.csv', index=False)
    csv_file = csv.reader(open('credentials.csv', "r"), delimiter=",")
    for row in csv_file:
        if email == row[0]:
            stored_email = row[0]
            stored_pwd = row[1]
    if email == stored_email and auth_hash == stored_pwd:
        OTP_Auth.OTPAUTH(email,"Logging-in")
        print("Logged in Successfully!")
        exit()
    else:
        print("Login failed! The user name or password you entered isn't correct. Try entering it again \n")
        exec(open("Menu.py").read())



def reset():
    email = input("Enter the Email to verify the account : ")
    flag = 0
    filename = 'credentials.csv'
    df = pd.read_csv(filename)
    for i in range(len(df.Email_ID)):
        if email == df.Email_ID[i]:
            index = i
            flag = 1
    if flag == 0:
        print(" Email not present in the Database, Create a new account \n")
        exec(open("MainDriver.py").read())
    print("Account in the Database, OTP sent to verify the Account")
    OTP_Auth.OTPAUTH(email," for Password Reset")
    msg = """Please ensure that the Password has the following combination
              Minimum 8 characters.
              The alphabet must be between [a-z]
              At least one alphabet should be of Upper Case [A-Z]
              At least 1 number or digit between [0-9].
              At least 1 character from [ _ or @ or $ or &]. 
        """
    print(msg)
    pwd = stdiomask.getpass("Enter your new Password: ")
    while 1:
        if Password_Validity.password_check(pwd):
            break
        else:
            pwd = stdiomask.getpass("Enter a valid Password : ")
    conf_pwd = stdiomask.getpass("Confirm Password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        df.at[index, 'Password'] = hash1
        df.to_csv("credentials.csv", encoding='utf-8', index=False)
        print("Password has been changed successfully \n ")
    else:
        print("Password is not matching, try again \n")
    exec(open("MainDriver.py").read())
