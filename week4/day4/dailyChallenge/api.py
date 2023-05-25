import requests
import json
import pprint
import psycopg2
import random

# Instructions
# Using this API, create the functionality which will write 10 random countries to your database.

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.
    

# Connect to your PostgreSQL database

connection = psycopg2.connect( 
    database="Countries", 
    user='postgres',
    password='bubaleh23',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()


# Create a table to store country data if it doesn't exist
query = "CREATE TABLE countries (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, capital VARCHAR(50) NOT NULL, flag_code VARCHAR(50) NOT NULL, subregion VARCHAR(50) NOT NULL, population INTEGER)"
cursor.execute(query)
connection.commit() #saving the changes in the database


# Get all countries from the API
countries_api = requests.get('https://restcountries.com/v3.1/all')
countries_api.raise_for_status() # Check for errors
data = countries_api.json()


# Iterate over the selected countries and insert data into the database
for i in range(10):
    choice = random.choice(data)
    name = choice['name']['official'].replace("'","")
    capital = choice['capital'][0].replace("'","")
    flag = choice['flags']['png']
    subregion = choice['subregion'].replace("'","")
    population =  choice['population']
    query = f"INSERT INTO countries (name, capital, flag_code, subregion, population)" \
            f"VALUES ('{name}', '{capital}', '{flag}', '{subregion}', '{population}');"
    cursor.execute(query)
    connection.commit()

# Close the cursor, and close the connection
cursor.close()
connection.close()




# pprint.pprint(data[0]['population'])
# print(type(data))
# name = data[0]['name']['common']
# capital = data[0]['capital'][0]
# flag = data[0]['flag']
# subregion = data[0]['subregion']
# population = data[0]['population']
# pprint.pprint(data[0]['name']['official'].replace("'",""))
