# BASIC OTP AUTHENTICATION USING PYTHON

## Problem Statement :
OTP Verification is the process of verifying a user by sending a unique password so
that the user can be verified before completing a registration or payment process.
Most of the time, we get an OTP when we make an online payment, or when we forget
our password, or when creating an account on any online platform. Thus, the
sole purpose of an OTP is to verify the identity of a user by sending a unique password.
Create an application for the task of OTP verification using Python.
You can write a program to send emails with OTP as message, then verify it with the user input!

### Approach
The goal was to create an OTP authenticator by using python.
I basically approached from bottom and worked my way up.
Basically sending the email through the terminal was priority. I used SMTP protocol, where Python provides 
smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with 
an SMTP or ESMTP listener daemon. 
Then generating an OTP by using random and sending that using smtplib module.
Logics for OTP verification, then Account creation, implementing 2FA by asking the user to sign-up with a password.
The Email-IDs and the passwords are stored in a CSV file, and the password are hashed using MD5.
The CSV file is maintained and run through using the package pandas.

### Script Files

#### 1. Accounts.py
Has the functions such as ```signup()```,```reset()```,```login()```, which further uses the functions from the various other scripts.

#### 2. MainDriver.py
Driver of this terminal driven app, self-explanatory.

#### 3. Menu.py

#### 4.OTP_Auth.py
OTP generation and verification, the soul of this app, has the function ```OTPAUTH(email_id,purpose)```.


#### 5. Password_Validity.py
Checks if the password passes various required conditions, has the function ```password_check(password)```.

### Database

The Usernames and Passwords are stored and managed in a CSV file ```credentials.csv```. The passwords are hashed using MD5 and
the CSV file is maintained and run through using the package pandas.

### Run
Running the MainDriver will be sufficient, creating the csv file ```credentials.csv``` is advised before executing the scripts.