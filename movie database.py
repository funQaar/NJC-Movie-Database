import sqlite3

class Movie:
    """A sample Movie class"""

    def __init__(self, movie, actor, actress, year):
        self.movie = movie
        self.actor = actor
        self.actress = actress
        self.year = year

    def __repr__(self):
        return "Movie('{}','{}', '{}', {})".format(self.movie, self.actor, self.actress, self.year)

    
# Defining Connection and Cursor
# Creates new database if not exist

conn = sqlite3.connect('demo.db')  #can also use :memory: to create db in RAM so that it can refresh itself and clear memory on every re-run.
c = conn.cursor()

#creating table
c.execute("""CREATE TABLE IF NOT EXISTS movies(
            movie text,
            actor text,
            actress text,
            year integer
            )""")
# adding movie data function

def add_mov(mov):
    c.execute("INSERT INTO movies VALUES (:movie, :actor, :actress, :year)", {'movie': mov.movie, 'actor': mov.actor, 'actress': mov.actress, 'year': mov.year})


def retrieve_movie_data():
    c.execute("SELECT * FROM movies")
    print(c.fetchall())

def get_actor_data(act):
    c.execute("SELECT * FROM movies WHERE actor=:actor", {'actor': act})
    print(c.fetchall())


#main

mov_1 = Movie('A','John', 'Diana', 1996)
mov_2 = Movie('B','Jane', 'Dru', 2000)

add_mov(mov_1)

add_mov(mov_2)

retrieve_movie_data()

get_actor_data('Jane')


conn.close()
