import streamlit as st
from PIL import Image

def main():
    
    st.title("Emissions per capita and analyzing graphs.")

    # Displaying text
    st.write("""
    This pages focuses on the graphical analysis of the emissions per capita for a few countries.
    """)
    st.markdown('---')


    st.write("""
    As you can see here, we decided to check the emissions per capita for a few countries.
    We decided to pick countries that were interesting to us, and we decided to compare them.
    First of all we picked Denmark and Greece for our first analysis.         
             
    """)
    # Displaying images
    image_path = "Media/DenmarkPerCapita.png"
    image = Image.open(image_path)
    st.image(image, caption="Denmark Per Capita", use_column_width=True)

    image_path = "Media/GreecePerCapita.png"
    image = Image.open(image_path)
    st.image(image, caption="Greece Per Capita", use_column_width=True)

    
    st.write("""
    It was a result we were happy to see, as it showcases that both countries are on a decline in overall emissions per capita.
    We didn't stop here however, as we continued at a greater scale, and we decided to bring a big country into the mix.
    """)

    # more images
    another_image_path = "Media/PerCapitaComparisonWesternCountries.png"  # Update this path as well
    another_image = Image.open(another_image_path)
    st.image(another_image, caption="Per Capita with USA and Bulgaria.", use_column_width=True)

    st.write("""
             
    This showed us that even a larger country like the USA, despite being #2 on Total emissions, are also on a decline on per capita emissions.
    We decided to go even further and look at the top countries in the world when it comes to total emission and then see how their Per Capita looks like.
             
    """)


    another_image_path = "Media/PerCapitaComparisonTopCountries.png"  # Update this path as well
    another_image = Image.open(another_image_path)
    st.image(another_image, caption="Per Capita with Top countries", use_column_width=True)

    st.write("""This shows us many things, one that many developed and/or Western countries have a high per capita emission, but that they are slowly starting to fall.
             However, Eastern countries that are less developed or rather, as a more gracious way to say it: countries that have a large areas of their population in poverty, have a lower per capital emission but are steadily rising.
             
             """)
if __name__ == "__main__":
    main()