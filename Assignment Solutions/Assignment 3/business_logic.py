import database

def add_player(playerID,name, wins, losses, ties):
    database.insert_player(playerID,name, wins, losses, ties)

def delete_player(name):
    database.delete_player(name)

def get_all_players():
    return database.get_all_players()
