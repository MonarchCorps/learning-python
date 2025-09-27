class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"Driving {self.model}")

    def stop(self):
        print(f"Stopping {self.model}")

    def park(self):
        print(f"Parking {self.model}")

    def sell(self):
        print(f"Selling {self.model}")