started = False

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
            started = False  # Fix: should be False to indicate the car has stopped
            print("Car stopped.")
    elif command == "help":
        print("""
 Start - Start the car
 Stop - Stop the car
 Quit - Terminate """)
    elif command == "quit":
        break
    else:
        print("I do not understand")