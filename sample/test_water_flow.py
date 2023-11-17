# import form the water_flow program to create test functions, import approx from pytest and also 
#import pytest.
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest

# A test function for the water_column_height function
def test_water_column_height():
    test_cases = [
        (0.0, 0.0),
        (0.0, 10.0),
        (25.0, 0.0),
        (48.3, 12.8)
    ]
    expected_heights = [
        0.0,
        7.5,
        25.0,
        57.9
    ]
    for i, (tower_height, tank_height) in enumerate(test_cases):
        expected_height = expected_heights[i]
        result = water_column_height(tower_height, tank_height)
        assert result == approx(expected_height)
            
# A test function for the pressure_gain_from_water_height function     
def test_pressure_gain_from_water_height():
    test_cases = [
        (0.0, 0.000),
        (30.2, 295.628),
        (50.0, 489.450)
    ]
    approx_absolute_tolerances =[
        0.001,
        0.001,
        0.001
    ]
    for i, (height, expected_pressure) in enumerate(test_cases):
        approx_tolerance = approx_absolute_tolerances[i]
        result = pressure_gain_from_water_height(height)
        assert result == approx(expected_pressure, abs=approx_tolerance)
         
# A test function for the pressure_loss_from_pipe function          
def test_pressure_loss_from_pipe():
    test_cases = [
        (0.048692, 0.00, 0.018, 1.75, 0.000),
        (0.048692, 200.00, 0.000, 1.75, 0.000),
        (0.048692, 200.00, 0.018, 0.00, 0.000),
        (0.048692, 200.00, 0.018, 1.75, -113.008),
        (0.048692, 200.00, 0.018, 1.65, -100.462),
        (0.286870, 1000.00, 0.013, 1.65, -61.576),
        (0.286870, 1800.75, 0.013, 1.65, -110.884)
    ]
    approx_absolute_tolerances = [
        0.001,
        0.001,
        0.001,
        0.001,
        0.001,
        0.001,
        0.001
    ]
    for i, (pipe_diameter, pipe_length, friction_factor, fluid_velocity, expected_pressure_loss) in enumerate(test_cases):
        approx_tolerance = approx_absolute_tolerances[i]
        result = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
        assert result == approx(expected_pressure_loss, abs=approx_tolerance)
        
        
        
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])



    