class Flight:
    counter = 1

    def __init__(self, origin, destination, duration):

        # Colocando ID no OBJETO que estamos trabalhando
        self.id = Flight.counter
        # Atualizando o COUNTER na CLASSE Flight
        Flight.counter += 1

        self.passengers = []

        # informações do voo
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"self.origin: {self.origin}")
        print(f"self.destination: {self.destination}")
        print(f"self.duration: {self.duration}")

        print()
        print("Passengers: ")
        for passenger in self.passengers:
            print(f"{passenger.name}")


    def delay(self, atraso):
        self.duration += atraso

    def add_passenger(self, passageiro):
        self.passengers.append(passageiro)
        passageiro.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name



def main():

    f1 = Flight("New York", "London", 540)
    f2 = Flight("New York", "Moscou", 940)

    alice = Passenger("Alice")
    marcos = Passenger("Marcos")

    f1.add_passenger(alice)
    f1.add_passenger(marcos)

    f2.add_passenger(marcos)

    f1.print_info()
    f2.print_info()

if __name__ == "__main__":
    main()
