
def password_check(password):
    l, u, p, d = 0, 0, 0, 0
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    specialchar = "$@_&"
    digits = "0123456789"
    if (len(password) >= 8):
        for i in password:
            if (i in smallalphabets):
                l += 1
            elif (i in capitalalphabets):
                u += 1
            elif (i in digits):
                d += 1
            elif (i in specialchar):
                p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(password)):
        print("Valid Password")
        return True
    else:
        print("Invalid Password")
        return False