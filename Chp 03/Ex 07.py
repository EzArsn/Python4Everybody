# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# Eg:
#     Enter score: 0.95
#     A
#     Enter score: perfect
#     Bad score
#     Enter score: 10.0
#     Bad score
#     Enter score: 0.75
#     C
#     Enter score: 0.5
#     F
# Run the program repeatedly to test the various different values for input.

def main():
    s=input('Enter score: ')
    def computegrade(sc):
        try:
            sc=float(sc)
            if sc>1.0:
                return "Bad score"
            elif sc>=0.9:
                return "A"
            elif sc>=0.8:
                return "B"
            elif sc>=0.7:
                return "C"
            elif sc>=0.6:
                return "D"
            else:
                return "F"
        except:
            return "Bad score"
    print(computegrade(s))

main()