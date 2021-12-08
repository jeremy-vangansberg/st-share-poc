import streamlit as st
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://jvsimplon:1234@cluster0.njzrg.mongodb.net/cars?retryWrites=true&w=majority')


@st.cache(ttl=100)
def get_data():
    db = client.cars
    items = db.info.find()
    items = list(items)  # make hashable for st.cache
    return items


items = get_data()

# st.write(items)

for item in items[0:10]:
    if item['Make'] == 'BMW':
        st.write(
            f"La {item['Make']} {item['Model']} a {item['Engine HP']} chevaux et {item['Engine Cylinders']}")


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
