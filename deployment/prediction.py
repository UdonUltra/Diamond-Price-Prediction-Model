import streamlit as st
import pandas as pd
import pickle


def user_input():
    carat = st.number_input("Enter Carat Value", value=5.2)
    cut = st.selectbox('Choose Cut Quality',('Ideal', 'Premium', 'Good', 'Very Good', 'Fair'))
    color = st.selectbox('Choose Color Quality',('E', 'I', 'J', 'H', 'F', 'G', 'D'))
    clarity = st.selectbox('Choose Clarity Quality',('SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'))
    depth = st.number_input("Enter Diamond Depth Percentage", value=80.0)
    table = st.number_input("Enter Diamond Table Percentage", value=90.0)
    x = st.number_input("Enter Diamond Lenght in mm", value=11.0)
    y = st.number_input("Enter Diamond Width in mm", value=60.0)
    z = st.number_input("Enter Diamond Depth in mm", value=32.0)
    
    
    data = {
        'carat': carat,
        'cut': cut,
        'color': color,
        'clarity': clarity,
        'depth': depth,
        'table': table,
        'x': x,
        'y': y,
        'z': z
        
    }
    features = pd.DataFrame(data, index=[0])
    return features

def app():
    st.title('Diamond Price PREDICTION')
    # Getting user input
    input_df = user_input()

    # Load model and other files
    with open("model.pkl", "rb") as file_3:
        model = pickle.load(file_3)

    # Predict Score
    if st.button('Predict Now'):
        predicted_score = model.predict(input_df)
        st.write(f"Predicted Price: {predicted_score[0]:.2f} USD")
    else:
        st.write('Predicted Price:')
    

app()
