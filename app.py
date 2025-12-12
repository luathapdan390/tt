import streamlit as st
import pandas as pd
from streamlit_calendar import calendar # Thư viện vẽ lịch
# Cần cài đặt kết nối Google Sheets API ở đây (gspread)

st.title("My Time Tracker (Like Clockify)")

# 1. Form nhập liệu
with st.form("entry_form"):
    project = st.selectbox("Dự án", ["Making Videos", "Coding", "Reading"])
    date = st.date_input("Ngày")
    start_time = st.time_input("Bắt đầu")
    end_time = st.time_input("Kết thúc")
    submitted = st.form_submit_button("Lưu")

    if submitted:
        # Tính thời lượng
        duration = "3 hours" # Logic tính toán thời gian ở đây
        
        # Gửi dữ liệu lên Google Sheets
        # add_to_google_sheet(project, date, start_time, end_time, duration)
        st.success("Đã lưu vào Google Sheets!")

# 2. Hiển thị Calendar
# Lấy dữ liệu từ Google Sheets về dataframe
# df = get_data_from_sheet()

# Hiển thị dạng bảng (hoặc dùng component calendar để hiển thị đẹp hơn)
st.subheader("Lịch sử làm việc")
st.dataframe({
    "Dự án": ["Making Videos", "Book Club"],
    "Thời lượng": ["3h", "50m"],
    "Ngày": ["2025-12-12", "2025-12-12"]
})