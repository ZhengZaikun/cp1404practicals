from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi('my_taxi', 200, 2)
total_distance = my_taxi.drive(18)
print(my_taxi)
total_price = my_taxi.calculate_total_price()
print(f"Total price: ${total_price}")