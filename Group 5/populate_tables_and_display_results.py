"""
GROUP 5
OUTLAND ADVENTURES
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "outland_user",
    "password": "adventure",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"], ))

    cursor = db.cursor()

    # DELETE TABLES IF THEY ALREADY EXIST
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("DROP TABLE IF EXISTS equipment;")
    cursor.execute("DROP TABLE IF EXISTS trips;")


    # CREATE TABLES
    # customers
    cursor.execute("""CREATE TABLE customers (
        customer_ID     INT             NOT NULL        AUTO_INCREMENT,
        first_Name   VARCHAR(25)     NOT NULL,
        last_Name    VARCHAR(25),        
        address    VARCHAR(40),       
        email     VARCHAR(50),
        phone_Number     VARCHAR(50),
        trip_ID     INT,

        PRIMARY KEY(customer_ID)
    ); """)

    # employees
    cursor.execute("""CREATE TABLE employees (
        employee_ID     INT             NOT NULL        AUTO_INCREMENT,
        first_name   VARCHAR(25)     NOT NULL,
        last_Name   VARCHAR(25)     NOT NULL,
        job_Title      VARCHAR(25),
        home_Address   VARCHAR(40),
        work_Email  VARCHAR(50),

        PRIMARY KEY(employee_ID)
    );""")

    # equipment
    cursor.execute("""CREATE TABLE equipment (
        equipment_id   INT             NOT NULL     AUTO_INCREMENT,
        rental  BOOLEAN,
        purchase   BOOLEAN,
        equipment_age INT ,
        inventory      INT,
        trip_ID INT,

        PRIMARY KEY(equipment_id)
    );""")

    # trips
    cursor.execute("""CREATE TABLE trips (
        trip_ID   INT             NOT NULL        AUTO_INCREMENT,
        location  VARCHAR(75),
        airfare   INT,
        visa_requirements     VARCHAR(75),
        inoculations     VARCHAR(75),
        needed_equipment     VARCHAR(75),
        employee_ID     INT,

        PRIMARY KEY(trip_ID)
    );""")


    # POPULATE TABLES
    cursor.execute("""INSERT INTO employees (first_Name, last_Name, job_Title, home_Address, work_Email) 
        VALUES ('Blythe','Timmerson', 'Owner', '55 Woodland Lane', 'BTimmerson@outlandadventures.com');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Jim', 'Ford');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('John', 'MacNell');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Duke', 'Marland');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Anita', 'Gallegos');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Dimitrios', 'Stravopolous');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Mei', 'Wong');""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, trip_ID)
        VALUES('John', 'Doe', '123 Avenue', 'jdoe@mail.com', '123-123-123', 1);""")

    cursor.execute("""INSERT INTO equipment(rental, purchase, equipment_age, inventory, trip_ID)
        VALUES(false, true, 1, 50, 1);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, visa_requirements, inoculations, needed_equipment, employee_ID)
        VALUES(1, 'Africa', 1000, 'Accepted', 'Cleared', 'Canteen', 1);""")


    # PRINT RESULTS
    # CUSTOMERS
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    print("\n\n-- DISPLAYING CUSTOMERS RECORDS --")
    for customer in customers:
        print("Customer ID: " + str(customer[0]))
        print("First Name: " + str(customer[1]))
        print("Last Name: " + str(customer[2]))
        print("Address: " + str(customer[3]))
        print("Email: " + str(customer[4]))
        print("Phone Number: " + str(customer[5]))
        print("Trip ID: " + str(customer[6]))
        print("")

    # EMPLOYEES
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("\n-- DISPLAYING EMPLOYEES RECORDS --")
    for employee in employees:
        print("Employee ID: " + str(employee[0]))
        print("First Name: " + str(employee[1]))
        print("Last Name: " + str(employee[2]))
        print("Job Title: " + str(employee[3]))
        print("Home Address: " + str(employee[4]))
        print("Work Email: " + str(employee[5]))
        print("")

    # EQUIPMENT
    cursor.execute("SELECT * FROM equipment")
    equipment = cursor.fetchall()

    print("\n-- DISPLAYING EQUIPMENT RECORDS --")
    for item in equipment:
        print("Equipment ID: " + str(item[0]))
        print("Rental: " + str(item[1]))
        print("Purchase: " + str(item[2]))
        print("Equipment Age: " + str(item[3]))
        print("Inventory: " + str(item[4]))
        print("Trip ID: " + str(item[5]))
        print("")

    # TRIPS
    cursor.execute("SELECT * FROM trips")
    trips = cursor.fetchall()

    print("\n-- DISPLAYING TRIPS RECORDS --")
    for trip in trips:
        print("Trip ID: " + str(trip[0]))
        print("Location: " + str(trip[1]))
        print("Airfare: " + str(trip[2]))
        print("Visa Requirements: " + str(trip[3]))
        print("Inoculations: " + str(trip[4]))
        print("Equipment Needed: " + str(trip[5]))
        print("Employee ID: " + str(trip[6]))
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