from prac_07.guitar import Guitar
def main():
    """Input information for one or more guitars and store it,
    then output detailed information."""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            line = line.strip().split(",")
            guitars.append(Guitar(line[0], int(line[1]), float(line[2])))
        guitars.sort()
    print(guitars)
    print("\n--- Unsorted Guitars ---")
    print_information_of_guitars(guitars)
    guitars = write_guitars(guitars)
    guitars.sort()
    print_information_of_guitars(guitars)
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            guitar = ",".join([guitar.name, str(guitar.year), str(guitar.cost)]) + "\n"
            out_file.writelines(guitar)

def print_information_of_guitars(guitars):
    """Print information about guitars."""
    longest_name = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>{longest_name}} ({guitar.year}), worth ${guitar.cost:.2f} {vintage_string}")

def write_guitars(guitars):
    """Get new guitars from user and return them."""
    name = input("Name: ")
    while name.strip() != "":
        try:
            year = int(input("Year: "))
            cost = round(float(input("Cost: ")),2)
            guitar = [name, year, cost]
            guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
        except ValueError:
            print("Invalid input")
        name = input("Name: ")
    return guitars

main()