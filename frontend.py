import psycopg2


class DatabaseHandler:
    """
    Handles all database-related actions
    """

    def __init__(self):
        """
        Fetches database cursors to the different databases
        """
        self.active_cursor = None
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

    def find_all_movies_in_country(self, country):
        self.movie_cur.execute(
            f"""
            SELECT m.*, COALESCE(r1.region_americas, r2.region_asia, r3.region_emea) as country
            FROM movies m
            LEFT JOIN americas_content r1
            ON m.movie_id = r1.movie_id AND r1.region_americas = '{country}'
            LEFT JOIN asia_content r2
            ON m.movie_id = r2.movie_id AND r2.region_asia = '{country}'
            LEFT JOIN emea_content r3
            ON m.movie_id = r3.movie_id AND r3.region_emea = '{country}'
            WHERE COALESCE(r1.region_americas, r2.region_asia, r3.region_emea) = '{country}';
            """
        )
        for entry in self.movie_cur.fetchall():
            print(entry)

    def update_movie(self, movie_id, title, runtime, description, release_date):
        self.movie_cur.execute(
            f"""
            UPDATE movies
            SET title = '{title}', runtime = '{runtime}', description = '{description}', release_date = '{release_date}'
            WHERE movie_id = '{movie_id}';
            """
        )
        self.movie_db_conn.commit()
        print("Entry updated")
        
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
    print("\n1) Show movie selection available in a specific country")
    print("2) Update movie information")
    # print("3) placeholder")
    # print("4) placeholder")
    # print("5) placeholder")
    # print("6) placeholder")
    print("0) Exit the application")


def main():
    database_handler = DatabaseHandler()

    while 1:
        main_menu()
        user_input = input("Please make your selection: ")

        match user_input:
            case "0":
                break
            case "1":
                country = input("Which country? (e.g., Brazil): ")
                database_handler.find_all_movies_in_country(country.capitalize())
            case "2":
                movie_id = input("Enter the id of the movie to be updated: ")
                title = input("Enter a new title for the movie: ")
                runtime = input("Enter a new runtime for the movie: ")
                description = input("Enter a new description for the movie: ")
                release_date = input("Enter a new release date for the movie: ")
                database_handler.update_movie(movie_id, title, runtime, description, release_date)

            case _:
                print("Erronous input, try again!")

    database_handler.quit()

    print("Exiting application...")


if __name__ == "__main__":
    main()
