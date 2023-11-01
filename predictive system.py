# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:43:36 2023

@author: Rajat
"""
import streamlit as st
import pickle

#loading the save model

loaded_model = pickle.load(open("trained_model.sav", 'rb'))

with open("C:/Project STR/manufacturer_encoder.pkl", 'rb') as f:
    Manufacturer_le = pickle.load(f)

with open("C:/Project STR/model_encoder.pkl", 'rb') as f:
    Model_le = pickle.load(f)
    
with open("C:/Project STR/category_encoder.pkl", 'rb') as f:
    Category_le = pickle.load(f)

with open("C:/Project STR/fuel_type_encoder.pkl", 'rb') as f:
     Fuel_type_le = pickle.load(f)

with open("C:/Project STR/gear_box_encoder.pkl", 'rb') as f:
    Gear_box_type_le = pickle.load(f)

with open("C:/Project STR/drive_wheels_encoder.pkl", 'rb') as f:
    Drive_wheels_le = pickle.load(f)
    

st.title("Car Price Predictor")

Manufacturer = st.text_input("Enter the Car Manufacturer Name:")
Model = st.text_input("Enter the Car's Model Name:")
Year = st.text_input("Enter the Year of the car:")
Category = st.text_input("Enter the Category of the car:")
Interior = st.number_input("Enter leather interior given (if yes then 1 or no then 0):")
Fuel = st.text_input("Enter the Car's Fuel type:")
Gear_box = st.text_input("Enter the type of gear box in the car:")
Mileage = st.text_input("Enter the Mileage of the car in kilometers:")
Cylinders = st.number_input("Enter the number of Cylinders in the car(default is 4.0):")
Engine_volume = st.number_input("Enter the Engine Volume of the car in liters(minimum 1 to maximum 5):")
Doors = st.number_input("Enter the number of Doors on the car (if 4-5 then 1 or 2-5 then 0):")
Drive = st.text_input("Enter the Drive wheels of the car:")
Wheel = st.number_input("Enter the wheel of the car (if left then 0 or right then 1):")
Airbags = st.number_input("Enter the Airbags in the car:")


if st.button("Predict Car Price"):
    Manufacturer = Manufacturer_le.transform([Manufacturer])
    Model = Model_le.transform([Model])
    Category = Category_le.transform([Category])
    Fuel = Fuel_type_le.transform([Fuel])
    Gear_box = Gear_box_type_le.transform([Gear_box])
    Drive = Drive_wheels_le.transform([Drive])
    car_features = [Manufacturer, Model, Year, Category, Interior, Fuel, Gear_box, Mileage, Cylinders, Engine_volume, Doors, Drive, Wheel, Airbags]
    predicted_price = loaded_model.predict([car_features])
    st.write(f"Estimated Car Price: ${predicted_price[0]:.2f}")