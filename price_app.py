# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:43:36 2023

@author: Rajat
"""
import streamlit as st
import pickle
from PIL import Image

#loading the save model

loaded_model = pickle.load(open("trained_model.sav", 'rb'))

with open("manufacturer_encoder.pkl", 'rb') as f:
    Manufacturer_le = pickle.load(f)

with open("model_encoder.pkl", 'rb') as f:
    Model_le = pickle.load(f)
    
with open("category_encoder.pkl", 'rb') as f:
    Category_le = pickle.load(f)

with open("fuel_type_encoder.pkl", 'rb') as f:
     Fuel_type_le = pickle.load(f)

with open("gear_box_encoder.pkl", 'rb') as f:
    Gear_box_type_le = pickle.load(f)

with open("drive_wheels_encoder.pkl", 'rb') as f:
    Drive_wheels_le = pickle.load(f)

with open("drive_wheels_encoder.pkl", 'rb') as f:
    Drive_wheels_le = pickle.load(f)
    
with open("leather_interior_encoder.pkl", 'rb') as f:
    Leather_interior_le = pickle.load(f)
    
with open("wheel_encoder.pkl", 'rb') as f:
    Wheel_le = pickle.load(f)
def transform_with_unseen_label(encoder, labels):
    unseen_labels = set(labels) - set(encoder.classes_)
    if unseen_labels:
        encoder.classes_ = sorted(list(encoder.classes_) + list(unseen_labels))
    return encoder.transform(labels)
    
if 'user_data' not in st.session_state:
    st.session_state.user_data = {'users': []}
if 'user_data' not in st.session_state:
    st.session_state.user_data = {'users': []}

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user_data = st.session_state.user_data
        if any(user['username'] == username and user['password'] == password for user in user_data['users']):
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.write("Welcome, " + username)
            display_car_prediction_form()

def signup():
    st.title("Sign Up")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        # Add your signup logic here
        user_data = st.session_state.user_data
        user_data['users'].append({'username': new_username, 'password': new_password})
        st.success("Sign Up successful! Please login.")
def display_car_prediction_form():
    st.title("Car Price Predictor")
    image = Image.open("C:/Project STR/753302.jpg")
    st.image(image, '')
    
    manufacturer_options = ['LEXUS','CHEVROLET','HONDA','FORD','HYUNDAI','TOYOTA','MERCEDES-BENZ','OPEL','PORSCHE','BMW', 'JEEP','VOLKSWAGEN','AUDI','RENAULT','NISSAN', 'SUBARU','DAEWOO','KIA',
     'MITSUBISHI','SSANGYONG','MAZDA','GMC','FIAT','INFINITI','ALFA ROMEO','SUZUKI','ACURA', 'LINCOLN','VAZ',
     'GAZ','CITROEN','LAND ROVER','MINI','DODGE','CHRYSLER','JAGUAR', 'ISUZU','SKODA', 'DAIHATSU','BUICK', 'TESLA',
     'CADILLAC', 'PEUGEOT','BENTLEY','VOLVO','სხვა','HAVAL', 'HUMMER','SCION','UAZ', 'MERCURY','ZAZ','ROVER','SEAT',
     'LANCIA', 'MOSKVICH','MASERATI', 'FERRARI', 'SAAB','LAMBORGHINI','ROLLS-ROYCE','PONTIAC','SATURN','ASTON MARTIN','GREATWALL']
    
    model_options = [
        'RX 450', 'Equinox', 'FIT', 'Escape', 'Santa FE', 'Prius', 'Sonata', 'Camry', 'RX 350', 'E 350',
        'Transit', 'Vectra', 'CHR', 'Elantra', 'RX 400', 'E 220', 'GX 470', 'Highlander', 'Vito', 'Cayenne', 'X5',
        'Grand Cherokee', 'CHR Limited', 'H1', 'Jetta', 'Tacoma', 'Prius C', 'Aqua', 'Escape Hybrid', 'Civic', 'Q7',
        'Megane 1.5CDI', 'E 300', 'Q5', 'C 180', 'GLA 250', 'Juke', '535', 'Cruze LT', 'Fusion', 'VOXY', 'A 160',
        'Tucson', 'Vitz', 'Captiva', 'Mustang', 'ML 350', 'Yaris', 'Cr-v', 'Cruze', 'Orlando', 'GL 63 AMG', '520 Vanos',
        'Forester', 'Lacetti', '428 Sport Line', 'Patrol', 'E 320', 'Genesis', '911', 'GX 460', 'Sprinter', 'Focus SE',
        'Picanto', '328', 'Explorer', 'Airtrek', 'E 500 AMG', 'Lancer', 'Korando', 'Clio', '616', 'C 220', 'Serena',
        'Maxima', 'RAV 4', 'Pajero', 'Volt', 'TERRAIN', '208', 'Hr-v EX', '500', 'Legacy', 'Elantra sport limited',
        'Sienna', 'A 170', 'NX 300', 'REXTON', 'Carnival grand', 'QX60', 'Passat', 'E 240 E 240', '1000', '50', 'C 250',
        'Vitz funkargo', '325', 'A6', 'Pathfinder', 'Delica', 'Golf', 'Vaneo', 'Camry Se', 'Patrol Y60', 'A7', 'I30',
        'Altima', '147', 'Grand Vitara', 'CT 200h', 'Panamera', 'Veloster', 'RAV 4 XLE Sport', 'Sienta', 'CLS 550',
        'Avalanche', 'Avalon LIMITED', 'Cerato K3', 'CX-7', 'Astra G', 'Ist', 'Corolla', 'Rogue', 'MPV', '530', 'GS 350',
        'Sharan', 'Tiida', 'C 300', 'Actyon', 'Tundra', 'Elgrand', 'C 350', 'CLS 500', 'S 350', 'RAV 4 Le', 'Zafira',
        'Vectra b', 'C 200', 'Astra', '323', 'E 350 ამგ', 'CLK 320', 'Avalon', 'ML 250', '330', 'A7 Prestige', 'Colt Lancer',
        '318', 'Outlander', 'Camry SE', 'E 200', 'GLE 350', 'Malibu', 'TL', 'Insight', 'Stream', 'I', 'GTI', 'Colt', 'Pajero Mini',
        'C-MAX', '750', 'RAV 4 s p o r t', 'E 250', 'Outback', 'GLC 300', 'Navigator', 'Fusion Titanium', 'Jimny', 'Aveo', 'X6',
        'Aqua S', '1111', 'NX 200', '32214', 'Laguna', 'Optima', 'Shuttle', 'C 240', 'Land Cruiser Prado', '328 Xdrive', 'E 240',
        'Taurus', 'Twingo', '535 M PAKET', 'S 500']
    
    category_options = ['Jeep',
     'Hatchback',
     'Sedan',
     'Microbus',
     'Goods wagon',
     'Universal',
     'Coupe',
     'Minivan',
     'Cabriolet',
     'Limousine',
     'Pickup']
    fuel_options = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
    gear_options = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
    drive_options = ['4x4', 'Front', 'Rear']
    wheel_options = ['Left wheel', 'Right-hand drive']
    interior_options = ['Yes', 'No'] 
    
    
    Manufacturer = st.selectbox("Select the Car Manufacturer", manufacturer_options)
    Model = st.selectbox("Select the Car Model:", model_options)
    Year = st.text_input("Enter the Year of the Car:")
    Category = st.selectbox("Select the Car Category:", category_options)
    Interior = st.selectbox("Want Leather Interior yes or no:", interior_options)
    Fuel = st.selectbox("Enter the Car's Fuel type:", fuel_options)
    Gear_box = st.selectbox("Enter the type of gear box in the car:", gear_options)
    Mileage = st.text_input("Enter the Mileage of the car in kilometers:")
    Cylinders = st.slider("Enter the number of Cylinders in the car:",min_value=1.0, max_value=16.0, step=1.0, value=4.0, format="%f")
    Engine_volume = st.slider("Enter the Engine Volume of the car in liters:",min_value=0.0, max_value=7.5, step=0.1, value=2.0, format="%f")
    Doors = st.slider("Enter the number of Doors on the car (if 4-5 then 1 or 2-5 then 0):",min_value = 0, max_value= 3, step= 1, value= 2, format="%d")
    Drive = st.selectbox("Select the Drive wheels of the car:",drive_options)
    Wheel = st.selectbox("Select the wheel of the car:",wheel_options)
    Airbags = st.slider("Enter the Airbags in the car:",min_value=0.0, max_value=16.0, step=2.0, value=4.0, format="%f")
    
    
    if st.button("Predict Car Price"):
        Manufacturer = transform_with_unseen_label(Manufacturer_le, [Manufacturer])
        Model = transform_with_unseen_label(Model_le, [Model])
        Category = transform_with_unseen_label(Category_le, [Category])
        Fuel = transform_with_unseen_label(Fuel_type_le, [Fuel])
        Gear_box = transform_with_unseen_label(Gear_box_type_le, [Gear_box])
        Drive = transform_with_unseen_label(Drive_wheels_le, [Drive])
        Wheel = transform_with_unseen_label(Wheel_le, [Wheel])
        Interior = transform_with_unseen_label(Leather_interior_le, [Interior])
        car_features = [Manufacturer, Model, Year, Category, Interior, Fuel, Gear_box, Mileage, Cylinders, Engine_volume, Doors, Drive, Wheel, Airbags]
        predicted_price = loaded_model.predict([car_features])
        st.write(f"Estimated Car Price: ${predicted_price[0]:.2f}")
        
def main():
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        option = st.radio("Choose an option", ("Login", "Sign Up"))
        if option == "Login":
            login()
        else:
            signup()
    else:
        display_car_prediction_form()

if __name__ == "__main__":
    main()
