started = False
speed = 0

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print("Car already stopped.")
        else:
            started = False
            speed = 0
            print("Car stopped.")
    elif command.startswith("accelerate"):
        try:
            speed_increase = int(command.split()[1])
            if not started:
                print("Start the car first.")
            else:
                speed += speed_increase
                print(f"Car accelerated to {speed} km/h.")
        except IndexError:
            print("Please provide a speed value to accelerate.")
        except ValueError:
            print("Invalid speed value.")
    elif command.startswith("brake"):
        try:
            speed_decrease = int(command.split()[1])
            if not started or speed == 0:
                print("Car is not moving.")
            else:
                speed = max(0, speed - speed_decrease)
                print(f"Car slowed down to {speed} km/h.")
        except IndexError:
            print("Please provide a speed value to brake.")
        except ValueError:
            print("Invalid speed value.")
    elif command == "help":
        print("""
Start - Start the car
Stop - Stop the car
Accelerate <speed> - Increase car speed
Brake <speed> - Decrease car speed
Display - Display car information
Quit - Terminate""")
    elif command == "display":
        print(f"Car status: {'Running' if started else 'Stopped'} | Speed: {speed} km/h")
    elif command == "quit":
        break
    else:
        print("I do not understand.")