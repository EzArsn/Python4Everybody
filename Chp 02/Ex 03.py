# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Eg:
#     Enter Hours: 35
#     Enter Rate: 2.75
#     Pay: 96.25

def main():
    print('Enter working hours: \t')
    h=input()
    print('Enter pay rate: \t')
    r=input()
    h=float(h)
    r=float(r)
    w=h*r
    print('Wage is ',w)
main()