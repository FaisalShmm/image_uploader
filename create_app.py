import streamlit as st
import time

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"
col1,col2,col3=st.columns([1,2,1])

col1.markdown("# Welcome to Photo Uploader app")
col1.markdown("Here i have created a virtual environment and used streamlit with python for this functionality")
col3.markdown("# How to reach me?")
col3.markdown("[Linkedin](https://www.linkedin.com/in/faisal-shamim-a49332241)")
def change_photo_state():
    st.session_state["photo"]="done"
uploaded_photo=col2.file_uploader("Upload a photo",on_change=change_photo_state)

camera_photo = col2.camera_input("Take a Photo",on_change=change_photo_state)
#----progress bar--------
if st.session_state["photo"]=="done":
    progress_bar=col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)
    col2.success("Photo uploaded successfully")

    #using expanders
    with st.expander("Click to read more "):
        st.write("Hello I am Faisal Shamim,Sophomore at Techno International Newtown.")
        st.write("I love engaging myself in developing something amazing via Python")
        st.write("Below is the image that had been taken/uploaded ")

        if uploaded_photo is None:
            st.image(camera_photo)  
        else:
            st.image(uploaded_photo)
        st.write("I am open to suggestions if any")
