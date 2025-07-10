import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="도쿄 & 치앙마이 관광 지도", layout="wide")

st.title("🇯🇵 도쿄 & 🇹🇭 치앙마이 관광 명소 추천")
st.markdown("한국인들에게 인기 있는 관광지와 꼭 먹어야 할 맛집을 지도로 확인해보세요!")

# ---------------------
# 도쿄 관광 명소
# ---------------------
tokyo_spots = [
    {"name": "도쿄 타워", "location": [35.6586, 139.7454], "desc": "도쿄의 대표적인 전망대"},
    {"name": "아사쿠사 센소지", "location": [35.7148, 139.7967], "desc": "일본에서 가장 오래된 사찰"},
    {"name": "시부야 스크램블 교차로", "location": [35.6595, 139.7004], "desc": "세계에서 가장 번잡한 교차로"},
]

# ---------------------
# 치앙마이 관광 명소 + 맛집
# ---------------------
chiangmai_spots = [
    {"name": "도이수텝 사원", "location": [18.8056, 98.9215], "desc": "치앙마이에서 가장 유명한 사원"},
    {"name": "치앙마이 올드타운", "location": [18.7877, 98.9931], "desc": "역사적인 유적지와 사원이 밀집한 지역"},
    {"name": "왓체디루앙", "location": [18.7861, 98.9866], "desc": "14세기에 지어진 고대 사원"},
]

chiangmai_foods = [
    {"name": "카오쏘이 메솟", "location": [18.7956, 98.9937], "desc": "진한 국물의 카오쏘이 맛집"},
    {"name": "SP 치킨", "location": [18.7864, 98.9876], "desc": "숯불치킨으로 유명한 현지 맛집"},
]

# ---------------------
# Folium 지도 생성
# ---------------------
tab1, tab2 = st.tabs(["도쿄 관광 명소", "치앙마이 관광 + 맛집"])

with tab1:
    st.subheader("📍 도쿄 관광 명소 지도")
    tokyo_map = folium.Map(location=[35.6804, 139.7690], zoom_start=12)
    for spot in tokyo_spots:
        folium.Marker(
            location=spot["location"],
            popup=f"{spot['name']}: {spot['desc']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(tokyo_map)
    st_folium(tokyo_map, width=900)

with tab2:
    st.subheader("📍 치앙마이 관광 명소 & 맛집 지도")
    chiangmai_map = folium.Map(location=[18.7877, 98.9931], zoom_start=13)
    cluster = MarkerCluster().add_to(chiangmai_map)

    # 관광지
    for spot in chiangmai_spots:
        folium.Marker(
            location=spot["location"],
            popup=f"{spot['name']}: {spot['desc']}",
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(cluster)

    # 맛집
    for food in chiangmai_foods:
        folium.Marker(
            location=food["location"],
            popup=f"🍽️ {food['name']}: {food['desc']}",
            icon=folium.Icon(color='red', icon='cutlery')
        ).add_to(cluster)

    st_folium(chiangmai_map, width=900)
