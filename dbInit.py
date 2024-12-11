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

    #  DELETE IF EXISTS
    cursor.execute("DROP DATABASE IF EXISTS movie_db")
    cursor.execute("DROP DATABASE IF EXISTS series_db")
    cursor.execute("DROP DATABASE IF EXISTS user_db")
    cursor.execute("DROP DATABASE IF EXISTS metadata_db")
    cursor.execute("DROP DATABASE IF EXISTS advertisement_db")
    print("Deleted pre-existing databases with similar names")

    # CREATE DBs
    cursor.execute("CREATE DATABASE movie_db")
    print("Created movie_db")
    cursor.execute("CREATE DATABASE series_db")
    print("Created series_db")
    cursor.execute("CREATE DATABASE user_db")
    print("Created user_db")
    cursor.execute("CREATE DATABASE metadata_db")
    print("Created metadata_db")
    cursor.execute("CREATE DATABASE advertisement_db")
    print("Created advertisement_db")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()
    print("\nPostgreSQL databases created successfully")
    print("Creating tables and populating databases...\n")
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
    
    print("#############################################")
    print("Created tables in movie_db")
    
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
    print("Populated tables in movie_db")
    print("#############################################")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE series_db
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="series_db",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # CREATE TABLES

    cursor.execute("""
        CREATE TABLE series (
            series_id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            episodes INTEGER,
            seasons INTEGER,
            description TEXT,
            release_date DATE
        )""")

    cursor.execute("""
        CREATE TABLE AMERICAS_content (
            series_id INTEGER REFERENCES series(series_id),
            region_AMERICAS VARCHAR(255)
        )""")
    
    cursor.execute("""
        CREATE TABLE EMEA_content (
            series_id INTEGER REFERENCES series(series_id),
            region_EMEA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE ASIA_content (
            series_id INTEGER REFERENCES series(series_id),
            region_ASIA VARCHAR(255)
        )""")
    
    cursor.execute("""
        CREATE TABLE reviews (
            series_id INTEGER REFERENCES series(series_id),
            rating DECIMAL(10,2),
            comments TEXT
        )""")
    
    cursor.execute("""
        CREATE TABLE casting (
            series_id INTEGER REFERENCES series(series_id),
            genre VARCHAR(255),
            actors TEXT,
            director TEXT
        )""")
    print("Created tables in series_db")

    # INSERT DATA INTO TABLES

    cursor.execute("""
        INSERT INTO series (series_id, title, episodes, seasons, description, release_date) VALUES
            (1, 'Mystic Falls', 1, 1, 'Mystery in a small town', '2021-01-01'),
            (2, 'Quantum Leap', 2, 1, 'Time travel adventures', '2021-01-02'),
            (3, 'Hidden Truths', 17, 2, 'Uncovering hidden secrets', '2021-01-03'),
            (4, 'Silent Echo', 5, 1, 'Echoes of the past', '2021-01-04'),
            (5, 'Urban Legends', 10, 1, 'Urban myths come alive', '2021-01-05'),
            (6, 'Lost Souls', 8, 2, 'Lost souls seeking redemption', '2021-01-06'),
            (7, 'Dark Secrets', 89, 9, 'Dark secrets revealed', '2021-01-07'),
            (8, 'Final Hour', 81, 7, 'Race against time', '2021-01-08'),
            (9, 'Broken Dreams', 19, 2, 'Dreams shattered by reality', '2021-01-09'),
            (10, 'Shattered Lives', 20, 2, 'Lives intertwined by fate', '2021-01-10'),
            (11, 'Eternal Night', 31, 3, 'Eternal night of suspense', '2021-01-11'),
            (12, 'Forgotten Tales', 62, 11, 'Forgotten tales retold', '2021-01-12'),
            (13, 'Secret Garden', 3, 1, 'Secrets of a hidden garden', '2021-01-13'),
            (14, 'Twilight Zone', 44, 6, 'Exploring the unknown', '2021-01-14'),
            (15, 'Parallel Worlds', 15, 2, 'Parallel worlds collide', '2021-01-15'),
            (16, 'Haunted Manor', 9, 1, 'Haunted manor mysteries', '2021-01-16'),
            (17, 'Crimson Peak', 17, 2, 'Crimson peak dark history', '2021-01-17'),
            (18, 'Midnight Sun', 72, 10, 'Midnight sun hidden truths', '2021-01-18'),
            (19, 'Echoes of Time', 31, 6, 'Echoes of time travel', '2021-01-19'),
            (20, 'Vanishing Point', 24, 3, 'Vanishing point of reality', '2021-01-20')
    """)

    cursor.execute("""
        INSERT INTO AMERICAS_content (series_id, region_AMERICAS) VALUES
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
        INSERT INTO EMEA_content (series_id, region_EMEA) VALUES
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
        INSERT INTO ASIA_content (series_id, region_ASIA) VALUES
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
        INSERT INTO reviews (series_id, rating, comments) VALUES
            (1, 2.11, 'Amazing plot and characters'),
            (2, 3.40, 'Loved the cinematography'),
            (3, 7.10, 'Great acting, but slow pace'),
            (4, 2.20, 'Not what I expected'),
            (5, 4.56, 'A must-watch for everyone'),
            (6, 10.0, 'Too predictable and cliché'),
            (7, 3.90, 'Fantastic special effects'),
            (8, 6.80, 'Could have been better'),
            (9, 3.66, 'Highly entertaining and fun'),
            (10, 8.12, 'Disappointing ending'),
            (11, 4.51, 'Brilliant from start to finish'),
            (12, 7.77, 'Mediocre at best'),
            (13, 3.53, 'Exceeded my expectations'),
            (14, 4.31, 'Boring and unoriginal'),
            (15, 10.00, 'Heartwarming and touching'),
            (16, 2.12, 'Not worth the hype'),
            (17, 5.43, 'A visual masterpiece'),
            (18, 7.53, 'Poor script and dialogue'),
            (19, 3.34, 'Engaging and thrilling'),
            (20, 4.67, 'Forgettable experience')
    """)

    cursor.execute("""
        INSERT INTO casting (series_id, genre, actors, director) VALUES
        (1, 'Documentary', 'John Smith, Jane Doe', 'Lucas Bennett'),
        (2, 'Drama', 'Michael Johnson, Emily Davis', 'Amelia Foster'),
        (3, 'Action', 'Robert Brown, Jessica Wilson', 'Henry Collins'),
        (4, 'Drama', 'William Taylor, Sarah Moore', 'Grace Mitchell'),
        (5, 'Documentary', 'David Anderson, Laura Thomas', 'Jack Parker'),
        (6, 'Documentary', 'James Jackson, Olivia White', 'Lily Evans'),
        (7, 'Action', 'Christopher Harris, Emma Martin', 'Owen Brooks'),
        (8, 'Cartoon', 'Daniel Thompson, Sophia Garcia', 'Ava Morgan'),
        (9, 'Documentary', 'Matthew Martinez, Isabella Robinson', 'Noah Reed'),
        (10, 'Action', 'Anthony Clark, Mia Rodriguez', 'Emma Hayes'),
        (11, 'Drama', 'Joshua Lewis, Ava Lee', 'Mason Cooper'),
        (12, 'Drama', 'Andrew Walker, Abigail Hall', 'Chloe Adams'),
        (13, 'Drama', 'Joseph Allen, Lily Young', 'Logan Turner'),
        (14, 'Action', 'Benjamin King, Chloe Wright', 'Mia Scott'),
        (15,' Drama', 'Samuel Scott, Grace Green', 'Ethan Bailey'),
        (16, 'Documentary', 'Alexander Adams, Zoe Baker', 'Zoe Carter'),
        (17, 'Drama', 'Ryan Nelson, Hannah Carter', 'Caleb Hughes'),
        (18, 'Drama', 'Jacob Mitchell, Natalie Perez', 'Ella Jenkins'),
        (19, 'Drama', 'Ethan Roberts, Ella Turner', 'Aiden Ross'),
        (20, 'Action', 'Nicholas Phillips, Victoria Campbell', 'Natalie Simmons')
    """)
    print("Populated tables in series_db")
    print("#############################################")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE user_db
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="user_db",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # CREATE TABLES

    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            email VARCHAR(255),
            age INTEGER,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE AMERICAS_users (
            user_id INTEGER REFERENCES users(user_id),
            region_AMERICAS VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE EMEA_users (
            user_id INTEGER REFERENCES users(user_id),
            region_EMEA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE ASIA_users (
            user_id INTEGER REFERENCES users(user_id),
            region_ASIA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE subscribers (
            user_id INTEGER REFERENCES users(user_id),
            subscription_status BOOLEAN
        )""")

    cursor.execute("""
        CREATE TABLE user_preferences (
            user_id INTEGER REFERENCES users(user_id),
            main_genre VARCHAR(255),
            secondary_genre VARCHAR(255)
        )""")
    print("Created tables in user_db")

    # INSERT DATA INTO TABLES

    cursor.execute("""
        INSERT INTO users (user_id, email, age, first_name, last_name) VALUES
            (1, 'a@gmail.com', 18, 'Jack', 'Jones'),
            (2, 'b@gmail.com', 19, 'Jill', 'Jackson'),
            (3, 'c@gmail.com', 20, 'Joe', 'Johnson'),
            (4, 'd@gmail.com', 21, 'Jane', 'Jefferson'),
            (5, 'e@gmail.com', 22, 'Jeff', 'Washington'),
            (6, 'f@gmail.com', 23, 'Alex', 'Garfield'),
            (7, 'g@gmail.com', 24, 'Brian', 'Bridges'),
            (8, 'h@gmail.com', 25, 'Carla', 'Hill'),
            (9, 'i@gmail.com', 26, 'Anna', 'Eriksson'),
            (10, 'j@gmail.com', 27, 'Emma', 'Hendricks'),
            (11, 'k@gmail.com', 28, 'Joan', 'Mcdavid'),
            (12, 'l@gmail.com', 29, 'Jeffrey', 'Lewis'),
            (13, 'm@gmail.com', 30, 'Tim', 'Shields'),
            (14, 'n@gmail.com', 31, 'Oscar', 'Smith'),
            (15, 'o@gmail.com', 32, 'Hannah', 'Anderson'),
            (16, 'p@gmail.com', 33, 'William', 'Summers'),
            (17, 'q@gmail.com', 34, 'Megan', 'Morrison'),
            (18, 'r@gmail.com', 35, 'Susan', 'Olsen'),
            (19, 's@gmail.com', 36, 'Geoff', 'Larson'),
            (20, 't@gmail.com', 37, 'Wayne', 'Ekholm')
        """)

    cursor.execute("""
        INSERT INTO AMERICAS_users (user_id, region_AMERICAS) VALUES
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
        INSERT INTO EMEA_users (user_id, region_EMEA) VALUES
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
        INSERT INTO ASIA_users (user_id, region_ASIA) VALUES
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
        INSERT INTO subscribers (user_id, subscription_status) VALUES
            (1, TRUE),
            (2, TRUE),
            (3, FALSE),
            (4, TRUE),
            (5, FALSE),
            (6, FALSE),
            (7, FALSE),
            (8, TRUE),
            (9, FALSE),
            (10, FALSE),
            (11, TRUE),
            (12, FALSE),
            (13, FALSE),
            (14, TRUE),
            (15, FALSE),
            (16, TRUE),
            (17, TRUE),
            (18, TRUE),
            (19, FALSE),
            (20, FALSE)

        """)

    cursor.execute("""
        INSERT INTO user_preferences (user_id, main_genre, secondary_genre) VALUES
            (1, 'Action', 'Documentary'),
            (2, 'Documentary', 'Horror'),
            (3, 'Drama', 'Action'),
            (4, 'Documentary', 'Thriller'),
            (5, 'Drama', 'Thriller'),
            (6, 'Action', 'Drama'),
            (7, 'Action', 'Documentary'),
            (8, 'Drama', 'Thriller'),
            (9, 'Horror', 'Thriller'),
            (10, 'Thriller', 'Action'),
            (11, 'Horror', 'Drama'),
            (12, 'Thriller', 'Cartoon'),
            (13, 'Horror', 'Action'),
            (14, 'Drama', 'Thriller'),
            (15, 'Action', 'Drama'),
            (16, 'Drama', 'Cartoon'),
            (17, 'Action', 'Documentary'),
            (18, 'Cartoon', 'Documentary'),
            (19, 'Action', 'Horror'),
            (20, 'Action', 'Horror')
        """)
    print("Populated tables in user_db")
    print("#############################################")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE metadata_db
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="metadata_db",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # CREATE TABLES

    cursor.execute("""
        CREATE TABLE purchases (
            user_id INTEGER,
            purchase_date DATE ARRAY
        )""")

    cursor.execute("""
        CREATE TABLE movie_history (
            user_id INTEGER,
            movie_id INTEGER ARRAY
        )""")

    cursor.execute("""
        CREATE TABLE series_history (
            user_id INTEGER,
            series_id INTEGER ARRAY
        )""")

    cursor.execute("""
        CREATE TABLE search_history (
            user_id INTEGER,
            search_query TEXT ARRAY
        )""")

    cursor.execute("""
        CREATE TABLE user_meta (
            user_id INTEGER,
            created DATE,
            watchtime INTEGER,
            subcribed_for INTEGER,
            last_login DATE
        )""")
    print("Created tables in metadata_db")

    # INSERT DATA INTO TABLES

    cursor.execute("""
        INSERT INTO purchases (user_id, purchase_date) VALUES
            (1, '{"2021-01-01"}'),
            (2, '{"2021-01-02"}'),
            (3, '{"2021-01-03","2021-01-04"}'),
            (4, '{"2021-01-05"}'),
            (5, '{"2021-01-06"}'),
            (6, '{"2021-01-07"}'),
            (7, '{"2021-01-08", "2021-01-02"}'),
            (8, '{"2021-01-09"}'),
            (9, '{"2021-01-10"}'),
            (10, '{"2021-01-11"}'),
            (11, '{"2021-01-12","2021-01-02"}'),
            (12, '{"2021-01-13"}'),
            (13, '{"2021-01-14"}'),
            (14, '{"2021-01-15"}'),
            (15, '{"2021-01-16"}'),
            (16, '{"2021-01-17"}'),
            (17, '{"2021-01-18","2021-01-02","2021-01-02"}'),
            (18, '{"2021-01-19"}'),
            (19, '{"2021-01-20"}'),
            (20, '{"2021-01-21","2021-01-02"}')
        """)
    
    cursor.execute("""
        INSERT INTO movie_history (user_id, movie_id) VALUES
            (1, '{1}'),
            (2, '{2}'),
            (3, '{3, 4}'),
            (4, '{5}'),
            (5, '{6}'),
            (6, '{7}'),
            (7, '{8, 2}'),
            (8, '{9}'),
            (9, '{10}'),
            (10, '{11}'),
            (11, '{12, 2}'),
            (12, '{13}'),
            (13, '{14}'),
            (14, '{15}'),
            (15, '{16}'),
            (16, '{17}'),
            (17, '{18, 2, 2}'),
            (18, '{19}'),
            (19, '{20}'),
            (20, '{21, 2}')
        """)

    cursor.execute("""
        INSERT INTO series_history (user_id, series_id) VALUES
            (1, '{1}'),
            (2, '{2, 3}'),
            (3, '{3, 4}'),
            (4, '{5, 2}'),
            (5, '{6}'),
            (6, '{7}'),
            (7, '{8, 2}'),
            (8, '{6}'),
            (9, '{10}'),
            (10, '{11}'),
            (11, '{12, 5}'),
            (12, '{13}'),
            (13, '{14}'),
            (14, '{1}'),
            (15, '{16}'),
            (16, '{17}'),
            (17, '{1, 2, 3}'),
            (18, '{19}'),
            (19, '{20}'),
            (20, '{21, 2}')
        """)

    cursor.execute("""
        INSERT INTO search_history (user_id, search_query) VALUES
            (1, '{"action movie", "cartoon series"}'),
            (2, '{"documentary movie", "horror series"}'),
            (3, '{"drama movie", "action series"}'),
            (4, '{"documentary movie", "thriller series"}'),
            (5, '{"drama movie", "thriller series"}'),
            (6, '{"action movie", "drama series"}'),
            (7, '{"action movie", "documentary series"}'),
            (8, '{"drama movie", "thriller series"}'),
            (9, '{"horror movie", "thriller series"}'),
            (10, '{"thriller movie", "action series"}'),
            (11, '{"horror movie", "drama series"}'),
            (12, '{"thriller movie", "cartoon series"}'),
            (13, '{"horror movie", "action series"}'),
            (14, '{"drama movie", "thriller series"}'),
            (15, '{"action movie", "drama series"}'),
            (16, '{"drama movie", "cartoon series"}'),
            (17, '{"action movie", "documentary series"}'),
            (18, '{"cartoon movie", "documentary series"}'),
            (19, '{"action movie", "horror series"}'),
            (20, '{"action movie", "horror series"}')
        """)

    cursor.execute("""
        INSERT INTO user_meta (user_id, created, watchtime, subcribed_for, last_login) VALUES
            (1, '2021-01-01', 120, 1, '2021-01-01'),
            (2, '2021-01-02', 130, 2, '2021-01-02'),
            (3, '2021-01-03', 140, 3, '2021-01-03'),
            (4, '2021-01-04', 150, 4, '2021-01-04'),
            (5, '2021-01-05', 160, 5, '2021-01-05'),
            (6, '2021-01-06', 170, 6, '2021-01-06'),
            (7, '2021-01-07', 180, 7, '2021-01-07'),
            (8, '2021-01-08', 190, 8, '2021-01-08'),
            (9, '2021-01-09', 200, 9, '2021-01-09'),
            (10, '2021-01-10', 210, 10, '2021-01-10'),
            (11, '2021-01-11', 220, 11, '2021-01-11'),
            (12, '2021-01-12', 230, 12, '2021-01-12'),
            (13, '2021-01-13', 240, 13, '2021-01-13'),
            (14, '2021-01-14', 250, 14, '2021-01-14'),
            (15, '2021-01-15', 260, 15, '2021-01-15'),
            (16, '2021-01-16', 270, 16, '2021-01-16'),
            (17, '2021-01-17', 280, 17, '2021-01-17'),
            (18, '2021-01-18', 290, 18, '2021-01-18'),
            (19, '2021-01-19', 300, 19, '2021-01-19'),
            (20, '2021-01-20', 310, 20, '2021-01-20')
        """)
    print("Populated tables in metadata_db")
    print("#############################################")


    # CLOSE CONNECTION
    cursor.close()
    connection.close()

# CREATE AND POPULATE advertisement_db
    # OPEN CONNECTION TO DESIRED DATABASE
    connection = psycopg2.connect(
        host="localhost",
        database="advertisement_db",
        user="postgres",
        password="admin"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # CREATE TABLES
    cursor.execute("""
        CREATE TABLE ads (
            ad_id INTEGER PRIMARY KEY,
            title VARCHAR(255),
            runtime INTEGER,
            advertiser VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE AMERICAS_ads (
            ad_id INTEGER REFERENCES ads(ad_id),
            region_AMERICAS VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE EMEA_ads (
            ad_id INTEGER REFERENCES ads(ad_id),
            region_EMEA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE ASIA_ads (
            ad_id INTEGER REFERENCES ads(ad_id),
            region_ASIA VARCHAR(255)
        )""")

    cursor.execute("""
        CREATE TABLE ad_target (
            ad_id INTEGER REFERENCES ads(ad_id),
            target_age INTEGER,
            target_group VARCHAR(255)
        )""")
    print("Created tables in advertisement_db")

    # INSERT DATA INTO TABLES

    cursor.execute("""
        INSERT INTO ads (ad_id, title, runtime, advertiser) VALUES
            (1, 'Summer Sale', 120, 'Company AB'),
            (2, 'New Arrival', 130, 'Valio OY'),
            (3, 'Limited Offer', 140, 'Pirkka'),
            (4, 'Flash Deal', 150, 'Pirkka'),
            (5, 'Holiday Special', 160, 'Kesko'),
            (6, 'Mega Discount', 170, 'Walmart'),
            (7, 'Exclusive Deal', 180, 'Amazon'),
            (8, 'Winter Clearance', 190, 'Amazon'),
            (9, 'Buy One Free', 200, 'Ebay'),
            (10, 'Weekend Sale', 210, 'Paypal'),
            (11, 'Hot Deals', 220, 'BMW'),
            (12, 'Best Price', 230, 'Volvo'),
            (13, 'Super Savings', 240, 'Steakhouse'),
            (14, 'Clearance Sale', 250, 'Fishmarket'),
            (15, 'Daily Deals', 260, 'Youtube'),
            (16, 'Seasonal Offer', 270, 'Python'),
            (17, 'Big Savings', 280, 'Amazon'),
            (18, 'Special Discount', 290, 'FirstFirst'),
            (19, 'Limited Time', 300, 'Megacorp'),
            (20, 'Grand Opening', 310, 'Amazon')
        """)

    cursor.execute("""
        INSERT INTO AMERICAS_ads (ad_id, region_AMERICAS) VALUES
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
        INSERT INTO EMEA_ads (ad_id, region_EMEA) VALUES
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
            (15, 'Egypt')
        """)

    cursor.execute("""
        INSERT INTO ASIA_ads (ad_id, region_ASIA) VALUES
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
        INSERT INTO ad_target (ad_id, target_age, target_group) VALUES
            (1, 18, 'Students'),
            (2, 19, 'Young Adults'),
            (3, 20, 'Adults'),
            (4, 21, 'Seniors'),
            (5, 22, 'Students'),
            (6, 23, 'Young Adults'),
            (7, 24, 'Adults'),
            (8, 25, 'Seniors'),
            (9, 26, 'Students'),
            (10, 27, 'Young Adults'),
            (11, 28, 'Adults'),
            (12, 29, 'Seniors'),
            (13, 30, 'Students'),
            (14, 31, 'Young Adults'),
            (15, 32, 'Adults'),
            (16, 33, 'Seniors'),
            (17, 34, 'Students'),
            (18, 35, 'Young Adults'),
            (19, 36, 'Adults'),
            (20, 37, 'Seniors')
        """)
    print("Populated tables in advertisement_db")
    print("#############################################")

    # CLOSE CONNECTION
    cursor.close()
    connection.close()


def dbInit():
    createPostgreSQL()
    print("\nDatabase initialization complete, exiting...")

dbInit()