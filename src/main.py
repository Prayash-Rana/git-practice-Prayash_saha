
from datetime import datetime
from utils import add, subtract, multiply, divide

name = "Prayash saha"
date = datetime.now().strftime("%Y-%m-%d")

print(f" User name : {name} ")
print(f"Today's date: {date}")

sum_result = add(10, 20)
print(f"sum of 10 and 5 is: {sum_result}")

subtract_result = subtract(10, 5)
print(f"subtract of 10 and 5 is: {subtract_result}")

multiply_result = multiply(10, 5)
print(f"multiply of 10 and 5 is: {multiply_result}")

divide_result = divide(10, 5)
print(f"divide of 10 and 5 is: {divide_result}")




