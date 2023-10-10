class CarManager:
    all_cars = {}
    total_cars = 0

    def __init__(self, id, make, model, year, mileage, services):
        self._id = id  # (instance attribute): An integer that should never be repeated and only rise with each car instance
        self._make = (
            make  # (instance attribute): A string representing the make of the car.
        )
        self._model = (
            model  # (instance attribute): A string representing the model of the car.
        )
        self._year = year  # (instance attribute): An integer representing the manufacturing year of the car.
        self._mileage = mileage  # (instance attribute): An integer representing the vehicles total mileage
        self._services = services  # (instance attribute): A list that will store the services done to the car.

    @property
    def get_id(self):
        return self._id

    @property
    def get_make(self):
        return self._make

    @property
    def get_model(self):
        return self._model

    @property
    def get_year(self):
        return self._year

    @property
    def get_mileage(self):
        return self._mileage

    @get_mileage.setter
    def set_mileage(self, mileage):
        self._mileage = mileage

    @property
    def get_services(self):
        return self._services

    @get_services.setter
    def set_services(self, service):
        self._services.append(service)


def term():
    running = True
    while running == True:
        selection = input(
            "----  WELCOME  ----\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n7. Quit\n\n"
        )
        match selection:
            case "1":
                CarManager.total_cars += 1
                id = str(CarManager.total_cars)
                make = input("Enter a make:")
                model = input("Enter a model:")
                year = input("Enter a year:")
                mileage = input("Enter a mileage:")
                services = []
                new_car = CarManager(id, make, model, year, mileage, services)
                CarManager.all_cars[id] = new_car
                print("New car created!\n")
            case "2":
                for car in CarManager.all_cars:
                    print(f"Car {car}: {CarManager.all_cars[car].__dict__}\n")
            case "3":
                print(f"{CarManager.total_cars}\n")
            case "4":
                id_selection = input(
                    "Enter the ID of the car you want to see the details for: "
                )
                car_details = CarManager.all_cars[id_selection].__dict__
                for key, value in car_details.items():
                    print(f"{key}: {value}")
            case "5":  # Modify this to use setters
                id_selection = input("Enter the id of the car you want to service: \n")
                servicing = True
                while servicing:
                    service = input(
                        "Enter the type of service you would like to perform, or q to quit:"
                    )
                    match service:
                        case "q":
                            servicing = False
                        case _:
                            CarManager.all_cars[
                                id_selection
                            ].set_services = service  # Notice how you don't call the setter as it's not a regular method, you assign it a value and the decorator does the rest
                            print(f"{service.title()} performed on Car {id_selection}")
            case "6":
                id_selection = input(
                    "Enter the ID of the car you want to update the mileage for: "
                )
                new_mileage = input("Enter the new mileage:")
                CarManager.all_cars[id_selection].set_mileage = int(new_mileage)
                print(f"Mileage updated for car {id_selection}")
            case "7":
                running = False
            case _:
                print("Please input a selection\n")


term()
