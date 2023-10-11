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

    @classmethod
    def add_a_car(cls):
        id = max(CarManager.all_cars.keys()) if CarManager.all_cars.keys() else 1
        make = input("Enter the car's make:")
        model = input("Enter the car's model:")
        year = input("Enter the car's year:")   
        cls(id,make,model,year)    
        print(cls.all_cars)
        print("Car added successfully!")
        return prompt()


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
            CarManager.add_a_car()    

        case '2':
            for car in CarManager.all_cars.values():
                print(f"{car.get_year} {car.get_make} {car.get_model}")
            return prompt()
    
        case '3':
            print(f"Total Cars: {CarManager.total_cars}")
            return prompt()

        case '4':
            id_of_car = int(input("Please enter the car's id':"))
            print(CarManager.all_cars.get(id_of_car))

            # for car in CarManager.all_cars:
            #     if car == id_of_car:
            #         user_car = CarManager.all_cars[car]
            #         print(user_car)

        case '5':
            car_id = int(input("Enter the car's id: "))
            car = CarManager.all_cars.get(car_id)
            new_service = input("Enter the service for the car:")
            car.add_services = new_service
            return prompt()


        case '6':
            car_id = int(input("Enter the car's id: "))
            
            car = CarManager.all_cars.get(car_id)
            new_mileage = int(input("Enter the mileage you need to add: "))

            car.set_mileage = new_mileage
            return prompt()

        case '7':
            print("Thank you, please come again!")
            exit()


prompt()













car_one = CarManager(1, "Ford", "Escort", 2001)
car_two = CarManager(2,"Mazda", "Tribute", 2006)
car_three = CarManager(3, "Nissan", "Versa Note", 2016)

print(CarManager.all_cars)


#print(car_one)
