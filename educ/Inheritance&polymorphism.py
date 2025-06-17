class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)


class School(Building):
    studs = 0

    def __init__(self, studs, year, city):
        super(School, self).__init__(year, city)
        self.studs = studs

    def get_info(self):
        super().get_info()
        print("Students:", self.studs)


class House(Building):
    pass


class Shop(Building):
    pass


school = School(150, 2007, "Moscow")
school.get_info()
house = House(2007, "Moscow")
shop = Shop(2007, "Moscow")
