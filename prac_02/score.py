"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    """Print grades by entering them"""
    score = float(input("Enter score: "))
    if score >= 0 or score <= 100:
        grade = determine_score(score)
        print(f"Your score is: {grade}")
    else:
        print("Invalid score")

def determine_score(score):
    """determine grade of score"""
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()