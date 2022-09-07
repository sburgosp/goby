import streamlit as st
from PIL import Image
st.title('GoBY')
st.subheader('Save Time   Having the cheapest price   Making your life easier')
image=Image.open('Uber.png')
image2=Image.open('Cabify.png')
image3=Image.open('Bolt.png')
image4=Image.open('Mytaxi.jpg')
st.image(image, caption='Sunrise by the mountains')
st.image(image2)
st.image(image3)
st.image(image4)
