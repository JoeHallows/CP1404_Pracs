
from prac_06.guitar import Guitar


def test_guitars():
    name = "Fender"
    year = 1924
    cost = 16425.00

    guitar = Guitar(name, year, cost)

    print("{} is the name, age is 97, got age {}".format(guitar.name, guitar.get_age()))
    print("{} is the name, vintage is True, got vintage as {}".format(guitar.name, guitar.is_vintage()))


if __name__ == '__main__':
    test_guitars()

