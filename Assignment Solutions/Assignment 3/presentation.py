import business_logic

def print_menu():
    print("\nCommand Menu:")
    print("1. View Players")
    print("2. Add Player")
    print("3. Delete Player")
    print("4. Exit")

def view_players():
    players = business_logic.get_all_players()
    if not players:
        print("No players found.")
    else:
        print("\nPlayers:")
        for i, player in enumerate(players,start=1):
            playerID, name, wins, losses, ties = player
            print(f"{i}. {name} {wins} {losses} {ties}")

def add_player():
    playerID = input("Enter player ID number:  ")
    name = input("Enter player's name: ")
    wins = input("Enter number of wins: ")
    losses = input("Enter number of losses: ")
    ties = input("Enter number of ties: ")

    if not (wins.isdigit() and losses.isdigit() and ties.isdigit()):
        print("Wins, losses, and ties must be integers.")
        return

    business_logic.add_player(playerID, name, int(wins), int(losses), int(ties))
    print("Player added successfully.")

def delete_player():
    name = input("Enter player's name to delete: ")
    business_logic.delete_player(name)
    print("Player deleted successfully.")

def main():
    print("Welcome to Player Manager!")

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_players()
        elif choice == "2":
            add_player()
        elif choice == "3":
            delete_player()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
