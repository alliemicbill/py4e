# exercise3-1.py
# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
hours = input('Enter Hours: ')
rate = input('Enter pay rate: ')
ot = 0
pay = 0
if int(hours) > 40:
    ot = (int(hours) - 40)*(1.5 * float(rate))
    pay = 40*float(rate) + ot
else:
    pay = int(hours) * float(rate)
print('Pay:', pay)
