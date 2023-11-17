# This function  calculates and returns the height of a column of 
# water from a tower height and a tank wall height. 
def water_column_height(tower_height, tank_height):
    water_column_height = tower_height + (3 * tank_height) / 4
    return water_column_height

# This function calculates and returns the pressure caused by Earth’s
# gravity pulling on the water stored in an elevated tank
def pressure_gain_from_water_height(height):
    density_water = 998.2  # density of water in kilogram/meter^3
    gravity_acceleration = 9.80665  # acceleration from Earth's gravity in meter/second^2
    pressure = (density_water * gravity_acceleration * height) / 1000  # pressure in kilopascals
    return pressure

# This function calculates and returns the water pressure lost because of 
# the friction between the water and the walls of a pipe that it flows through. 
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2  # density of water in kilogram/meter^3
    pressure_loss = (-friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
    