import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from django.shortcuts import render

def stock_chart(request):
    # รับค่าหุ้นที่ต้องการดู (ใช้ค่าเริ่มต้น 'AAPL' ถ้าไม่ได้ส่ง request)
    stock_symbol = request.GET.get('symbol', 'AAPL')

    # ดึงข้อมูลหุ้นจาก yfinance
    data = yf.download(stock_symbol, start="2023-01-01", end="2023-12-31")

    # สร้างกราฟ Plotly
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Market Data'
    ))

    # ตั้งค่าชื่อและแกน
    fig.update_layout(
        title=f'{stock_symbol} Stock Price',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )

    # แปลงกราฟ Plotly เป็น HTML
    chart = fig.to_html(full_html=False)

    # ส่งข้อมูลไปยัง Template
    return render(request, 'stockapp/stock_chart.html', {'chart': chart, 'stock_symbol': stock_symbol})
