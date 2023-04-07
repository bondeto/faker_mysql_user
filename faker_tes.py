from faker import Faker
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="data"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create a Faker object
fake = Faker()

try:
    # Insert 10 fake user records into the database
    for i in range(1000000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        age = fake.random_int(min=18, max=80)
        sql = "INSERT INTO user (first_name, last_name, email, age) VALUES (%s, %s, %s, %s)"
        val = (first_name, last_name, email, age)
        mycursor.execute(sql, val)

        # Commit the changes to the database
        mydb.commit()
 # Print the number of rows that were inserted
        print(mycursor.rowcount, "rows were inserted.")

except KeyboardInterrupt:
    print("Program interrupted by user. Exiting...")
