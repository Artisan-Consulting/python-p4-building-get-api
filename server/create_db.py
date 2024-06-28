# create_db.py is a script that creates the database and tables for the server.

from models import Game, Review, User

def create_db():
    Game.create_table()
    Review.create_table()
    User.create_table()

if __name__ == '__main__':
    create_db()
    
