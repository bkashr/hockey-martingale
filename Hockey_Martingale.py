import random
# Load spreadsheet
data = pd.read_excel("c:\Users\ryanb\Downloads\Hockey Martingale Stats.xlsx")

def simulate_martingale(
    initial_bet=2.50,
    bankroll=150,
    odds=2.1,  # Approximate parlay odds (+110 converted to decimal)
    probability=0.75,  # Approximate success rate for the parlay
    max_iterations=100
):
    bet = initial_bet
    current_bankroll = bankroll
    results = []

    for _ in range(max_iterations):
        # Simulate the outcome of the parlay (win or lose)
        outcome = random.random() < probability
        
        if outcome:  # Parlay wins
            winnings = bet * (odds - 1)
            current_bankroll += winnings
            bet = initial_bet  # Reset bet to initial size
        else:  # Parlay loses
            current_bankroll -= bet
            bet *= 2  # Double the bet for the next round

            # Stop if bankroll is insufficient for the next bet
            if bet > current_bankroll:
                results.append(current_bankroll)
                break
        
        results.append(current_bankroll)
        
        # Stop if bankroll is depleted
        if current_bankroll <= 0:
            break

    return results

# Run simulation
simulated_results = simulate_martingale()
print(simulated_results)
