import streamlit as st
from PIL import Image

def main():
    
    st.title("Emissions and analyzing graphs.")

    # Displaying text
    st.write("""
    This page focuses on graphical analysis of total emissions for a few selected countries and then top countries.
    We started out searching our own countries, as they are interesting to us.
    """)

    # Displaying an image
    image_path = "Media/DenmarkTotalEmission.png"  # Update this to the path of your image
    image = Image.open(image_path)
    st.image(image, caption="Denmark total emissions", use_column_width=True)

    image_path = "Media/GreeceTotalEmission.png"  # Update this to the path of your image
    image = Image.open(image_path)
    st.image(image, caption="Greece total emissions", use_column_width=True)

    # Add as many sections as you like
    st.write("""
    This was nice to see, that our main countries of interest were on a decline of total emissions, showing that we are on the right track,
    when it comes to lowering our emissions and being more resonsible for our future.
             
    We didn't stop here however, as we continued at a greater scale, and we decided to bring a big country into the mix.
    """)

    # Displaying another image
    image_path = "Media/TotalEmissionComparisonWesternCountries.png"  # Update this path as well
    another_image = Image.open(image_path)
    st.image(another_image, caption="With USA and Bulgaria", use_column_width=True)

    st.write("""
    This, well... this was a bit of a shocker. We knew that the USA was a big country, we knew that they were #2 in the world when it comes to total emissions, but we didn't expect to the actual difference to be this massive.
    It's one thing to look at numbers, and another to visualize it like this.
    You can't even see our countries on the graph, almost, it looks like mistaken data almost.
             
    This piqued our interest, and we decided to compare USA with the other top countries in the world when it comes to total emissions.            
""")
    image_path = "Media/TotalEmissionComparisonTopCountries.png"  # Update this path as well
    another_image = Image.open(image_path)
    st.image(another_image, caption="Top countries for total emissions.", use_column_width=True)

    st.write("""This puts a whole new perspective to it all. Again, we knew China was #1 in total emissions, but seeing it like this on a graph was crazy.
             Especially when you consider how explosively they have increased their emissions over the last 20 years.
             Their population are 5 times that of the US, but their emissions are 2.5 times that of the US. However that might chance sooner rather than later if China doesn't halt their borderline crazy emissions.
             
             """)


if __name__ == "__main__":
    main()