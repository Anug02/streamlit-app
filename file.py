import pandas as pd
import streamlit as st
from PIL import Image

st.title('File Uploading.')

# 1. Image
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload Image' ,type =['png','jpg','jpeg'])

if img_file is not None:
    st.write(type(img_file))

    file_details ={'file_name': img_file.name, 'file_type':img_file.type,
                'file_size':img_file.size}

    st.write(file_details)
    st.image(Image.open(img_file))

#2.Audio
st.subheader('1. Uploading an Audio')
audio_file = st.file_uploader('Upload Audio' ,type =['wav','mp3'])

if audio_file is not None:
    st.write(type(img_file))

    file_details ={'file_name': audio_file.name, 'file_type':audio_file.type,
                'file_size':audio_file.size}

    st.write(file_details)
    st.write(audio_file)
    st.audio(audio_file)

#3. Video
st.subheader('3. Uploading an Video')
video_file =st.file_uploader('Upload Video',type =['mov','mp4'])
if video_file is not None:
    file_details ={'file_name': audio_file.name, 'file_type':audio_file.type,
                'file_size':audio_file.size}
    
    st.write(video_file)
    st.video(video_file)

#4. Upload an csv file.
st.subheader('4.Upload an CSV file.')


   
