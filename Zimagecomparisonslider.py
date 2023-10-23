import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import StringIO
import leafmap

def ImageCompare():
    if k==1:
        print(k)
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


uploaded_files = st.file_uploader("Choose a file",accept_multiple_files=True)
i=0
k=0
for uploaded_file in uploaded_files: 
    k=1  
    if i==0:
        img1=uploaded_file.name
        i=i+1
        with open(uploaded_file.name,'wb') as f:
            f.write(uploaded_file.getbuffer())
    else:
        img2=uploaded_file.name
        with open(uploaded_file.name,'wb') as f:
            f.write(uploaded_file.getbuffer())
        ImageCompare()




#if uploaded_file is not None:
 #   f1=uploaded_file.name
    # To read file as bytes:
    
  #  bytes_data = uploaded_file.getvalue()
   # st.write(bytes_data)

    # To convert to a string based IO:
  #  stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
   # st.write(stringio)

    # To read file as string:
  #  string_data = stringio.read()
   # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
   # dataframe = pd.read_csv(uploaded_file)
   # st.write(dataframe)

