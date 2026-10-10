try:
    
    with open("sensor_data.csv","r") as file:

        next(file) # This skips the header line instantly

        highest_temp = 0
        total_temp = 0
        count = 0

        for i in file:

            parts = i.strip().split(",")
            print(parts)
            temperature = float(parts[2])

            # To find the highest temp
            if temperature > highest_temp:

                highest_temp = temperature

            # To find the avg temp
            total_temp += temperature
            count += 1

            # To create Temperature Alert
            if parts[3] == "WARNING" or parts[3] == "CRITICAL":
                print(f"ALERT! Sensor Status is {parts[3]} : {temperature}°C")

        if count > 0:

            avg_temp = total_temp//count # Avg is counted after the for loop
            print("\n =====SENSOR SUMMARY=====")
            print(f"The Highest Temperature is {highest_temp}°C")
            print(f"The Average Temperature is {avg_temp}°C")

except FileNotFoundError:

    print("The filename is not found. \nPlease provide a valid filename")

finally:

    print("These are the contents of sensor_data.csv")