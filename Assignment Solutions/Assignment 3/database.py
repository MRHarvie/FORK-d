import sqlite3

def create_table():
    conn = sqlite3.connect("player_db.sqlite")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Player (
                        playerID INT PRIMARY KEY,
                        name TEXT,
                        wins INTEGER,
                        losses INTEGER,
                        ties INTEGER,
                        total_games INTEGER
                    )''')
    conn.commit()
    conn.close()

def insert_player(playerID, name, wins, losses, ties):
    conn = sqlite3.connect("player_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Player VALUES (?, ?, ?, ?, ?)",
                   (playerID, name, wins, losses, ties))

    conn.commit()
    conn.close()

def delete_player(name):
    conn = sqlite3.connect("player_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Player WHERE name=?", (name,))

    conn.commit()
    conn.close()

def get_all_players():
    conn = sqlite3.connect("player_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Player")
    players = cursor.fetchall()

    conn.close()
    return players

if __name__ == "__main__":
    create_table()
