'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>
Submitted by: AMANDEEP SINGH (100893335)
Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
import math

# Formulas for area calculations

# Area of rectangle
def calculate_area_rectangle(length, width):
    "Calculate the area of a rectangle."
    return length * width, f"{length} * {width}"

# Area of square
def calculate_area_square(side):
    "Calculate the area of a square."
    return side * side, f"{side} * {side}"

# Volume of cube
def calculate_volume_cube(side):
    "Calculate the volume of a cube."
    return side**3, f"{side}**3"

# Area of triangle
def calculate_area_triangle(base, height):
    "Calculate the area of a triangle."
    return 1/2 * base * height, f"1/2 * {base} * {height}"

# Area of parallelogram
def calculate_area_parallelogram(base, height):
    "Calculate the area of a parallelogram."
    return base * height, f"{base} * {height}"

def main():
    "Main function to run the calculator."
    view_mode = 'default'

    while True:
        print("*********")
        print("A/V calculator")
        print("(Level 0)")
        print("Enter Q/q to quit")
        print("Enter V/v to change the calculated view or D/d for default view.")
        print("(Level 1)")
        print("Calculate Area/Volume")
        print("1. Area of rectangle calculation ")
        print("2. Area of square calculation ")
        print("3. Volume of cube calculation ")
        print("4. Area of triangle calculation ")
        print("5. Area of parallelogram calculation ")

        choice = input("Enter your choice: ")
        if choice == 'q':
            break
        elif choice == 'v':
            view_mode = 'equation'
        elif choice == 'd':
            view_mode = 'default'

        elif choice in ['1', '2', '3', '4', '5']:
            if choice == '1':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area, equation = calculate_area_rectangle(length, width)
            elif choice == '2':
                side = float(input("Enter side length: "))
                area, equation = calculate_area_square(side)
            elif choice == '3':
                side = float(input("Enter side length: "))
                volume, equation = calculate_volume_cube(side)
                print(f"Volume: {volume} (Equation: {equation})")
                continue
            elif choice == '4':
                base = float(input("Enter base length: "))
                height = float(input("Enter height: "))
                area, equation = calculate_area_triangle(base, height)
            elif choice == '5':
                base = float(input("Enter base length: "))
                height = float(input("Enter height: "))
                area, equation = calculate_area_parallelogram(base, height)

            if view_mode == 'equation':
                print(f"Area: {area} (Equation: {equation})")
            else:
                print(f"Area: {area}")
                
        else:
            print("Invalid choice, please Try Again!")
            continue

if __name__ == "__main__":
    main()
