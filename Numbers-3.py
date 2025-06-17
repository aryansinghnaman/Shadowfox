def calculate_speed(distance_m, time_min):
    time_sec = time_min * 60
    speed = distance_m / time_sec
    print("Speed (m/s):", int(speed))

# Call the function with 490 meters and 7 minutes
calculate_speed(490, 7)
