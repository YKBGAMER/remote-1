
import random
cars = ["Toyota", "Ford", "Honda", "Chevrolet", "Mercedes-Benz", "BMW", "Audi", "Tesla"]

selected_brand = random.choice(cars)

print(selected_brand)

def modelYear():
    year = ['2001', '2002', '2003', '2012', '2015', '2018', '2022', '2024']

    select_year = random.choice(year)
    
    print(select_year)

modelYear()
