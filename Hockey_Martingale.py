import random
import pandas as pd

# Read the main CSV file into a DataFrame
file_path_main = 'c:/Users/ryanb/Downloads/Hockey_Stats.csv'
df_main = pd.read_csv(file_path_main)

# Read the betting data CSV file into a DataFrame
file_path_betting = 'c:/Users/ryanb/Downloads/Hockey_Betting_Data.csv'
df_betting = pd.read_csv(file_path_betting)

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

# Analyze betting data
def analyze_betting_data(df_betting):
    # Calculate the average over/under for the first 5 and 10 minutes
    avg_over_5 = df_betting['Over_5'].mean()
    avg_under_5 = df_betting['Under_5'].mean()
    avg_over_10 = df_betting['Over_10'].mean()
    avg_under_10 = df_betting['Under_10'].mean()

    print(f"Average Over 5 minutes: {avg_over_5}")
    print(f"Average Under 5 minutes: {avg_under_5}")
    print(f"Average Over 10 minutes: {avg_over_10}")
    print(f"Average Under 10 minutes: {avg_under_10}")

    # Calculate the success rate of bets
    success_rate_5 = df_betting['Over_5'].sum() / len(df_betting)
    success_rate_10 = df_betting['Over_10'].sum() / len(df_betting)

    print(f"Success rate for Over 5 minutes bets: {success_rate_5}")
    print(f"Success rate for Over 10 minutes bets: {success_rate_10}")

# Run simulation for each team in the main DataFrame
for index, row in df_main.iterrows():
    team = row['Team']
    print(f"Simulating for team: {team}")
    simulated_results = simulate_martingale()
    print(f"Results for {team}: {simulated_results}")

# Run simulation for each entry in the betting DataFrame
for index, row in df_betting.iterrows():
    game = row['Game']
    print(f"Simulating for game: {game}")
    simulated_results = simulate_martingale()
    print(f"Results for {game}: {simulated_results}")

# Analyze betting data
analyze_betting_data(df_betting)