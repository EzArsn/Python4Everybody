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