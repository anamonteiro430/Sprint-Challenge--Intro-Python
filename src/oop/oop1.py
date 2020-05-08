# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle(): #base class
     def __init__(self, color, velocity):
          self.color = color
          self.velocity = velocity
     

class GroundVehicle(Vehicle): ##base class for Car and Motorcycle
     def __init__(self, color, velocity, wheels):
         super().__init__(color, velocity)
         self.wheels = wheels

class FlightVehicle(Vehicle): ##base class for Airplane and Starship
     def __init__(self, color, velocity, seats):
          super().__init__(color, velocity)
          self.seats = seats

class Car(GroundVehicle):
     pass

class Motorcycle(GroundVehicle):
     pass

class Starship(FlightVehicle):
     pass

class Airplane(FlightVehicle):
     pass