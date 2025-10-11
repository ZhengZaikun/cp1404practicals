"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_months = []
    months = int(input("How many months? "))
    incomes, numbers_of_months = enter_imformation(incomes, months, numbers_of_months)
    print_results(incomes, numbers_of_months, months)

def enter_imformation(incomes, months, numbers_of_months):
    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
        numbers_of_months.append(month)
    return incomes, numbers_of_months

def print_results(incomes, numbers_of_months, months):
    for number in range(months):
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".
              format(numbers_of_months[number], incomes[number], sum(incomes[0:number+1])))


main()