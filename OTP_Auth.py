import math
from email.message import EmailMessage
import random
import smtplib


def OTPAUTH(email_id,purpose):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    content = "Use Verification code " + OTP + " for OTPAuth authentication"

    msg = EmailMessage()
    msg.set_content(content)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("otpauthorizationauthentication@gmail.com", "gisjxjowvfpuywlh")
    msg['Subject'] = 'OTP for ' + purpose
    msg['From'] = "otpauthorizationauthentication@gmail.com"
    msg['To'] = email_id
    s.send_message(msg)
    flag = 0
    while flag != 1:
        a = input("Enter Your OTP : ")
        if a == OTP:
            print("Verified")
            flag = 1
        else:
            print("Please Check again and enter your OTP")

    return 1
