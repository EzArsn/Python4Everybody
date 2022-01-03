# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Eg:
    # Enter Hours: 45
    # Enter Rate: 10
    # Pay: 475.0

def main():
    print('Enter Hours worked: ', end='')
    h=float(input())
    print('Enter pay rate: ',end='')
    p=float(input())
    if h>40:
        w=40*p+(h-40)*1.5*p
    else:
        w=h*p
    print('Pay: ',w)

main()