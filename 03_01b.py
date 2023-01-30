from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_cap >= num_packages

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver", ['name', 'car_type', 'car_cap'])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    Iris = Driver('Iris', 'Prius', 7)
    Mickie = Driver('Mickie', 'Tucson', 15)
    Witty = Driver('Witty', 'Hummer', 26)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(Iris, 20))
    return

if __name__ == "__main__":
    main()