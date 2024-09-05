def create_calculator():
    return {
        "current_value": "0",          # Current value displayed on the calculator
        "expression": "",              # Mathematical expression being built
        "clear_on_next_input": False,  # Flag -- determines if next input should clear the display
        "last_operator": None,         # Tracks the last operator entered (e.g., +, -, *, /)
        "operations": {                # Mapping of input keys to their corresponding functions
            '+': add_operator,
            '-': add_operator,
            '*': add_operator,
            '/': add_operator,
            '%': percentage,
            '!': negate,
            '=': calculate,
            'c': clear
        }
    }

# Retrieves the value to be displayed on the calculator.
def get_display(calculator):
    return calculator["current_value"] # Returns the current display val

# Processes a single key input (digit, operator) and updates the calculator's state
def input_key(calculator, key: str):
    if key.isdigit():
        add_digit(calculator, key)  # Process digit inputs
    elif key in calculator["operations"]:
        calculator["operations"][key](calculator, key)  # Process operator inputs

# Adds digit to the current display value or starts a new number if needed.
def add_digit(calculator, digit: str):
    if calculator["clear_on_next_input"] or calculator["current_value"] == "0":
        calculator["current_value"] = digit  # Start a new number
        calculator["clear_on_next_input"] = False  # Reset the clear flag
    else:
        calculator["current_value"] += digit  # Append digit to the current number

# Resets display to "0" and clears the last operator.
def clear(calculator, _=None):
    calculator["current_value"] = "0"  # Reset display to "0"
    calculator["expression"] = ""      # Clear the expression
    calculator["last_operator"] = None  # Clear the last operator

def percentage(calculator, _=None):
    #2% assume there is a curr value already
    currVal = calculator["current_value"]
    newVal = float(currVal)/100
    calculator["current_value"] = str(newVal)

#  Toggles sign of the current display value between positive and negative.
def negate(calculator, _=None):
    if calculator["current_value"].startswith('-'):
        calculator["current_value"] = calculator["current_value"][1:]  # Remove '-' sign
    elif calculator["current_value"] != "0":
        calculator["current_value"] = '-' + calculator["current_value"] # Add '-' sign
    #calculator["expression"] = calculator["current_value"]

# Stores the last entered operator and prepares for the next operand input.
# If an operator is entered after a number, the expression will be calculated and the result will be used for the next operation.
def add_operator(calculator, operator: str):
    if calculator["last_operator"] and not calculator["clear_on_next_input"]:
        calculate(calculator)  # Evaluate before adding a new operator
    calculator["expression"] += calculator["current_value"] + operator  # Append operator to the expression
    calculator["clear_on_next_input"] = True  # Clear display on the next input
    calculator["last_operator"] = operator  # Store last operator

# Evaluates the current mathematical expression and updates the display.
def calculate(calculator, _=None):
    try:
        # Complete the expression with the current value
        calculator["expression"] += calculator["current_value"]
        # Evaluate the full expression and convert it to a string
        result = str(eval(calculator["expression"]))
        calculator["current_value"] = result  # Update display with the result
        calculator["clear_on_next_input"] = True  # Prepare to clear on next input
        calculator["expression"] = ""  # Clear the expression for next use
        calculator["last_operator"] = None  # Reset last operator
    except Exception:
        calculator["current_value"] = "Error"
    #except ZeroDivisionError"
