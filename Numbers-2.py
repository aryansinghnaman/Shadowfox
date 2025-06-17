def calculate_water_in_pond(radius):
    pi = 3.14
    water_per_sqm = 1.4

    area = pi * radius ** 2
    total_water = area * water_per_sqm

    print("Total Water in Pond (liters):", int(total_water))

# Call the function with radius = 84
calculate_water_in_pond(84)
