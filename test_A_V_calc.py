'''
TPRG 2131 Fall 2023 Assignment 1
Sept, 2023
Phil J <philip.jarvis@durhamcollege>
Submitted by: AMANDEEP SINGH (100893335)

This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

import A_V_calc

def test_calculate_area_rectangle():
    assert A_V_calc.calculate_area_rectangle(5, 5)[0] == 25.0
    assert A_V_calc.calculate_area_rectangle(5, 7)[0] == 35.0
    
def test_calculate_area_square():
    assert A_V_calc.calculate_area_square(4)[0] == 16.0
    assert A_V_calc.calculate_area_square(6)[0] == 36.0

def test_calculate_volume_cube():
    assert A_V_calc.calculate_volume_cube(2)[0] == 8.0
    assert A_V_calc.calculate_volume_cube(5)[0] == 125.0

def test_calculate_area_triangle():
    assert A_V_calc.calculate_area_triangle(6, 4)[0] == 12.0
    assert A_V_calc.calculate_area_triangle(8, 10)[0] == 40.0

def test_calculate_area_parallelogram():
    assert A_V_calc.calculate_area_parallelogram(7, 5)[0] == 35.0
    assert A_V_calc.calculate_area_parallelogram(12, 8)[0] == 96.0
