class Plane:
    max_height = 10000

    def __init__(self, name=None, tank_volume=None, number_of_passengers=None,
                 country_of_producing=None,
                 price_in_dollars=None, year_of_opening=None):
        self.name = name
        self.tank_volume = tank_volume
        self.number_of_passengers = number_of_passengers
        self.country_of_producing = country_of_producing
        self.price_in_dollars = price_in_dollars
        self.year_of_opening = year_of_opening

    @staticmethod
    def staticmethod():
        return Plane.max_height

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        tank_volume = "Tank_volume: {0}\n".format(self.tank_volume)
        number_of_passengers = "Number_of_passengers: {0}\n".format(self.number_of_passengers)
        country_of_producing = "country_of_producing : {0}\n".format(
            self.country_of_producing)
        price_in_dollars = "Price_in_dollars: {0}\n".format(self.price_in_dollars)
        year_of_opening = "Year of opening: {0}\n".format(self.year_of_opening)
        max_height = "Price in millions of dollars: {0}\n".format(
            Plane.max_height)
        return name + tank_volume + number_of_passengers + country_of_producing + price_in_dollars + \
               year_of_opening + max_height

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_tank_volume(self):
        return self.tank_volume

    def set_tank_volume(self, tank_volume):
        self.tank_volume = tank_volume

    def get_number_of_passengers(self):
        return self.number_of_passengers

    def set_number_of_passengers(self, number_of_passengers):
        self.number_of_passengers = number_of_passengers

    def get_country_of_producing(self):
        return self.country_of_producing

    def get_country_of_producing(self, country_of_producing):
        self.country_of_producing = country_of_producing

    def get_price_in_dollars(self):
        return self.price_in_dollars

    def set_price_in_dollars(self, price_in_dollars):
        self.price_in_dollars = price_in_dollars

    def get_year_of_opening(self):
        return self.year_of_opening

    def set_year_of_opening(self, year_of_opening):
        self.year_of_opening = year_of_opening

    def get_max_height(self):
        return self.max_height

    def set_max_height(self, max_height):
        self.max_height = max_height