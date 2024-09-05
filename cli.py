import calculator

def start():
    # Create a new calculator instance.
    print("test")
    print(eval("3/1.5"))
    calc = calculator.create_calculator()
    
    # Initial display of calculator value
    print(calculator.get_display(calc))
    
    # Loop to process user inputs
    while True:
        # Prompt the user for input
        command = input("> ")
        
        # Process each character in the input string.
        process_input(calc, command)

# Processes user's input command by sending each char to the calculator logic
def process_input(calc, command):
    if command.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        exit()

    for key in command:
        calculator.input_key(calc, key)
    
    # Display updated calculator val after processing the input
    print(calculator.get_display(calc))
