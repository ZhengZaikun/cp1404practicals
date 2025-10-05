import random
MIN_PRICE = 1
MAX_PRICE = 100
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
CRITICAL_PROBABILITY = 50
INITIAL_PRICE = 10
FILENAME = "capitalist.txt"
out_file = open(FILENAME, "w")
price = INITIAL_PRICE
print("Starting price: $10")
number_of_days = 1
while price >= MIN_PRICE and price <= MAX_PRICE:
    probability = random.randint(1, 100)
    if probability > CRITICAL_PROBABILITY:
        price = price + random.uniform(0,MAX_INCREASE) * price
    else:
        price = price - random.uniform(0,MAX_DECREASE) * price
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:.2f}  ")
    print(f"${round(price, 2)}", file=out_file)
out_file.close()
