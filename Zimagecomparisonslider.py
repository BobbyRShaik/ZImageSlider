#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import leafmap
import requests
from PIL import Image
import os
from tkinter import filedialog
from tkinter import Tk
import streamlit as st
import streamlit.components.v1 as components

def is_valid_image_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            # Check if the URL points to a valid image
            image = Image.open(requests.get(url, stream=True).raw)
            return True
        else:
            return False
    except Exception as e:
        return False

def get_local_image_path():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=(("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")))
    return file_path

def get_image_choice():
    while True:
        try:
            choice = input("Do you want to import an image via URL or from your local machine? (URL/local): ").lower()
            if choice == 'url':
                url = input('Enter the URL for the image: ')
                if is_valid_image_url(url):
                    return url
                else:
                    print("Invalid image URL. Please enter a valid image URL.")
            elif choice == 'local':
                file_path = get_local_image_path()
                if file_path:
                    return file_path  # Return the local file path
                else:
                    print("Invalid local image file path. Please select a valid file.")
            else:
                print("Invalid choice. Please enter 'URL' or 'local'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

img1 = get_image_choice()
img2 = get_image_choice()

if img1 and img2:
    leafmap.image_comparison(
        img1,
        img2,
        label1='Image 1',
        label2='Image 2',
        starting_position=50,
        out_html='image_comparison.html'
    )
    HtmlFile = open("image_comparison.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code,width=600,height=600)
else:
    print("Invalid or no image files selected.")


# In[ ]:




