# Exercise 4: Assume that we execute the following assignment statements:
# width = 17
# height = 12.0

# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
    # 1. width//2
    # 2. width/2.0
    # 3. height/3
    # 4. 1 + 2 * 5

def main():
    width = 17
    height= 12.0

    a=width//2
    b=width/2
    c=height/3
    d=1+2*5
    print(f'{a}\t {b}\t {c}\t {d}')
main()