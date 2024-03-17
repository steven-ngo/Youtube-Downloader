import streamlit as st
from pytube import YouTube
import time

# App description
st.markdown('''
# Youtube Downloader
- Source Code: https://github.com/steven-ngo/Youtube-Downloader
- Language: `Python`
- Libraries: `streamlit` `pytube`
''')
st.write('---')

def complete_func( stream,file_path):
    st.success("Done.")

def progress_func( stream, chunk,bytes_remaining):
    total_size = stream.filesize

    percentage_of_completion = round((total_size - bytes_remaining) / total_size * 100)

    my_bar.progress(percentage_of_completion, text=progress_text)


path = st.text_input('Enter URL of any youtube video')

option = st.selectbox(
    'Select type of download',
    ('audio', 'highest_resolution', 'lowest_resolution'))

if st.button("download") and path: 
    try:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        video_object =  YouTube(path,on_progress_callback=progress_func,on_complete_callback=complete_func)
        
        st.write("🎥 Video Title: " + str(video_object.title))

        if option=='audio':
            video_object.streams.get_audio_only().download() 

        elif option=='highest_resolution':
            video_object.streams.get_highest_resolution().download()

        elif option=='lowest_resolution':
            video_object.streams.get_lowest_resolution().download()
        
        my_bar.empty()
    except Exception:
        st.error("Error")

if st.button("view") and path: 
    try:
        st.video(path) 
    except Exception:
        st.error("Error")

