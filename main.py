import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="치앙마이 맛집 지도", layout="wide")

st.title("🇹🇭 치앙마이 추천 맛집 5선")
st.markdown("한국인 여행객들이 좋아하는 **치앙마이 현지 맛집** 5곳을 소개합니다. 지도에서 위치를 확인해보세요!")

# ---------------------
# 맛집 리스트 (5곳)
# ---------------------
chiangmai_foods = [
    {
        "name": "카오쏘이 메솟",
        "location": [18.7956, 98.9937],
        "desc": "진한 국물의 치앙마이식 카레국수 전문점. 현지인과 관광객 모두에게 인기!",
        "summary": "부드러운 면발과 진한 국물의 조화, 현지 스타일 카오쏘이 맛집"
    },
    {
        "name": "SP 치킨",
        "location": [18.7864, 98.9876],
        "desc": "숯불에 구운 통닭이 유명한 로컬 치킨 맛집",
        "summary": "겉은 바삭, 속은 촉촉! 숯불통닭이 일품인 숨은 명소"
    },
    {
        "name": "Tikky Cafe",
        "location": [18.7883, 98.9816],
        "desc": "깔끔하고 저렴한 태국 가정식 요리를 제공하는 인기 카페",
        "summary": "신선한 재료로 만든 저렴하고 건강한 태국 가정식"
    },
    {
        "name": "Khao Soi Khun Yai",
        "location": [18.7940, 98.9811],
        "desc": "오래된 골목길 안 숨겨진 카오쏘이 명가",
        "summary": "현지인도 줄 서는 골목 맛집, 정통 카오쏘이 맛볼 수 있음"
    },
    {
        "name": "Huen Muan Jai",
        "location": [18.8042, 98.9724],
        "desc": "치앙마이 북부 전통 요리를 맛볼 수 있는 식당",
        "summary": "현지 분위기 가득한 북부 전통식 식당, 돼지고기 카레 추천"
    },
]

# ---------------------
# 맛집 요약 출력
# ---------------------
st.subheader("📋 맛집 요약 정보")
for food in chiangmai_foods:
    st.markdown(f"**🍴 {food['name']}** — {food['summary']}")

# ---------------------
# 지도에 마커 표시
# ---------------------
st.subheader("📍 맛집 지도")
chiangmai_map = folium.Map(location=[18.7877, 98.9931], zoom_start=13)
cluster = MarkerCluster().add_to(chiangmai_map)

for food in chiangmai_foods:
    folium.Marker(
        location=food["location"],
        popup=f"<b>{food['name']}</b><br>{food['desc']}",
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(cluster)

st_folium(chiangmai_map, width=900)
