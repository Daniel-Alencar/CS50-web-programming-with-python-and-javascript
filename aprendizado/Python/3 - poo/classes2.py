class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"self.origin: {self.origin}")
        print(f"self.destination: {self.destination}")
        print(f"self.duration: {self.duration}")

def main():

    f1 = Flight("New York", "London", 540)
    f1.print_info()

    f2 = Flight("New York", "Moscou", 940)
    f2.print_info()

if __name__ == "__main__":
    main()
