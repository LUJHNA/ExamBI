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
### Problem formulation
Our project aims to analyze global emissions, using datasets which has several years of data to develop predictive models that forecast the potential increases/decreases in emissions in the future. 
This research is crucial as it addresses the direct impact of emissions on the future of humanity, highlighting the urgency for immediate change. 
The expected and hoped positive outcome from this project is a large awakening not only among individuals but more importantly among governments worldwide, motivating a hopeful change in how we live, 
so that the planet and future generations may live and ensure the survival of the human race.


## Title:
The past, present and potential future of emissions.


""")
st.markdown("---")




