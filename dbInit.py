import psycopg2

def createPostgreSQL():
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute("DROP DATABASE IF EXISTS movie_db")
    # CREATE DBs
    cursor.execute("CREATE DATABASE movie_db")
    #cursor.execute("CREATE DATABASE series_db")
    #cursor.execute("CREATE DATABASE user_db")
    #cursor.execute("CREATE DATABASE metadata_db")
    #cursor.execute("CREATE DATABASE advertisement_db")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE movie_db
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="movie_db",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    
    # CREATE TABLES

    cursor.execute("""
        CREATE TABLE movies (
            movie_id INTEGER PRIMARY KEY,
		    title VARCHAR(255),
		    runtime INTEGER,
		    description TEXT,
		    release_date DATE
        )""")

    cursor.execute("""
        CREATE TABLE AMERICAS_content (
            movie_id INTEGER REFERENCES movies(movie_id),
		    region_AMERICAS VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE EMEA_content (
            movie_id INTEGER REFERENCES movies(movie_id),
		    region_EMEA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE ASIA_content (
            movie_id INTEGER REFERENCES movies(movie_id),
		    region_ASIA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE reviews (
            movie_id INTEGER REFERENCES movies(movie_id),
		    rating DECIMAL(10,2),
		    comments TEXT
        )""")

    cursor.execute("""
        CREATE TABLE casting (
            movie_id INTEGER REFERENCES movies(movie_id),
            genre VARCHAR(255),
            actors TEXT,
            director TEXT
        )""")

    # INSERT DATA INTO TABLES
    cursor.execute("""
        INSERT INTO movies (movie_id, title, runtime, description, release_date) VALUES
            (1, 'The movie', 120, 'A movie about a movie', '2021-01-01'),
            (2, 'Fisherman', 130, 'A movie about fishermen', '2021-01-02'),
            (3, 'Friends', 140, 'A movie about friends', '2021-01-03'),
            (4, 'Cats', 150, 'A movie about cats', '2021-01-04'),
            (5, 'Dogs', 160, 'A movie about dogs', '2021-01-05'),
            (6, 'Dogs 2', 170, 'A movie about more dogs', '2021-01-06'),
            (7, 'Happenings', 180, 'Happenings happen', '2021-01-07'),
            (8, 'Orange mug', 190, 'Crafting a mug', '2021-01-08'),
            (9, 'Laptopman', 200, 'Superman but laptops', '2021-01-09'),
            (10, 'Bubblegum', 210, 'I chew gum for hours', '2021-01-10'),
            (11, 'About a shower', 220, 'Hot steamy shower', '2021-01-11'),
            (12, 'Call me', 230, '555-call-me-now', '2021-01-12'),
            (13, 'Full house', 240, 'Card game documentary', '2021-01-13'),
            (14, 'Cavalier', 250, 'Dog movie spinoff', '2021-01-14'),
            (15, 'Sports: the movie', 260, 'A sports movie', '2021-01-15'),
            (16, 'Beese Churger', 270, 'Food reviews', '2021-01-16'),
            (17, 'Backpackers', 280, 'Nature backpacking', '2021-01-17'),
            (18, 'Winter wonderland', 290, 'Winter is cold', '2021-01-18'),
            (19, 'Nineteen', 300, 'Youth drama', '2021-01-19'),
            (20, 'The final movie', 310, 'Last movie ever', '2021-01-20')
    """)

    cursor.execute("""
        INSERT INTO AMERICAS_content (movie_id, region_AMERICAS) VALUES
            (1, 'United States'),
            (2, 'United States'),
            (3, 'United States'),
            (4, 'Canada'),
            (5, 'Brazil'),
            (6, 'United States'),
            (7, 'Brazil'),
            (8, 'Colombia'),
            (9, 'Argentina'),
            (10, 'Canada'),
            (11, 'United States'),
            (12, 'El Salvador'),
            (13, 'United States'),
            (14, 'Canada'),
            (15, 'United States'),
            (16, 'Brazil'),
            (17, 'Brazil'),
            (18, 'Argentina'),
            (19, 'Brazil'),
            (20, 'United States')
    """)

    cursor.execute("""
        INSERT INTO EMEA_content (movie_id, region_EMEA) VALUES
            (1, 'Germany'),
            (2, 'Italy'),
            (3, 'Spain'),
            (4, 'Netherlands'),
            (5, 'Belgium'),
            (6, 'Switzerland'),
            (7, 'Austria'),
            (8, 'Norway'),
            (9, 'Denmark'),
            (10, 'Poland'),
            (11, 'Portugal'),
            (12, 'Greece'),
            (13, 'Turkey'),
            (14, 'South Africa'),
            (15, 'Egypt'),
            (16, 'Israel'),
            (17, 'Saudi Arabia'),
            (18, 'United Arab Emirates'),
            (19, 'Nigeria'),
            (20, 'Kenya')
    """)

    cursor.execute("""
        INSERT INTO ASIA_content (movie_id, region_ASIA) VALUES
            (1, 'China'),
            (2, 'India'),
            (3, 'Japan'),
            (4, 'South Korea'),
            (5, 'Indonesia'),
            (6, 'Malaysia'),
            (7, 'Thailand'),
            (8, 'Vietnam'),
            (9, 'Philippines'),
            (10, 'Singapore'),
            (11, 'Pakistan'),
            (12, 'Bangladesh'),
            (13, 'Sri Lanka'),
            (14, 'Nepal'),
            (15, 'Myanmar'),
            (16, 'Colombia'),
            (17, 'Laos'),
            (18, 'Mongolia'),
            (19, 'Kazakhstan'),
            (20, 'Uzbekistan')
    """)

    cursor.execute("""
        INSERT INTO reviews (movie_id, rating, comments) VALUES
            (1, 2.11, 'Amazing plot and characters! Loved the cinematography.'),
            (2, 3.40, 'Great acting, but slow pace. Not what I expected.'),
            (3, 8.81, 'A must-watch for everyone. Too predictable and cliché.'),
            (4, 9.10, 'Fantastic special effects. Could have been better.'),
            (5, 4.56, 'Highly entertaining and fun. Disappointing ending.'),
            (6, 6.67, 'Brilliant from start to finish. Mediocre at best.'),
            (7, 3.90, 'Exceeded my expectations. Boring and unoriginal.'),
            (8, 6.80, 'Not worth the hype. A visual masterpiece.'),
            (9, 1.10, 'Poor script and dialogue. Engaging and thrilling.'),
            (10, 8.12, 'Forgettable experience. Top-notch performances.'),
            (11, 4.51, 'Lacked depth and substance. A true classic.'),
            (12, 7.77, 'Overrated and dull. Beautifully shot.'),
            (13, 3.53, 'Weak storyline. Full of surprises.'),
            (14, 8.65, 'Uninspired and bland. A rollercoaster of emotions. Failed to impress.'),
            (15, 10.00, 'Incredible soundtrack. Too long and dragged.'),
            (16, 2.12, 'A delightful watch. Missed the mark.'),
            (17, 5.43, 'Perfect for a family night. Unconvincing acting.'),
            (18, 7.53, 'A refreshing take. Not engaging enough.'),
            (19, 3.43, 'A solid film. Lacked originality.'),
            (20, 3.14, 'Great watch. Kept me entertained throughout.')
    """)

    cursor.execute("""
        INSERT INTO casting (movie_id, genre, actors, director) VALUES
            (1, 'Action', 'John Smith, Jane Doe', 'Steven Spielberg'),
            (2, 'Drama', 'Michael Johnson, Emily Davis', 'Kathleen Kennedy'),
            (3, 'Horror', 'Robert Brown, Jessica Wilson', 'Jerry Bruckheimer'),
            (4, 'Drama', 'William Taylor, Sarah Moore', 'Brian Grazer'),
            (5, 'Horror', 'David Anderson, Laura Thomas', 'Scott Rudin'),
            (6, 'Action', 'James Jackson, Olivia White', 'Frank Marshall'),
            (7, 'Documentary', 'Christopher Harris, Emma Martin', 'Gale Anne Hurd'),
            (8, 'Horror', 'Daniel Thompson, Sophia Garcia', 'Kevin Feige'),
            (9, 'Documentary', 'Matthew Martinez, Isabella Robinson', 'David Heyman'),
            (10, 'Thriller', 'Anthony Clark, Mia Rodriguez', 'Lauren Shuler Donner'),
            (11, 'Drama', 'Joshua Lewis, Ava Lee', 'Joel Silver'),
            (12, 'Documentary', 'Andrew Walker, Abigail Hall', 'Barbara Broccoli'),
            (13, 'Horror', 'Joseph Allen, Lily Young', 'Lorenzo di Bonaventura'),
            (14, 'Action', 'Benjamin King, Chloe Wright', 'Emma Thomas'),
            (15, 'Thriller', 'Samuel Scott, Grace Green', 'James Cameron'),
            (16, 'Drama', 'Alexander Adams, Zoe Baker', 'Kathleen Kennedy'),
            (17, 'Action', 'Ryan Nelson, Hannah Carter', 'Ridley Scott'),
            (18, 'Documentary', 'Jacob Mitchell, Natalie Perez', 'Peter Jackson'),
            (19, 'Thriller', 'Ethan Roberts, Ella Turner', 'J.J. Abrams'),
            (20, 'Drama', 'Nicholas Phillips, Victoria Campbell', 'Christopher Nolan')
    """)

    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE series_db


# CREATE AND POPULATE user_db


# CREATE AND POPULATE metadata_db


# CREATE AND POPULATE advertisement_db



def dbInit():
    createPostgreSQL()
    print("Databases created successfully")

dbInit()