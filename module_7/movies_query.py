import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"],))

    #print("\n\n Press any key to continue...")

    cursor = db.cursor()

    # STUDIO
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    print("\n\n-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: " + str(studio[0]))
        print("Studio Name: " + str(studio[1]))
        print("")

    # GENRE
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: " + str(genre[0]))
        print("Genre Name: " + str(genre[1]))
        print("")

    # SHORT FILMS
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    films = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: " + str(film[0]))
        print("Runtime: " + str(film[1]))
        print("")

    # DIRECTORS
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
    directors = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")
    for director in directors:
        print("Film Name: " + str(director[0]))
        print("Director: " + str(director[1]))
        print("")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)


finally:
    db.close()
