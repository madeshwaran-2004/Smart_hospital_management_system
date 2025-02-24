# import mysql.connector
# from mysql.connector import Error

# def setup_database():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="anand$2005"
#         )
        
#         if connection.is_connected():
#             cursor = connection.cursor()
            
#             # Create database
#             cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_management")
#             print("Database created successfully!")
            
#             # Use the database
#             cursor.execute("USE hospital_management")
            
#             print("Setup completed successfully!")
            
#     except Error as e:
#         print(f"Error: {e}")
        
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection closed.")

# if __name__ == "__main__":
#     setup_database()