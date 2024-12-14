"""
Frontend application for managing local PostgreSQL databases of an on-demand media subscription platform Metflix.
"""

import psycopg2


class DatabaseHandler:
    """
    Handles all database-related actions
    """

    def __init__(self):
        """
        Fetches database cursors to the different databases
        """
        self.movie_db_conn = psycopg2.connect(
            dbname="movie_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )
        self.movie_cur = self.movie_db_conn.cursor()

        self.series_db_conn = psycopg2.connect(
            dbname="series_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )
        self.series_cur = self.series_db_conn.cursor()

        self.user_db_conn = psycopg2.connect(
            dbname="user_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )
        self.user_cur = self.user_db_conn.cursor()

        self.metadata_db_conn = psycopg2.connect(
            dbname="metadata_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )
        self.metadata_cur = self.metadata_db_conn.cursor()

        self.advertisement_db_conn = psycopg2.connect(
            dbname="advertisement_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )
        self.advertisement_cur = self.advertisement_db_conn.cursor()

    def add_user(self, user_id, email, age, first_name, last_name, subscription_status, main_genre, secondary_genre, region):
        self.usercur.execute("""
                         INSERT INTO users (user_id, email, age, first_name, last_name)
                         VALUES (?, ?, ?, ?, ?)""", (user_id, email, age, first_name, last_name))
        
        self.usercur.execute("""
                         INSERT INTO subscribers (user_id, subscription_status)
                         VALUES (?, ?)""", (user_id, subscription_status))
        self.usercur.execute("""
                         INSERT INTO user_preferences (user_id, main_genre, secondary_genre)
                         VALUES (?, ?, ?)""", (user_id, main_genre, secondary_genre))
        if region == 'AMERICAS':
            self.usercur.execute("""
                             INSERT INTO AMERICAS_users (user_id, region_AMERICAS)
                             VALUES (?, ?)
                             """, (user_id, region))
        elif region == 'EMEA':
            self.usercur.execute("""
                             INSERT INTO EMEA_users (user_id, region_EMEA)
                             VALUES (?, ?)
                             """, (user_id, region))
        elif region == 'ASIA':
            self.usercur.execute("""
                             INSERT INTO ASIA_users (user_id, region_ASIA)
                             VALUES (?, ?)
                             """, (user_id, region))

        self.user_db_conn.commit()

        print(f"User {first_name} {last_name} added successfully!")


    def find_all_movies_in_country(self, country):
        """
        Finds all available movies in a given country
        """

        # COALESCE combines countries as one, there can only be one country due to the checks. LEFT JOIN is used to
        # keep all the information since a country cannot be in multiple regions. LOWER case makes the checks
        # case insensitive.
        self.movie_cur.execute(
            f"""
            SELECT m.*, COALESCE(r1.region_americas, r2.region_asia, r3.region_emea) as country
            FROM movies m
            LEFT JOIN americas_content r1
            ON m.movie_id = r1.movie_id AND LOWER(r1.region_americas) = LOWER('{country}')
            LEFT JOIN asia_content r2
            ON m.movie_id = r2.movie_id AND LOWER(r2.region_asia) = LOWER('{country}')
            LEFT JOIN emea_content r3
            ON m.movie_id = r3.movie_id AND LOWER(r3.region_emea) = LOWER('{country}')
            WHERE LOWER(COALESCE(r1.region_americas, r2.region_asia, r3.region_emea)) = LOWER('{country}');
            """
        )

        # All entries are printed one by one
        movies = self.movie_cur.fetchall()
        if movies:
            for entry in movies:
                print(entry)
        # Fallback if nothing is found
        else:
            print("No movies were found. Try again!")

    def update_movie(self, movie_id, title, runtime, description, release_date):
        """
        Updates movie information based on the movie_id
        """
        self.movie_cur.execute(
            f"""
            UPDATE movies
            SET title = '{title}', runtime = '{runtime}', description = '{description}', release_date = '{release_date}'
            WHERE movie_id = '{movie_id}';
            """
        )
        self.movie_db_conn.commit()
        print("Entry updated")

    def find_movie_reviews(self, movie_id):
        """
        Finds all movie reviews based on a movie_id
        """
        self.movie_cur.execute(
            f"""
            SELECT *
            FROM reviews
            WHERE movie_id = '{movie_id}';
            """
        )

        # All entries are printed one by one
        reviews = self.movie_cur.fetchall()
        if reviews:
            for entry in reviews:
                print(entry)
        # Fallback if nothing is found
        else:
            print("No reviews were found. Try again!")

    def insert_movie_review(self, movie_id, rating, comment):
        """
        Inserts new reviews to the reviews table
        """
        self.movie_cur.execute(
            f"""
            INSERT INTO reviews (movie_id, rating, comments)
            VALUES ('{movie_id}', '{rating}', '{comment}');
            """
        )

        # Updates database is committed
        self.movie_db_conn.commit()
        print("Movie review inserted")

    def delete_movie_reviews(self, movie_id):
        """
        Deletes movie reviews for a given movie_id
        """
        self.movie_cur.execute(
            f"""
            DELETE FROM reviews
            WHERE movie_id = '{movie_id}';
            """
        )

        # Updates database is committed
        self.movie_db_conn.commit()
        print("Movie reviews deleted")

    def find_all_series_in_country(self, country):
        """
        Finds all available movies in a given country
        """
        # COALESCE combines countries as one, there can only be one country due to the checks. LEFT JOIN is used to
        # keep all the information since a country cannot be in multiple regions. LOWER case makes the checks
        # case insensitive.
        self.series_cur.execute(
            f"""
            SELECT s.*, COALESCE(r1.region_americas, r2.region_asia, r3.region_emea) as country
            FROM series s
            LEFT JOIN americas_content r1
            ON s.series_id = r1.series_id AND LOWER(r1.region_americas) = LOWER('{country}')
            LEFT JOIN asia_content r2
            ON s.series_id = r2.series_id AND LOWER(r2.region_asia) = LOWER('{country}')
            LEFT JOIN emea_content r3
            ON s.series_id = r3.series_id AND LOWER(r3.region_emea) = LOWER('{country}')
            WHERE LOWER(COALESCE(r1.region_americas, r2.region_asia, r3.region_emea)) = LOWER('{country}');
            """
        )

        # All entries are printed one by one
        series = self.series_cur.fetchall()
        if series:
            for entry in series:
                print(entry)
        # Fallback if nothing is found
        else:
            print("No series were found. Try again!")

    def update_series(self, series_id, title, episodes, seasons, description, release_date):
        """
        Updates series information based on the series_id
        """
        self.series_cur.execute(
            f"""
            UPDATE series
            SET title = '{title}', episodes = '{episodes}', seasons = '{seasons}', description = '{description}', release_date = '{release_date}'
            WHERE series_id = '{series_id}';
            """
        )

        # Updates database is committed
        self.series_db_conn.commit()
        print("Entry updated")

    def find_series_reviews(self, series_id):
        """
        Finds all series reviews based on the series_id
        """
        self.series_cur.execute(
            f"""
            SELECT *
            FROM reviews
            WHERE series_id = '{series_id}';
            """
        )

                # All entries are printed one by one
        reviews = self.series_cur.fetchall()
        if reviews:
            for entry in reviews:
                print(entry)
        # Fallback if nothing is found
        else:
            print("No reviews were found. Try again!")

    def insert_series_review(self, series_id, rating, comment):
        """
        Inserts new reviews to the reviews table
        """
        self.series_cur.execute(
            f"""
            INSERT INTO reviews (series_id, rating, comments)
            VALUES ('{series_id}', '{rating}', '{comment}');
            """
        )

        # Updates database is committed
        self.series_db_conn.commit()
        print("Series review inserted")

    def delete_series_reviews(self, series_id):
        """
        Deletes series reviews for a given series_id
        """
        self.series_cur.execute(
            f"""
            DELETE FROM reviews
            WHERE series_id = '{series_id}';
            """
        )

        # Updates database is committed
        self.series_db_conn.commit()
        print("Series reviews deleted")

    def find_all_movies_and_series(self):
        """
        Finds all available movies and series with their respective country
        """
        # STRING_AGG combines entries from the r resulting of the LEFT JOIN, essentially "' ".join(r.country) in Python.
        # CAST ensures that whatever is throwns at STRING_AGG is TEXT avoiding errors.
        self.movie_cur.execute(
            """
            SELECT m.*, STRING_AGG(DISTINCT r.country, ', ') AS countries
            FROM movies m
            LEFT JOIN (
                SELECT movie_id, CAST(region_americas AS TEXT) AS country FROM americas_content
                UNION ALL
                SELECT movie_id, CAST(region_asia AS TEXT) AS country FROM asia_content
                UNION ALL
                SELECT movie_id, CAST(region_emea AS TEXT) AS country FROM emea_content
            ) r ON m.movie_id = r.movie_id
            GROUP BY m.movie_id;
            """
        )
        self.series_cur.execute(
            """
            SELECT s.*, STRING_AGG(DISTINCT r.country, ', ') AS countries
            FROM series s
            LEFT JOIN (
                SELECT series_id, CAST(region_americas AS TEXT) AS country FROM americas_content
                UNION ALL
                SELECT series_id, CAST(region_asia AS TEXT) AS country FROM asia_content
                UNION ALL
                SELECT series_id, CAST(region_emea AS TEXT) AS country FROM emea_content
            ) r ON s.series_id = r.series_id
            GROUP BY s.series_id;
            """
        )

        # All entries are printed one by one
        movies = self.movie_cur.fetchall()
        series = self.series_cur.fetchall()

        # Concenate entries from movies and series queries to one
        entries = movies + series

        # All entries are printed one by one
        if entries:
            for entry in entries:
                print(entry)
        # Fallback if nothing is found
        else:
            print("No entries were found. Try again!")

    def find_all_user_information(self):
        """
        Finds all users with their respective information
        """
        self.user_cur.execute(
            """
            SELECT u.*, COALESCE(r1.region_americas, r2.region_asia, r3.region_emea) as country, pref.main_genre, pref.secondary_genre, sub.subscription_status
            FROM users u
            LEFT JOIN americas_users r1
            ON u.user_id = r1.user_id
            LEFT JOIN asia_users r2
            ON u.user_id = r2.user_id
            LEFT JOIN emea_users r3
            ON u.user_id = r3.user_id
            JOIN user_preferences pref
            ON u.user_id = pref.user_id
            JOIN subscribers sub
            ON u.user_id = sub.user_id;
            """
        )
        self.metadata_cur.execute(
            """
            SELECT * FROM user_meta
            """
        )
        metadata = self.metadata_cur.fetchall()
        users = self.user_cur.fetchall()

        # Intermediate list for storing data from both databases
        found_entries = []

        # All entries are printed one by one
        if users:
            for user in users:
                found_entries.append(list(user))
        # Fallback if nothing is found
        else:
            print("No users were found. Try again!")
            return

        # Add informative header due to amount of data
        print("[ID, Email, Age, Firstname, Lastname, Country, Favorite Genre #1, Favorite Genre #2, Subscription Status, Account Created, Watch Time, Subscribed For, Last Login]")
        for entry in found_entries:
            for data in metadata:
                # If the ids match, append metadata to the user element
                if data[0] == entry[0]:
                    entry.append(data[1:])
            print(entry)


    def quit(self):
        print("Closing connections to databases...")
        self.movie_db_conn.close()
        self.movie_cur.close()
        self.series_db_conn.close()
        self.series_cur.close()
        self.user_db_conn.close()
        self.user_cur.close()
        self.metadata_db_conn.close()
        self.metadata_cur.close()
        self.advertisement_db_conn.close()
        self.advertisement_cur.close()


def main_menu():
    print("\n---------------- MAIN MENU ----------------")
    print("1) Media context menu")
    print("2) User context menu")
    print("0) Quit")
    print("--------------------------------------------")

    return input("Selection: ")


def media_menu():
    print("\n---------------- MEDIA MENU ----------------")
    print("1) Show movie selection available in a specific country")
    print("2) Update movie information")
    print("3) Show movie reviews")
    print("4) Insert movie review")
    print("5) Delete movie reviews")
    print("6) Show series selection available in a specific country")
    print("7) Update series information")
    print("8) Show series reviews")
    print("9) Insert series review")
    print("10) Delete series reviews")
    print("11) Show all movies and series available")
    print("0) Go back")
    print("--------------------------------------------")

    return input("Selection: ")

def user_menu():
    print("\n---------------- USER MENU ----------------")
    print("\n1) Show all relevant user information")
    print("0) Go back")
    print("--------------------------------------------")

    return input("Selection: ")


def main():
    database_handler = DatabaseHandler()

    # Main state machine; Main loop
    while 1:
        match main_menu():
            case "0":
                break
            case "1":
                # Loop through menu
                while 1:
                    # Media context menu
                    match media_menu():
                        case "0":
                            break

                        # Cases related to movies
                        case "1":
                            country = input("Which country? (e.g., Brazil): ")
                            database_handler.find_all_movies_in_country(country)
                        case "2":
                            movie_id = input("Enter the id of the movie to be updated: ")
                            title = input("Enter a new title for the movie: ")
                            runtime = input("Enter a new runtime for the movie: ")
                            description = input("Enter a new description for the movie: ")
                            release_date = input("Enter a new release date for the movie: ")
                            database_handler.update_movie(movie_id, title, runtime, description, release_date)
                        case "3":
                            movie_id = input("Enter the id of the movie: ")
                            database_handler.find_movie_reviews(movie_id)
                        case "4":
                            movie_id = input("Enter the id of the movie: ")
                            rating = float(input("Enter the rating (1.0-10.0): "))
                            comment = input("Enter a comment: ")
                            if rating > 10.0 or rating < 1.0:
                                print("Invalid rating, rating must be between 1.0 and 10.0.")
                                continue
                            database_handler.insert_movie_review(movie_id, float(rating), comment)
                        case "5":
                            movie_id = input("Enter the id of the movie: ")
                            database_handler.delete_movie_reviews(movie_id)

                        # Cases related to series
                        case "6":
                            country = input("Which country? (e.g., Brazil): ")
                            database_handler.find_all_series_in_country(country)
                        case "7":
                            series_id = input("Enter the id of the series to be updated: ")
                            title = input("Enter a new title for the series: ")
                            episodes = input("Enter a new episode count for the series: ")
                            seasons = input("Enter a new season count for the series: ")
                            description = input("Enter a new description for the series: ")
                            release_date = input("Enter a new release date for the series: ")
                            database_handler.update_series(series_id, title, episodes, seasons, description, release_date)
                        case "8":
                            series_id = input("Enter the id of the series: ")
                            database_handler.find_series_reviews(series_id)
                        case "9":
                            series_id = input("Enter the id of the series: ")
                            rating = float(input("Enter the rating (1.0-10.0): "))
                            if rating > 10.0 or rating < 1.0:
                                print("Invalid rating, rating must be between 1.0 and 10.0.")
                                continue
                            comment = input("Enter a comment: ")
                            database_handler.insert_series_review(series_id, rating, comment)
                        case "10":
                            series_id = input("Enter the id of the series: ")
                            database_handler.delete_series_reviews(series_id)

                        # Cases related to both movies and series
                        case "11":
                            database_handler.find_all_movies_and_series()

                        # Catches erronous inputs and continues looping
                        case _:
                            print("Erronous input, try again!")
            case "2":
                # Loop through menu
                while 1:
                    # User context menu
                    match user_menu():
                        case "0":
                            break
                        case "1":
                            database_handler.find_all_user_information()
                        case _:
                            print("Erronous input, try again!")

            # Catches erronous inputs and continues looping
            case _:
                print("Erronous input, try again!")

    database_handler.quit()

    print("Exiting application...")


if __name__ == "__main__":
    main()
