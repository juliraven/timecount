import streamlit as st
from datetime import datetime, timedelta

def countdown_timer(target_date):
    now = datetime.now()
    delta = target_date - now
    days = delta.days
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds

st.title("Odliczanie do wybranego dnia")

target_date = st.date_input("Wybierz datę końcową")
target_time = st.time_input("Wybierz godzinę końcową", value=datetime.now().time())

if target_date:
    target_datetime = datetime.combine(target_date, target_time)
    days, hours, minutes, seconds = countdown_timer(target_datetime)

    st.write(f"Pozostało: {days} dni, {hours} godzin, {minutes} minut, {seconds} sekund")

    st.markdown(f"""
    ## Szczegóły:
    - Dni: **{days}**
    - Godzin: **{hours}**
    - Minut: **{minutes}**
    - Sekund: **{seconds}**
    """)
else:
    st.write("Wybierz datę i godzinę, aby rozpocząć odliczanie.")
