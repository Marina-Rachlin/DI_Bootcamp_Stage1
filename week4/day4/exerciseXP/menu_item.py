import psycopg2
from menu_manager import MenuManager

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



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    # I will use "try-except" because if we will try to assign to a variable the result of manage_connection method but the connection failed in this place our program will crash 
    def save(self): 
        self.name = self.name.capitalize()
        try:
            # Check if an item with the same name and price already exists
            check_query = f"SELECT * FROM menu_items WHERE item_name = '{self.name}' AND item_price = '{self.price}'"
            result = manage_connection(check_query)

            if not result:
            # If no item exists with the same name and price, insert the new item
                query = f"INSERT INTO menu_items (item_name, item_price) VALUES ('{self.name}', '{self.price}')"
                manage_connection(query)
            else:
                print("Item with the same name and price already exists.")
        except:
            raise Exception("Connection to server failed")  # Raise an exception when the connection fails 
                  

    def delete(self):
        try:
            # Check if the item exists. We will need it later
            check_query = f"SELECT * FROM menu_items WHERE item_name = '{self.name}'"
            result = manage_connection(check_query)

            if result:
                # Delete the item
                query = f"DELETE FROM menu_items WHERE item_name = '{self.name}'"
                manage_connection(query)
                return True # we will need it later
            else:
                return False
        except:
            raise Exception("Connection to server failed")


    def update(self, new_name, new_price):
        if not isinstance(new_name, str):
            print("Invalid name. Name must be a string.")
            return

        name = new_name.title()
        
        if not isinstance(new_price, int):
           print("Invalid price. Price must be an integer.")
           return
        
        # Check if the item exists
        check_query = f"SELECT * FROM menu_items WHERE item_name = '{self.name}' AND item_price = '{self.price}'"
        result = manage_connection(check_query)

        if not result:
            print("Item does not exist.")
            return

        try:
            query = f"UPDATE menu_items SET item_name = '{name}', item_price = '{new_price}' WHERE item_name = '{self.name}'"
            self.name = name
            self.price = new_price
            manage_connection(query)
            print("Item was updated successfully.")
        except:
            raise Exception("Connection to server failed")



# item = MenuItem('Burger', 35)
# item.save()
# item.update('burger', 37)


   



