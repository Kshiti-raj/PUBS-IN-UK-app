import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

# Loading the dataset into a DataFrame pubs:
pubs = pd.read_csv("open_pubs.csv", header=None)
# Assigning column names to the DataFrame:
pubs.columns = ["fsa_id", "name", "address","postcode","easting","northing","latitude", "longitude","local_authority"]
pubs["latitude"]= pd.to_numeric(pubs["latitude"], errors="coerce")
pubs["longitude"]= pd.to_numeric(pubs["longitude"], errors="coerce")
# Removing rows with null values in the latitude and longitude columns:
pubs.dropna(subset=["latitude", "longitude"], inplace=True)
    

# Some basic statistics about the dataset :
# HEADER
colored_header(
    label=":beers: :green[Welcome to Open Pubs!] :beers:",
    description="This app shows the locations of pubs in the UK",
    color_name="red-70",
)

# centering the image:
left_co, cent_co,last_co = st.columns(3)
with left_co:
    st.image("pub.jpg",width=500)


st.header(" **Here are some basic statistics about the dataset:**")
st.write("- Number of pubs present: ", len(pubs))
st.write("- Number of unique postal codes: ", len(pubs["postcode"].unique()))
st.write("- Number of unique local authorities: ", len(pubs["local_authority"].unique()))

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")



# MOving pages with a click of button:
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(150,100,100);
}
</style>""", unsafe_allow_html=True)

# RADIO
reply = st.radio(
    "WOULD YOU LIKE TO MOVE ON TO THE NEXT PAGE ?",
    ("\"yes\"","\"no\""))
st.text("")
st.text("")
st.text("")

if reply == "\"yes\"":
    move_page = st.button("I want to move pages!")
    if move_page:
        switch_page("Pub Location")
if reply == "\"no\"":
    st.text("I think you should!!")