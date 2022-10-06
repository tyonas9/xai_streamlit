from dis import dis
from http import server
import openslide
import streamlit as st
import pandas as pd
import numpy as np
import time
import os
from pathlib import Path
from PIL import Image

def upload_image(image_file):
    if image_file is not None:
        # see image details
        file_details = {"FileName": image_file.name,
                        "FileType": image_file.type}
        #Saving image file in a WSI folder
        save_img_path = os.path.join("WSI", image_file.name)
        with open(save_img_path, "wb") as f:
            f.write(image_file.getbuffer())
        st.success("WSI image has been uploaded")
    return save_img_path
def display_image(save_img_path):
    slide_path = save_img_path
    #slide_path = str(os.path.join('WSI', file_name))
    #file_type = file_name.split('.')[-1]
    file_type = 'svs'
    if file_type == 'svs':
        slide = openslide.open_slide(str(slide_path))
        slide_dims = slide.level_dimensions
        st.write('slide dimensions: ', slide_dims)
        disp_size = slide_dims[-1]
        img = slide.read_region((0, 0), level=0, size=disp_size)
    elif file_type in ['jpg', 'jpeg', 'png']:
        img = Image.open(slide_path)
        img.load()
        print(f"size of slide: {img.size}")
    print(type(img))
st.markdown("## Welcome to Mitosis Detector :balloon:")
with st.sidebar:
    #st.markdown("# Main page :balloon:")
    st.subheader("Upload your Image")
    image_file = st.file_uploader("Upload a Image", type=["svs", "jpeg"])
    #file_name = image_file.name
    #st.write(file_name)
save_img_path = upload_image(image_file)
display_image(save_img_path)














