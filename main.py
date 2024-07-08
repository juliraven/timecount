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

# Ustaw datę docelową
target_date = datetime(2024, 8, 1)

st.title("Odliczanie do 1 sierpnia 2024")

# Pętla odświeżania co sekundę
while True:
    days, hours, minutes, seconds = countdown_timer(target_date)
    
    st.write(f"Pozostało: {days} dni, {hours} godzin, {minutes} minut, {seconds} sekund")

    # Wymaż poprzednie wyniki
    st.empty()

