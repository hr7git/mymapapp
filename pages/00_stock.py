import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 페이지 제목
st.title("글로벌 시가총액 Top 10 기업 - 최근 3년간 주가 변동")

# 글로벌 시가총액 Top 10 기업 (2025년 기준 예상, 티커는 각 기업에 맞게 수정)
top10_stocks = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 사우디 주식시장
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "NVIDIA": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "Eli Lilly": "LLY",
    "TSMC": "TSM"
}

# 기간 설정 (최근 3년)
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 데이터 다운로드 및 시각화
fig = go.Figure()

for company, ticker in top10_stocks.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data["Adj Close"],
            mode="lines",
            name=company
        ))
    except Exception as e:
        st.error(f"{company}({ticker}) 데이터 로드 중 오류 발생: {e}")

# 그래프 설정
fig.update_layout(
    title="글로벌 Top 10 기업 주가 추이 (최근 3년)",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_white",
    legend_title="기업명",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
