class Vehicle(): #base class
     pass
     

class GroundVehicle(Vehicle): ##base class for Car and Motorcycle
     pass

class FlightVehicle(Vehicle): ##base class for Airplane and Starship
     pass

class Car(GroundVehicle):
     pass

class Motorcycle(GroundVehicle):
     pass

class Starship(FlightVehicle):
     pass

class Airplane(FlightVehicle):
     pass