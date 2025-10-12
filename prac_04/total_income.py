"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_months = int(input("How many months? "))
    incomes = get_income_information(incomes, numbers_of_months)
    print_results(incomes, numbers_of_months)

def get_income_information(incomes, numbers_of_months):
    for month in range(1, numbers_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    return incomes

def print_results(incomes, numbers_of_months):
    for number in range(numbers_of_months):
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".
              format(number + 1, incomes[number], sum(incomes[0:number+1])))


main()