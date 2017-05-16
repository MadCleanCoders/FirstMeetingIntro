#Example of the O in SOLID principles



#Bad example, Close class
class CarService:

    plates = ""
    # 12-12-2015 - I have to add a new field 'color'
    color = ""
    # 12-1-2016 - I have to add a new field 'wheel_size'
    wheel_size = "17.5"

    def get_plates(self):
        return self.plates

    def set_plates(self, new_plates):
        self.plates = new_plates

    def paint_car(self, new_color):
        self.color = new_color

    def get_wheel_size(self):
        return self.wheel_size




#Cool example, open class
class BasicVehicle:
    plates = ""

    def get_plates(self):
        return self.plates

    def set_plates(self, new_plates):
        self.plates = new_plates


class PaintableCar(BasicVehicle):
    color = ""

    def paint_car(self, new_color):
        self.color = new_color

class SuperCoolCar(PaintableCar):
    wheel_size = "17.5"

    def get_wheel_size(self):
        return self.wheel_size