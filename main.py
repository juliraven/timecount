import streamlit as st
from datetime import datetime, timedelta
from streamlit_extras.let_it_rain import rain 
from streamlit_autorefresh import st_autorefresh

l, r = st.columns((2,2))

def example():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

example()

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
    minutes, _ = divmod(seconds, 60)
    
    return weekdays, hours, minutes

# Ustaw datę docelową
target_date = datetime(2024, 9, 20)

# Funkcja do odświeżania interfejsu co minutę
def display_countdown():
    weekdays, hours, minutes = countdown_timer(target_date)
    st.write(f"Pozostało : {weekdays} dni, {hours} godzin, {minutes} minut")
    l.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
    r.markdown("![Alt Text](https://www.icegif.com/wp-content/uploads/2023/01/icegif-666.gif)")

# Uruchomienie funkcji do odświeżania
st.title("Odliczanie do kompika")
display_countdown()

# Automatyczne odświeżanie co minutę
st_autorefresh(interval=60000, key="refresh")
