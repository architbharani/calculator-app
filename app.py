from calc_func import do_addition, do_subtraction
from area import calculate_area_rectangle   
from multiply import do_multiplication


def main():
    print("Welcome to the app!")
    print(""" Select the function from the given option
          1. Add
          2. Subtract
          3. Multiply
          4.Area
          """)
    user_input= input("Select the function 2")
    
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    
    if user_input == "1":    
        print(do_addition(a,b))
    elif user_input == "2":
        print(do_subtraction(a,b))
    elif user_input=="3":
        print(do_multiplication(a,b))
if __name__=='__main__':
    main()
        
        