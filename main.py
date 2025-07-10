import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Top 5 Chiang Mai Restaurants", layout="wide")

st.title("🇹🇭 Top 5 Local Restaurants in Chiang Mai")
st.markdown("Here are 5 must-try local restaurants loved by Korean travelers. Explore their locations on the map below!")

# ---------------------
# Restaurant data (5 spots)
# ---------------------
chiangmai_foods = [
    {
        "name": "Khao Soi Mae Sai",
        "location": [18.7956, 98.9937],
        "desc": "A famous local spot for Chiang Mai-style curry noodles (Khao Soi) with deep and rich broth.",
        "summary": "Rich curry broth with soft noodles — a must-try Northern Thai specialty."
    },
    {
        "name": "SP Chicken",
        "location": [18.7864, 98.9876],
        "desc": "Renowned for charcoal-grilled whole chicken. Crispy skin and juicy meat!",
        "summary": "Charcoal-grilled chicken that’s crispy outside and tender inside."
    },
    {
        "name": "Tikky Cafe",
        "location": [18.7883, 98.9816],
        "desc": "Popular for clean, affordable Thai home-style dishes made with fresh ingredients.",
        "summary": "Fresh and healthy Thai dishes served in a casual setting."
    },
    {
        "name": "Khao Soi Khun Yai",
        "location": [18.7940, 98.9811],
        "desc": "Hidden in a small alley, this spot offers authentic and traditional Khao Soi.",
        "summary": "Locals line up here for authentic Khao Soi in a quiet alley."
    },
    {
        "name": "Huen Muan Jai",
        "location": [18.8042, 98.9724],
        "desc": "A restaurant serving traditional Northern Thai cuisine with a rustic atmosphere.",
        "summary": "Authentic Northern Thai flavors in a cozy, traditional setting."
    },
]

# ---------------------
# Restaurant summaries
# ---------------------
st.subheader("📋 Restaurant Summaries")
for food in chiangmai_foods:
    st.markdown(f"**🍴 {food['name']}** — {food['summary']}")

# ---------------------
# Map
# ---------------------
st.subheader("📍 Restaurant Map")
chiangmai_map = folium.Map(location=[18.7877, 98.9931], zoom_start=13)
cluster = MarkerCluster().add_to(chiangmai_map)

for food in chiangmai_foods:
    folium.Marker(
        location=food["location"],
        popup=f"<b>{food['name']}</b><br>{food['desc']}",
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(cluster)

st_folium(chiangmai_map, width=900)
