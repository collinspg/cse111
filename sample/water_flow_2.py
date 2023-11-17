## I exceeded the requirements by adding a function that computes and return the calculated value of psi conversion from kpa
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

# This function  calculates the water pressure lost because of fittings such 
# as 45° and 90° bends that are in a pipeline. 
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2  # density of water in kilogram/meter^3
    pressure_loss = (-0.04 * density_water * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss

# This function calculates and returns the Reynolds number for a pipe with water 
# flowing through it.
def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_water = 998.2  # density of water in kilogram/meter^3
    dynamic_viscosity = 0.0010016  # dynamic viscosity of water in Pascal seconds
    reynolds_number = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds_number

# This function calculates  calculates the water pressure lost because of water
# moving from a pipe with a large diameter into a pipe with a smaller diameter. 
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_water = 998.2  # density of water in kilogram/meter^3
    k_constant = ( 0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = (-k_constant * density_water * fluid_velocity**2) / 2000
    return pressure_loss

##Exceeding requirements codes.
# This function converts kilopascals (kPa) to pounds per square inch (psi)
def kpa_to_psi(kpa):
    psi = kpa * 0.145038
    return round(psi, 2)


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure_kpa = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure_kpa += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure_kpa += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure_kpa += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure_kpa += loss
    
    ##Exceeding requirements codes
    # Convert pressure from kPa to psi
    pressure_psi = kpa_to_psi(pressure_kpa)

    print(f"Pressure at house: {pressure_kpa:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} pounds per square inch(psi)")


if __name__ == "__main__":
    main()