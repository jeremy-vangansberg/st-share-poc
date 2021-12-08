import streamlit as st
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://jvsimplon:1234@cluster0.njzrg.mongodb.net/cars?retryWrites=true&w=majority')


def get_data():
    db = client.cars
    items = db.info.find()
    items = list(items)  # make hashable for st.cache
    return items


items = get_data()
for item in items[0:10]:
    st.write(f"{item['Model']} has a :{item['Engine HP']}:")
