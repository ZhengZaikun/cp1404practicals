from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive\n>>> "

def main():
    """Run the taxi simulator. Print taxi information by entering options."""
    total_price = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    option = input(MENU).upper()
    while option != "Q":
        if option == "C":
            print_taxis(taxis)
            number = input("Choose taxi: ")
            current_taxi = choose_taxi(number, taxis)
            print(f"Bill to date: ${total_price:.2f}")
        elif option == "D":
            if current_taxi is not None:
                taxis, total_price = drive_taxi(taxis, current_taxi, total_price)
                current_taxi = None
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        option = input(MENU).upper()
    print(f"Bill to date: ${total_price:.2f}")
    print_taxis(taxis)


def choose_taxi(number, taxis):
    """Choose a number of taxi"""
    number = judge_number(number, "Choose taxi: ")
    if number < 0 or number >= len(taxis):
        print("Invalid taxi choice")
    return number



def calculate_price(taxis, number, distance, total_price):
    """Calsulate total price."""
    taxis[number].start_fare()
    distance = judge_number(distance, "Drive how far? ")
    taxis[number].drive(distance)
    is_value = judge_attributes(number, taxis)
    price = taxis[number].get_fare() if not is_value else taxis[number].calculate_total_price()
    print(f"Your Prius trip cost you ${price:.2f}")
    total_price += price
    return taxis, total_price

def judge_number(number, information):
    """Judge whether the number is valid or not."""
    is_value = False
    while not is_value:
        try:
            number = int(number)
            is_value = True
        except ValueError:
            print("Invalid taxi choice")
            number = input(information)
    return number

def print_taxis(taxis):
    """Print information about taxis."""
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def judge_attributes(number, taxis):
    """Determine if this taxi has a starting fare."""
    try:
        taxis_flagfall = taxis[number].flagfall
        is_value = bool(taxis_flagfall)
    except AttributeError:
        is_value = False
    return is_value

def drive_taxi(taxis, current_taxi, total_price):
    """Drive designated taxi"""
    if not (current_taxi < 0 or current_taxi >= len(taxis)):
        distance = input("Drive how far? ")
        taxis, total_price = calculate_price(taxis, current_taxi, distance, total_price)
        print(f"Bill to date: ${total_price:.2f}")
    else:
        print("You need to choose a taxi before you can drive")
    return taxis, total_price

main()