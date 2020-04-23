from src.Plane import Plane


def main():
    Boeing = Plane("Boeing", 50000, 150, "USA", 100000000, 1999)
    Mriya = Plane("Mriya", 45500, "Ukraine")
    Airbus = Plane()
    plane = [Boeing, Mriya, Airbus]
    [print(count_of_object) for count_of_object in plane]


if __name__ =="__main__":
    main()