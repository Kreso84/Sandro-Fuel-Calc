import streamlit as st
import math

# Konfiguracija aplikacije
st.set_page_config(page_title="Sandro Fuel Calc", page_icon="⛽")

# Glavni naslov prema tvojoj želji
st.title("⛽ Da Sandro ne ostane bez goriva")
st.subheader("Službeni alat za preživljavanje na stazi. Razvijeno jer nam je dosadilo gledati Sandra kako gura auto zadnjih 500 metara. 🏁")

st.markdown("---")

# Unos podataka za izračun
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⏱️ Vrijeme")
    race_duration = st.number_input("Trajanje utrke (minuta)", min_value=1, value=20, help="Ukupno trajanje sesije")
    avg_lap_time_min = st.number_input("Vrijeme kruga (minute)", min_value=0, value=1)
    avg_lap_time_sec = st.number_input("Vrijeme kruga (sekunde)", min_value=0, max_value=59, value=30)

with col2:
    st.markdown("### ⛽ Potrošnja")
    fuel_per_lap = st.number_input("Litara po krugu", min_value=0.1, value=3.4, step=0.1, help="Provjeri na kontrolnoj ploči nakon 2-3 kruga")
    safety_laps = st.number_input("Rezerva (krugova)", min_value=0, value=2, help="Koliko krugova viška želiš za svaki slučaj")

# Izračunavanje decimalnog vremena kruga
total_lap_time_decimal = avg_lap_time_min + (avg_lap_time_sec / 60)

if total_lap_time_decimal > 0:
    # Broj krugova koje je moguće odvoziti u zadanom vremenu
    laps_total = race_duration / total_lap_time_decimal
    # Ukupno gorivo s uračunatom rezervom
    total_fuel_needed = (laps_total + safety_laps) * fuel_per_lap
    
    st.divider()
    
    # Istaknuti rezultat
    st.success(f"### 🏁 Potrebno natočiti: {math.ceil(total_fuel_needed)} L")
    
    # Detaljne informacije
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.write(f"**Predviđeni broj krugova:** {math.ceil(laps_total)}")
    with col_res2:
        st.write(f"**Rezerva uključena:** {safety_laps} kruga")
    
    st.warning("Pazi na pritisak u gumama (Target: 26.8 PSI)!")
else:
    st.error("Unesi vrijeme kruga da Sandro ne bi morao gurati auto!")

st.caption("Verzija 1.0 | Za internu upotrebu - Kreso & Co.")
