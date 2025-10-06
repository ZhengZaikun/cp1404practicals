
def main():
    """By entering the score and selecting different options, you can re-enter the score, determine the grade and print the star function"""
    fraction = int(input("Enter score: "))
    fraction = determine_score(fraction)
    options = input("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>>").upper()
    while options != "Q":
        if options == "G":
            fraction = int(input("Enter score: "))
            fraction = determine_score(fraction)
        elif options == "P":
            result = determine_fraction(fraction)
            print(f"your result: {result}")
        elif options == "S":
            print("*" * fraction)
        else:
            print("Invalid option")
        options = input("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>>").upper()

def determine_score(score):
    """Determine the score and return a score"""
    while score > 100 or score < 0:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_fraction(fraction):
    """Determine the score and return a grade"""
    # from score import determine_score
    # result = determine_score(fraction)
    # return result
    if fraction >= 90:
        result = "Excellent"
    elif fraction >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result
main()


