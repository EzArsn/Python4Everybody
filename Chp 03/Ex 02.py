# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

def main():
    h=input('Enter Hours worked: ')
    try:
        h=float(h)
    except:
        print('Error, please enter numeric input')
        
    p=input('Enter pay rate: ')
    try:
        p=float(p)
    except:
        print('Error, please enter numeric input')
    try:    
        if h>40:
            w=40*p+(h-40)*1.5*p
        else:
            w=h*p
        print('Pay: ',w)
    except:
        print('Kindly restart the program')

main()