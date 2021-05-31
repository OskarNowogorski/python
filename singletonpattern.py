#Every time a change is made in any class, the other classes will also change with it.

# Defining Metaclass
class CarMeta(type):
    _instances = {}

    # Creating the object of the same class instance
    def __call__(obj, *args, **kwargs):
        if obj not in obj._instances:
            instance = super().__call__(*args, **kwargs)
            obj._instances[obj] = instance
        return obj._instances[obj]


class CarModelX(metaclass=CarMeta):
    # The car has and invalid amount of wheels:
    _wheels = 3

    def how_many_wheels(self):
        print(self._wheels, " wheels")


if __name__ == "__main__":
    CarOne = CarModelX()
    CarTwo = CarModelX()
    CarThree = CarModelX()

    # Checking the amount of wheels
    print("Car one has:")
    CarOne.how_many_wheels()

    print("Car two has:")
    CarTwo.how_many_wheels()

    print("Car three has:")
    CarThree.how_many_wheels()

    print("------------------")

    CarOne._wheels = 4

    print("Car one has:")
    CarOne.how_many_wheels()

    print("Car two has:")
    CarTwo.how_many_wheels()

    print("Car three has:")
    CarThree.how_many_wheels()

    # Verifying instances:
    print(id(CarOne), id(CarTwo), id(CarThree))