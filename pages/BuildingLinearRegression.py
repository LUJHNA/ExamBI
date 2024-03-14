import streamlit as st
from PIL import Image

def main():
    
    st.title("Building the model")

    # Displaying text
    st.write("""
    This page focuses on how we built our prediction model and how we tested it.
    We started out by choosing Linear Regression as we felt it fit our dataset the best.
    """)

    # Displaying an image
    image_path = "Media/StartOfModel.png"  
    image = Image.open(image_path)
    st.image(image, caption="Starting The Model", use_column_width=True)

    st.write("""
    We continued by doing a scatterplot of our data, to showcase before the model was built.
    """)

    # Displaying another image
    image_path = "Media/GlobalEmissions.png"  
    another_image = Image.open(image_path)
    st.image(another_image, caption="Scatterplot of Global Emissions", use_column_width=True)

    st.write("""
    Then we continued to build the model and splitting the data into training and testing data.          
""")
    image_path = "Media/SplittingForTestSize.png"  
    another_image = Image.open(image_path)
    st.image(another_image, caption="Splitting the data 85/15", use_column_width=True)

    st.write("""
    Then we fit the model and saved it.
             """)
    
    image_path = "Media/FittingAndSaving.png"
    another_image = Image.open(image_path)
    st.image(another_image, caption="Fitting and saving the model", use_column_width=True)

    st.write("""
    Then we tested the prediction model and visualized it with the scatterplot from before.
             """)
    
    image_path = "Media/VisualizingPredictionWithData.png"
    another_image = Image.open(image_path)
    st.image(another_image, caption="Visualizing the prediction with the data", use_column_width=True)

    st.write("""
    Then finally we tested out the model to see if it gave an expected/accepted prediction within reason.
             
             """)
    image_path = "Media/TestingPrediction.png"
    another_image = Image.open(image_path)
    st.image(another_image, caption="Testing the prediction", use_column_width=True)

    image_path = "Media/PredictedFutureEmission.png"
    another_image = Image.open(image_path)
    st.image(another_image, caption="Scatterplot of predicted future.", use_column_width=True)

    st.write("""
    This is how we built and tested our model. It looks accurate from the scatterplot, taking previous data into account.
    
             
             """)


if __name__ == "__main__":
    main()