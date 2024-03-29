#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Image comparison slider that displays two pcitures side by side based on files the user uploads in pairs

import streamlit as st  # Import the Streamlit library for building web applications.
import streamlit.components.v1 as components  # Import components from Streamlit to embed custom HTML.
import pandas as pd  # Import the Pandas library for data manipulation.
from io import StringIO  # Import StringIO to work with string-based file data.
import leafmap  # Import the leafmap library for geospatial visualization.

# Define a function named ImageCompare.
def ImageCompare():
    if k == 1:
        print(k)
        # Check if img1 and img2 are provided.
        if img1 and img2:
            # Use the leafmap library to create an image comparison visualization.
            leafmap.image_comparison(
                img1,
                img2,
                label1='Image 1',
                label2='Image 2',
                starting_position=50,
                out_html='image_comparison.html'
            )
            # Open the HTML file generated by leafmap.
            HtmlFile = open("image_comparison.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            # Embed the HTML code in the Streamlit app.
            components.html(source_code, width=600, height=600)
        else:
            print("Invalid or no image files selected.")

# Create a file uploader in the Streamlit app that allows multiple file selections.
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

i = 0  # Initialize a counter for image file selection.
k = 0  # Initialize a flag variable to indicate if image files have been selected.

# Loop through the uploaded files.
for uploaded_file in uploaded_files:
    k = 1  # Set the flag to indicate that at least one image file has been selected.
    
    if i == 0:
        img1 = uploaded_file.name  # Store the name of the first image.
        i = i + 1
        with open(uploaded_file.name, 'wb') as f:
            f.write(uploaded_file.getbuffer())  # Write the first image file.
    else:
        img2 = uploaded_file.name  # Store the name of the second image.
        with open(uploaded_file.name, 'wb') as f:
            f.write(uploaded_file.getbuffer())  # Write the second image file.
        ImageCompare()  # Call the ImageCompare function to perform image comparison.

