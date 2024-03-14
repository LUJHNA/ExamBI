#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_option_menu import option_menu

import json
import requests
import pandas as pd
import numpy as np


from io import StringIO
import langdetect
from langdetect import DetectorFactory, detect, detect_langs
from PIL import Image

st.set_page_config(
    page_title="Business Intelligence Exam",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:tdi@cphbusiness.dk',
        'About': "https://docs.streamlit.io"
    }
)

st.sidebar.header("Try Me!", divider='rainbow')
# st.sidebar.success("Select a demo case from above")


banner = """
    <body style="background-color:yellow;">
            <div style="background-color:#385c7f ;padding:10px">
                <h2 style="color:white;text-align:center;">Business Intelligence Exam</h2>
            </div>
    </body>
    """

st.markdown(banner, unsafe_allow_html=True)


st.markdown(
    """
### Hello and welcome to our Business Intelligence Exam's streamlit visualization.
We would like to do a little presentation including answering our research questions with our models and graph analysis.:
-Which countries are producing the most emission?
-Which countries are producing most emission per capita?
-How have global emissions changed over the past 70 years?
-Which models can we use and fit the best for our datasets?




""")
st.markdown("---")




