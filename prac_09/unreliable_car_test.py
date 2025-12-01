from prac_09.unreliable_car import UnreliableCar
my_unreliable_car = UnreliableCar("Prius 1", 100, 30)
for number in range(100):
    print(f"Number: {number}, Distance: {my_unreliable_car.drive(50)} km")