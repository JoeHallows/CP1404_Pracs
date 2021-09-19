
from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("{} ({}) : ${:,.2f} Added".format(new_guitar.name, new_guitar.year, new_guitar.cost))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    for i, guitar in enumerate(guitars):
        yes_or_no_vintage = ""
        if guitar.is_vintage():
            yes_or_no_vintage = "(Vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {yes_or_no_vintage}")


main()

