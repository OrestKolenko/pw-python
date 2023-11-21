def sum_number(digits:str) ->int:
    total = 0
    for digit in digits:
        total += int(digit)
    return total

try:
    number = input('Enter a number: ')
    if number.isdigit():
        result = sum_number(number)
        print(f"suma cyfr liczby {number} wynosi: {result}")
    else:
        print("Please enter digits only")
except ValueError:
     print("Invalid input")








def  bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi
    
def interpret_bmi(bmi_value):
    if bmi_value < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi_value <= 24.9:
        return "Prawidlowa waga"
    elif 25 <= bmi_value <= 29.9:
        return "Nadwaga"
    else:
        return "Otylosc"
    
weight = float(input("Weight:"))
height = float(input("Height:"))

result = bmi_calculator(weight, height)

print("BMI:{:.2f}".format(result))
print("Waga:{}".format(interpret_bmi(result)))







def check_float(number:float) -> bool:
    try: 
        float(number)
        return True
    except ValueError:
        return False
    

def index_mass(mass:float, height:int) -> float:
    bmi = mass/(height**2)
    return index_mass_class(bmi)


def index_mass_class(bmi:float) -> str:
    if bmi <= 18.5:
        return "You are thin"
    elif 18.5 < bmi <= 25:
        return "You have normal weight"
    elif 25 < bmi <= 30:
        return "You are overweight"
    else:
        return "You are obese"

try:
    mass = input("Enter your mass: ")
    height = input("Enter your height: ")
    if check_float(mass) and height.isdigit():
        print(index_mass(float(mass), int(height)))
    else:
        print("Please enter digits only")
except ValueError:
    print("Invalid input")



