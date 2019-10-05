import mysql.connector

def get_connection():
    print('connection open')
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='banco'
    )

if __name__ == '__main__':
    connection = get_connection()
    print(connection)

    connection.close()
    print('connection closed')