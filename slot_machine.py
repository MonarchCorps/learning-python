import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "✨"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("------------")
    print(" | ".join(row))
    print("------------")

def get_payout(row, bet):
    payout_multipliers = {
        "🍒": 3,
        "🍉": 4,
        "🍋": 5,
        "🔔": 6,
        "✨": 7
    }
    if row[0] == row[1] == row[2]:
        return bet * payout_multipliers.get(row[0], 0)
    return 0

def main():
    balance = 100
    
    print("*****************")
    print("Welcome to the Slot Machine Game!")
    print("Symbols: 🍒 🍉 🍋 🔔 ✨")
    print("*****************")
    
    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")
        bet = input("Place your bet: ")
        
        if not bet.isdigit():
            print("Invalid bet. Please enter a valid number.")
            continue
            
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient balance. Please enter a smaller bet.")
            continue
        
        if bet <= 0:
            print("Invalid bet. Please enter a positive number.")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("SPINNING...")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout:.2f}!")
        else:
            print("You lost!")
        
        balance += payout
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again == "y":
            break
        
    print(f"Thank you for playing! Your final balance is ${balance:.2f}")

if __name__ == "__main__":
    main()