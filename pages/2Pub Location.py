import streamlit as st
import pandas as pd
from folium.plugins import MarkerCluster
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
import folium
from streamlit_folium import folium_static

# Loading the dataset into a DataFrame pubs:
pubs = pd.read_csv("open_pubs.csv", header=None)

# Assigning column names to the DataFrame :
pubs.columns = ["fsa_id", "name", "address","postcode","easting","northing","latitude", "longitude","local_authority"]
pubs["latitude"]= pd.to_numeric(pubs["latitude"], errors="coerce")
pubs["longitude"]= pd.to_numeric(pubs["longitude"], errors="coerce")
# Removing rows with null values in the latitude and longitude columns
pubs.dropna(subset=["latitude", "longitude"], inplace=True)


# HEADER
colored_header(
    label=":beer: :blue[PUB LOCATIONS] :beer:",
    description="This page shows the locations of pubs.",
    color_name="red-70",
)
    
# Allow the user to select the area by postal code or local authority:
area_type = st.radio("Select the area type:", ("Postal Code", "Local Authority"))
if area_type == "Postal Code":
    area = st.text_input("Enter the postal code:")
    pubs_in_area = pubs[pubs["postcode"].str.startswith(area)]
else:
    area = st.selectbox("Select the local authority:", pubs["local_authority"].unique())
    pubs_in_area = pubs[pubs["local_authority"] == area]
    
#A map of the pubs in the area
if len(pubs_in_area) > 0:
    map_center = [pubs_in_area["latitude"].mean(), pubs_in_area["longitude"].mean()]
    m = folium.Map(location=map_center, zoom_start=12)
    marker_cluster = MarkerCluster().add_to(m)
    for i, row in pubs_in_area.iterrows():
        folium.Marker([row["latitude"], row["longitude"]], popup=row["name"]).add_to(marker_cluster)
    folium_static(m)
else:
    st.warning("No pubs found in the selected area.")


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
        switch_page("Nearest Pub")
if reply == "\"no\"":
    st.text("I think you should!!")