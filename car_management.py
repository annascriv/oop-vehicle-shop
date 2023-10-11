class CarManager:
    all_cars={}
    total_cars=0

    def __init__(self,id, make, model, year ):
        self._id = id
        self._make=make
        self._model=model
        self._year=year
        self._mileage=0
        self._services=[]
        CarManager.total_cars+=1
        CarManager.all_cars[self._id]=self

    def __repr__(self):
        return f"{self._id} | {self._make} | {self._model} | {self._year} | {self._mileage} | {self._services}"    

    @property
    def get_id(self):
        return self._id

    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id=new_id

    @property
    def get_make(self):
        return self._make

    @get_make.setter
    def set_make(self, new_make):
        if type(new_make)==str:
            self._make=new_make

    @property
    def get_model(self):
        return self._model

    @get_model.setter
    def set_model(self, new_model):
        if isinstance(new_model,str):
            self._model=new_model

    @property
    def get_year(self):
        return self._year

    @get_year.setter
    def set_year(self, new_year):
        if isinstance(new_year,int) and new_year>1900:
            self._year=new_year

    def add_mileage(self, mileage):
        if isinstance(mileage, int) and mileage>0:
            self._mileage=mileage

    def add_services(self, services):
        if isinstance(services, str):
            self._services.append(services)


def prompt():
    choice = input("""
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
""")
    
    match choice:
        
        case '1':
            id = CarManager.total_cars
            make = input("Enter the car's make:")
            model = input("Enter the car's model:")
            year = input("Enter the car's year:")

            new_car = CarManager(id,make,model,year)
            #CarManager.all_cars

        case '2':
            print(CarManager.all_cars)

        case '3':
            print(CarManager.total_cars)

        case '4':
            id_of_car = int(input("Please enter the car's id':"))

            for car in CarManager.all_cars:
                if car == id_of_car:
                    user_car = CarManager.all_cars[car]
                    print(user_car)

        case '5':
            new_service = input("Enter the service for the car:")

            CarManager.add_services(new_service)

        case '6':
            new_mileage = int(input("Enter the mileage you need to add: "))

            CarManager.add_mileage(new_mileage)

        case '7':
            prompt()


prompt()













car_one = CarManager(1, "Ford", "Escort", 2001)


print(car_one)
