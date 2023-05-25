import psycopg2

def manage_connection(query):
# connect to the database
        connection = psycopg2.connect(
            host="localhost",
            port = '5432', 
            database="Restaurant",
            user="postgres",
            password="bubaleh23"
        )

        with connection:
            with connection.cursor() as cursor:   #it will close the cursor automatically
                 if "SELECT" in query:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                 else:
                    cursor.execute(query)
                    connection.commit()
                    
                #  connection.close() #it will close the connection automatically

class MenuManager:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price


    @classmethod
    def get_by_name(cls, name):
        name = name.title()
        query = f"SELECT item_name, item_price FROM Menu_Items WHERE item_name = '{name}'"
        try:
            result = manage_connection(query)
            if result:
                # Return the item if it exists
                return result
            else:
                # Return None if the item does not exist
                return None
        except:
            raise Exception("Connection to server failed")

    
    @classmethod
    def all(cls):
        query = f"SELECT item_name, item_price FROM menu_items"
        try:
            return manage_connection(query)
        except:
            raise Exception("Connection to server failed")


     
     
      
        


         