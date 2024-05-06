import mysql.connector

# query = "CREATE TABLE child (name VARCHAR(20), age INT)"

# query = "INSERT INTO child VALUES ('kamal' , 20) , ('saman' , 25) , ('nimal' , 30);"

query = "SELECT * FROM child"
try:
    connection = mysql.connector.connect(host='localhost', database='connector', user='root', password='# give the root password here')
    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    print(result)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
