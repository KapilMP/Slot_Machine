import random


MAX_LINES = 3
MIN_AMOUNT = 1
MAX_AMOUNT = 100

ROWS = 3
COLUMNS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_values ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        #check is done base on column
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
                # if you break the else statement doesn't run
        else:
            winnings = values[symbol] * bet
            winnings_lines.append(line + 1)
        return winnings, winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    # Select symbol base on count and append to all_symbols
    # for example a goes to all_symbols twice
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

     # What value will go in every single columns
    # columns = [[],[],[]] inside the inner list what value will go
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    #transposing: Visually appealing
    for row in range(len(columns[0])): #run the loops base on the number of columns
        for i, column in enumerate(columns): #col1[0], col2[0], col3[0]
            if i != len(column) - 1:
                print(column[row], end="|") # at the end print | instead of next line
            else:
                print(column[row], end= "") #after column number ends print nothing
        print() #after firs inner loops end go to next line



def deposit():
    while True:
        amount = input("What would you like to deposit: ")
        if amount.isdigit(): # To check user input valid number
            amount = int(amount) #converting to integer
            if amount > 0: # If amount is valid break the loop
                break
            #else keep asking
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please enter a number")

    return amount
def get_number_of_lines():

    while True:
        lines = input("Enter a number of line (1 - "+ str(MAX_LINES) + ") ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter between 1 and {MAX_LINES}")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter your bet between {MIN_AMOUNT} and {MAX_AMOUNT}:  ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_AMOUNT <= bet <= MAX_AMOUNT:
                break
            else:
                print(f"Please enter between {MIN_AMOUNT} and {MAX_AMOUNT}")
        else:
            print("Please enter a number")
    return bet

def spin(balance):
    if balance <= 0:
        print("You don't have enough funds to play!")
        return balance
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You dont have sufficient fund. Your balance is {balance} ")
            continue
        else:
            break
    balance -= total_bet
    print(f"You deposit {balance} on line {lines}. Remaining balance: {balance}")

    # Spin the slot machine
    slot = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slot)

    winnings, winnings_line = check_winnings(slot, lines, bet, symbol_values)
    print(f"You won {winnings}")
    if winnings_line:
        print(f"You won on lines:", *winnings_line)
    else:
        print("No winning lines.")

    balance += winnings
    return balance

def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance  = spin(balance)

    print(f"You left with a balance of {balance}. Thanks for playing!")

main()


