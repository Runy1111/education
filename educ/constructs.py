class Bird:
    color = None
    name = None
    alive = None

    def __init__(self, c=None, n=None, al=None):
        self.set_data(c, n,al)

        self.get_data()

    def set_data(self, c, n, al=None):
        self.color = c
        self.name = n
        self.alive = al

    def get_data(self):
        print(self.color, "Name:", self.name, ". Alive:", self.alive)


first_bird = Bird("Red", "RHCP", True)
first_bird.set_data("Green", "ABBA")
first_bird.get_data()

second_bird = Bird("Blue", "ACDC", False)
