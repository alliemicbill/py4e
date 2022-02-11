# exercise3-2.py
# Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program
try:
    hours = input('Enter Hours: ')
    hr = float(hours)
    rate = input('Enter pay rate: ')
    pr = float(rate)
    ot = 0
    pay = 0

    if hr > 40:
        ot = (hr - 40)*(1.5 * pr)
        pay = 40*pr + ot
    else:
        pay = hr * pr
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
