#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import streamlit as st 
from sklearn.linear_model import LinearRegression
from pickle import dump
from pickle import load

st.title('Model Deployment: Linear Regression')

st.sidebar.header('User Input Parameters')

def user_input_features():
    engine_size =st.sidebar.number_input('Insert engine Size')
    cylinders = st.sidebar.number_input('Insert no. of Cylinders')
    fl_con_comb_l_100km = st.sidebar.number_input('Insert Fuel Consumption Combined (l/100km)')
    fl_con_comb_mpg = st.sidebar.number_input('Insert Fuel Consumption Combined (mpg)')
    make_BUGATTI = st.sidebar.selectbox('car make BUGATTI',('1','0'))
    make_SRT = st.sidebar.selectbox('car make SRT',('1','0'))
    make_ROLLS_ROYCE = st.sidebar.selectbox('car make ROLLS-ROYCE',('1','0'))
    make_LAMBORGHINI = st.sidebar.selectbox('car make LAMBORGHINI',('1','0'))
    make_BENTLEY = st.sidebar.selectbox('car make BENTLEY',('1','0'))
    vehicle_class_VAN_PASSENGER = st.sidebar.selectbox('vehicle class VAN - PASSENGER',('1','0'))
    vehicle_class_VAN_CARGO = st.sidebar.selectbox('vehicle class VAN - CARGO',('1','0'))
    vehicle_class_PICKUP_TRUCK_STANDARD = st.sidebar.selectbox('vehicle class PICKUP TRUCK - STANDARD',('1','0'))
    vehicle_class_SUV_STANDARD = st.sidebar.selectbox('vehicle class SUV - STANDARD',('1','0'))
    vehicle_class_TWO_SEATER = st.sidebar.selectbox('vehicle class TWO-SEATER',('1','0'))
    transmission_A =  st.sidebar.selectbox('Automatic transmission',('1','0'))
    transmission_AM =  st.sidebar.selectbox('Automated manual transmission',('1','0'))
    transmission_AS =  st.sidebar.selectbox('Automatic with select shift transmission',('1','0'))
    transmission_AV =  st.sidebar.selectbox('Continuously variable transmission',('1','0'))
    transmission_M =  st.sidebar.selectbox('Manual transmission',('1','0'))
    fuel_type_D =  st.sidebar.selectbox('Diesel',('1','0'))
    fuel_type_E =  st.sidebar.selectbox('Ethanol (E85)',('1','0'))
    fuel_type_X =  st.sidebar.selectbox('Regular gasoline',('1','0'))
    fuel_type_Z =  st.sidebar.selectbox('Premium gasoline',('1','0'))
    input_data = pd.DataFrame({
        'engine_size': [engine_size],
        'cylinders': [cylinders],
        'fl_con_comb(l/100km)': [fl_con_comb_l_100km],
        'fl_con_comb(mpg)': [fl_con_comb_mpg],
        'make_BUGATTI': [make_BUGATTI],
        'make_SRT': [make_SRT],
        'make_ROLLS-ROYCE': [make_ROLLS_ROYCE],
        'make_LAMBORGHINI': [make_LAMBORGHINI],
        'make_BENTLEY': [make_BENTLEY],
        'vehicle_class_VAN - PASSENGER': [vehicle_class_VAN_PASSENGER],
        'vehicle_class_VAN - CARGO': [vehicle_class_VAN_CARGO],
        'vehicle_class_PICKUP TRUCK - STANDARD': [vehicle_class_PICKUP_TRUCK_STANDARD],
        'vehicle_class_SUV - STANDARD': [vehicle_class_SUV_STANDARD],
        'vehicle_class_TWO-SEATER': [vehicle_class_TWO_SEATER],
        'transmission_A': [transmission_A],
        'transmission_AM': [transmission_AM],
        'transmission_AS': [transmission_AS],
        'transmission_AV': [transmission_AV],
        'transmission_M': [transmission_M],
        'fuel_type_D': [fuel_type_D],
        'fuel_type_E': [fuel_type_E],
        'fuel_type_X': [fuel_type_X],
        'fuel_type_Z': [fuel_type_Z]
    })
    
    features = pd.DataFrame(input_data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('linear_model.sav', 'rb'))



if st.button('Predict'):
    prediction = loaded_model.predict(df)
    st.write('Predicted CO2 Emissions:', prediction)



# In[ ]:




