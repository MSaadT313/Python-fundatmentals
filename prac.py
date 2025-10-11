def printtemperature():
    print("Temperature Tracker Menu")
    print("1. Output All Temperatures")
    print("2. Input New Temperature")
    print("3. Print Temperature Statics")

    choice = int(input("Choice: "))

    if choice == 1:
        print("These are all your temperatures:\n")
        with open("temperature.txt", "r") as file:
            data = file.read()
            print(data)

    elif choice == 2:
        with open("temperature.txt", "a") as file:
            temp = input("Enter the temperature: ")
            file.write(temp + "\n")

        with open("temperature.txt", "r") as file:
            content = file.read()
            print("Updated temperatures:\n" + content)
    elif choice == 3:
        with open("temperature.txt", "r") as file:
            # data = file.read()
            #Reads each line,removes spaces/newlines,skips empty ones,and converts to float.
            data = [float(line.strip())for line in file]
            avg = sum(data) / len(data)
            print('The highest temperature is ', max(data))
            print('The lowest temperature is ', min(data))
            print('The average temperature is ', avg)

printtemperature()