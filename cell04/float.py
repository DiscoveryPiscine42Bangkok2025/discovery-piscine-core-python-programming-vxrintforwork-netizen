my_num=input("Give me a number:")
try:
    number=float(my_num)
    if number.is_integer():
     print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
   pass