import streamlit as st
from joblib import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

co2mt_df = pd.read_csv('data/GCB2022V27_MtCO2_flat.csv')

def main():
    st.title("CO2 Emissions Prediction by Country")

    countries = ['USA', 'China', 'India', 'Global'] 

    def predict_emissions_for_country(year, country, model):
        year_array = np.array([[year]])
        prediction = model.predict(year_array)
        return prediction[0][0]

    # User selects a country
    selected_country = st.selectbox("Select a country:", countries)

    # User inputs a year
    year = st.number_input("Enter a year to predict emissions:", min_value=1990, max_value=2100, value=2020, step=1)

    if st.button("Predict Emissions"):
        # Load the model for the selected country
        model_path = f'Models/linear_regression_model_{selected_country}.joblib'
        model = load(model_path)
        
        # Predict emissions for the specified year and country
        predicted_emissions = predict_emissions_for_country(year, selected_country, model)
        st.write(f"The predicted CO2 emissions for {selected_country} in the year {year} are: {predicted_emissions:.2f} MtCO2.")
        
        # Filter the DataFrame for the selected country's historical data
        historical_data = co2mt_df[(co2mt_df['Country'] == selected_country) & (co2mt_df['Year'] >= 1950)]

        
        # Plotting the historical data
        plt.figure(figsize=(10, 6))
        plt.scatter(historical_data['Year'], historical_data['Total'], color='blue', label='Historical Data')
        
        # Adding the predicted point
        plt.scatter([year], [predicted_emissions], color='red', label='Predicted Value')
        
        plt.title(f"CO2 Emissions for {selected_country}")
        plt.xlabel("Year")
        plt.ylabel("Total CO2 Emissions (MtCO2)")
        plt.legend()
        
        st.pyplot(plt)

if __name__ == "__main__":
    main()
