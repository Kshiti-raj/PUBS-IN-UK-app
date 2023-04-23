import streamlit as st
import pandas as pd
from folium.plugins import MarkerCluster
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px
from streamlit_extras.colored_header import colored_header

# Load the dataset into a DataFrame
pubs = pd.read_csv("open_pubs.csv", header=None)
# Assign column names to the DataFrame
pubs.columns = ["fsa_id", "name", "address","postcode","easting","northing","latitude", "longitude","local_authority"]
pubs["latitude"]= pd.to_numeric(pubs["latitude"], errors="coerce")
pubs["longitude"]= pd.to_numeric(pubs["longitude"], errors="coerce")
# Remove rows with null values in the latitude and longitude columns
pubs.dropna(subset=["latitude", "longitude"], inplace=True)


# HEADER
colored_header(
    label=":yellow[Nearest pubs are:]",
    description="This page shows the locations of nearest pubs.",
    color_name="red-70",
)
    
# Allow the user to enter their latitude and longitude
lat = st.number_input("Enter your latitude:")
lon = st.number_input("Enter your longitude:")
    
# Calculating the distance between the user's location and each pub using Euclidean Distance:
pubs["distance"] = np.sqrt((pubs["latitude"] - lat) ** 2 + (pubs["longitude"] - lon) ** 2)
    
# Displaing the nearest 5 pubs on a map:
nearest_pubs = pubs.sort_values("distance").head(5)
if len(nearest_pubs) > 0:
    map_center = [lat, lon]
    m = folium.Map(location=map_center, zoom_start=12)
    marker_cluster = MarkerCluster().add_to(m)
    for i, row in nearest_pubs.iterrows():
        folium.Marker([row["latitude"], row["longitude"]], popup=row["name"]).add_to(marker_cluster)
    folium_static(m)
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    #A bar chart of the distances:
    fig = px.bar(nearest_pubs, x="name", y="distance")
fig.update_layout(title="Distance to nearest pubs")
st.plotly_chart(fig)