
# savin a model
# import pickle pickle_out = open("classifier.pkl", mode = "wb")
# pickle.dump(model, pickle_out)
# pickle_out.close()

import streamlit as st
import pandas as pd 
import pickle as pkl
import numpy as np

st.title("Automobile price predictions")

# taking inputs from the user for predictor/independent variable to later feed to model to make prediction

# 2 columns for fuel and transmission type
col1, col2 = st.columns(2)
with col1:
    fuel_type = st.selectbox(
    'Fuel Type',
    ('Diesel', 'Petrol', 'CNG', 'LPG','Electric'))
with col2:
    transmission = st.radio(
    "",
    ('Manual', 'Electric')
    )

# 2 columns for car_seat_count and 
col1, col2 = st.columns(2)
with col1:
    seats = st.slider(
    'Number of seats',
    2, 7)
with col2:
    engine = st.slider(
        'Engine power', 500,5000, step = 100
    )


# Encoding the data before sending it to backend
encode_dict = {'Fuel Type': {'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG': 4, 'Electric': 5},
'transmission': {'Manual':1, 'Automatic':2}
}


# sending the data to model
def model_pred(fuel_type,transmission,engine, seats):

    # reading model
    # for working in local machine:
    # with open ('Automobile-price-prediction-/car_pred','rb') as file:
    with open ('car_pred','rb') as file: # fro web app
        reg_model = pkl.load(file)

    # test data info
    x_test = [[2018.0,1,40000,fuel_type, transmission,18.0, engine, 85, seats]]
    '''
    reshape error  (occurs specially in line regression model), while providing data to model. 
    That is why here x_test is converted to 2D array
    '''
    
    # returning the predictions
    return reg_model.predict(x_test)

if st.button('Predict'):
    fuel_type = encode_dict['Fuel Type'][fuel_type]
    transmission = encode_dict['transmission'][transmission]

    price = model_pred(fuel_type, transmission, engine,seats)

    st.write(f"The estimated price for automobile with your desired features: {np.round(price,3)} Lakhs")
else:
    st.write(
        'HIT the predict button'
    )