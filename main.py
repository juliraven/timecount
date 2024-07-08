import streamlit as st
from datetime import datetime, timedelta
import asyncio

def countdown_timer(target_date):
    now = datetime.now()
    delta = target_date - now
    days = delta.days
    
    # Oblicz liczbę dni roboczych
    weekdays = 0
    for i in range(days):
        current_day = now + timedelta(days=i)
        if current_day.weekday() < 5:  # Poniedziałek - Piątek
            weekdays += 1
            
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    
    return weekdays, hours, minutes, seconds

# Ustaw datę docelową
target_date = datetime(2024, 9, 20)

# Funkcja do odświeżania interfejsu co sekundę
async def refresh():
    while True:
        weekdays, hours, minutes, seconds = countdown_timer(target_date)
        
        st.write(f"Pozostało : {weekdays} dni, {hours} godzin, {minutes} minut, {seconds} sekund")

        await asyncio.sleep(1)  # Opóźnienie na 1 sekundę

# Uruchomienie funkcji do odświeżania asynchronicznie
st.title("Odliczanie do 1 sierpnia 2024")
loop = asyncio.get_event_loop()
loop.run_until_complete(refresh())

