import math

# calc_fuel requires an int
def calc_fuel(mass: int) -> int:
    # Calculate the fuel needed for given mass
    fuel_need = math.floor(mass/3)-2

    # If the fuel needed is a positive, calculate
    # the fuel needed for the fuel's mass
    if fuel_need > 0:
        return fuel_need + calc_fuel(fuel_need)
    else:
        return 0

f = open("input.txt", "r")
o = 0
for line in f:
    o = o + calc_fuel(int(line))

print(o)


