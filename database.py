import sqlite3
import os


def connect_database():

    base_directory = os.path.dirname(
        os.path.abspath(__file__)
    )

    database_path = os.path.join(
        base_directory,
        "gopal_multiplex.db"
    )

    connection = sqlite3.connect(database_path)

    return connection

def create_tables():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER PRIMARY KEY,
            movie_name TEXT,
            language TEXT,
            duration TEXT,
            price INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT,
            customer_name TEXT,
            phone TEXT,
            movie_name TEXT,
            language TEXT,
            show_time TEXT,
            seats TEXT,
            total_amount INTEGER,
            payment_type TEXT,
            booking_date TEXT
        )
    """)

    connection.commit()

    connection.close()


def add_movies():

    connection = connect_database()
    cursor = connection.cursor()

    movies = [

        (1, "Vibe", "Hindi", "2h 26m", 250),
        (2, "Daayra", "Hindi", "2h 23m", 280),
        (3, "Om Ka Hari", "Hindi", "2h 01m", 220),
        (4, "Haiwaan", "Hindi", "2h 20m", 250),

        (5, "Secret Soldier", "Telugu", "2h 20m", 250),
        (6, "Good Time", "Telugu", "2h 01m", 220),
        (7, "Pithapuram Lo: Ala Modalaindi",
         "Telugu", "1h 59m", 230),
        (8, "Mahendragiri Varahi",
         "Telugu", "2h 34m", 250),

        (9, "Resident Evil", "English", "1h 30m", 300),
        (10, "The Weight", "English", "1h 52m", 280),
        (11, "The Uprising", "English", "2h 08m", 300),
        (12, "Bad Apples", "English", "1h 18m", 250),

        (13, "BeeP", "Tamil", "2h 02m", 220),
        (14, "Sandakari", "Tamil", "2h 02m", 220),
        (15, "Nalla Padam", "Tamil", "1h 50m", 200),

        (16, "Kirunage", "Kannada", "1h 55m", 220),
        (17, "Mahakavi", "Kannada", "2h 02m", 230),
        (18, "Toss", "Kannada", "2h 22m", 240),

        (19, "Law And Order",
         "Malayalam", "2h 38m", 250)
    ]

    for movie in movies:

        cursor.execute("""
            INSERT OR IGNORE INTO movies
            VALUES (?, ?, ?, ?, ?)
        """, movie)

    connection.commit()

    connection.close()


def save_booking(
        ticket_id,
        customer_name,
        phone,
        movie_name,
        language,
        show_time,
        seats,
        total_amount,
        payment_type,
        booking_date):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bookings
        (
            ticket_id,
            customer_name,
            phone,
            movie_name,
            language,
            show_time,
            seats,
            total_amount,
            payment_type,
            booking_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_id,
        customer_name,
        phone,
        movie_name,
        language,
        show_time,
        seats,
        total_amount,
        payment_type,
        booking_date
    ))

    connection.commit()

    connection.close()
def add_movie(movie_id, movie_name, language, duration, price):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO movies
        (movie_id, movie_name, language, duration, price)
        VALUES (?, ?, ?, ?, ?)
    """, (
        movie_id,
        movie_name,
        language,
        duration,
        price
    ))

    connection.commit()
    connection.close()


def delete_movie(movie_id):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM movies
        WHERE movie_id = ?
    """, (movie_id,))

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted
def get_next_movie_id():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT MAX(movie_id)
        FROM movies
    """)

    result = cursor.fetchone()
    connection.close()

    if result[0] is None:
        return 1

    return result[0] + 1
