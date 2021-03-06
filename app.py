import streamlit as st
from pymongo import MongoClient

client = MongoClient(**st.secrets['mongo'])


db = client.cars
items = db.info.find()
items = list(items)  # make hashable for st.cache

# st.write(items)

for item in items[0:10]:
    if item['Make'] == 'BMW':
        st.write(
            f"La {item['Make']} {item['Model']} a {item['Engine HP']} chevaux et {item['Engine Cylinders']} cylindres")


cars = client.cars.info

add_car = st.checkbox('ajouter une voiture à la base données')
if add_car:
    constructeur = st.text_input('Constructeur :')
    model = st.text_input('Modèle :')
    cylindres = st.text_input('Cylinders :')
    sub = st.button('Submit')
    if sub:
        cars.insert_one({'Make': constructeur, 'Model': model,
                        'Engine Cylinders': cylindres})
