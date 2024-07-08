import streamlit as st
from datetime import datetime, timedelta
import time

def countdown_timer(target_date):
    now = datetime.now()
    delta = target_date - now
    days = delta.days
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds

def calculate_weekdays(start_date, end_date):
    day_count = 0
    current_date = start_date

    while current_date < end_date:
        if current_date.weekday() < 5:  # Monday to Friday are 0-4
            day_count += 1
        current_date += timedelta(days=1)
    
    return day_count

# Ustaw datę docelową
target_date = datetime(2024, 8, 1)

st.title("Odliczanie do 1 sierpnia 2024 (bez sobót i niedziel)")

# Pętla odświeżania co sekundę
while True:
    weekdays_left = calculate_weekdays(datetime.now(), target_date)
    days, hours, minutes, seconds = countdown_timer(target_date)
    
    st.write(f"Pozostało: {weekdays_left} dni roboczych, {hours} godzin, {minutes} minut, {seconds} sekund")

    st.markdown(f"""
    ## Szczegóły:
    - Dni roboczych: **{weekdays_left}**
    - Godzin: **{hours}**
    - Minut: **{minutes}**
    - Sekund: **{seconds}**
    """)

    # Opóźnienie 1 sekundy
    time.sleep(1)

    # Wymaż poprzednie wyniki
    st.experimental_rerun()
