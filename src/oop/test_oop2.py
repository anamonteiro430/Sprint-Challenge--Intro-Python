import unittest
# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels #default

    def __str__(self):
        return f"{self.num_wheels} wheels."
    #drive() method
    def drive(self):
        return f"vroooom"


# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
    def __str__(self):
        return f"{self.num_wheels} wheels."
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        return f"BRAAAP!!"

    

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for i in vehicles:
    print(i.drive())


class Oop2Tests(unittest.TestCase):
  def setUp(self):
    self.ground_vehicle = GroundVehicle()
    self.motorcycle = Motorcycle()

  def test_motorcycle_inheritance(self):
    self.assertTrue(isinstance(self.motorcycle, GroundVehicle))

  def test_ground_vehicle_num_wheels(self):
    self.assertEqual(self.ground_vehicle.num_wheels, 4)

  def test_motocycle_num_wheels(self):
    self.assertEqual(self.motorcycle.num_wheels, 2)

  def test_ground_vehicle_drive(self):
    self.assertEqual(self.ground_vehicle.drive(), "vroooom")

  def test_motorcyle_drive(self):
    self.assertEqual(self.motorcycle.drive(), "BRAAAP!!")


if __name__ == '__main__':
  unittest.main()