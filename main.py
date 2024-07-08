import streamlit as st
from datetime import datetime, timedelta

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
def refresh():
    while True:
        weekdays, hours, minutes, seconds = countdown_timer(target_date)
        
        st.write(f"Pozostało : {weekdays} dni, {hours} godzin, {minutes} minut, {seconds} sekund",font_size=90)
        st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
        st.markdown("![Alt Text](https://www.icegif.com/wp-content/uploads/2023/01/icegif-666.gif)")
        
        # Odśwież zawartość co sekundę
        st.experimental_rerun()

# Uruchomienie funkcji do odświeżania
st.title("Odliczanie do kompika")
refresh()

