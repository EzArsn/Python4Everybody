# Exercise 6: Rewrite your pay computation with time-and-a-half for over-
# time and create a function called computepay which takes two parameters
# (hours and rate).
#Eg:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def main():
    print('Enter Hours worked: ', end='')
    h=float(input())
    print('Enter pay rate: ',end='')
    p=float(input())
    def computepay(a,b):
        if a>40:
            w=40*b+(a-40)*1.5*b
        else:
            w=a*b
        print('Pay: ',w)
    computepay(h,p)

main()