class Bird:
    color = None
    name = None
    alive = None



    def set_data(self, c, n, al):
        self.color = c
        self.name = n
        self.alive = al

    def get_data(self):
        print(self.color, "Name:", self.name, ". Alive:", self.alive)


first_bird = Bird()
first_bird.set_data("Red", "RHCP", True)
first_bird.get_data()


second_bird = Bird()
second_bird.set_data("Blue", "ACDC", False)

print(first_bird.name)
