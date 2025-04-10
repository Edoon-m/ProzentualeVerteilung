import streamlit as st

st.title("Prozentuale Verteilung")

# Schritt 1: Anzahl der Elemente eingeben
anzahl = st.number_input("Wie viele Sachen willst du aufteilen?", min_value=1, step=1)

namen = []
prozente = []

# Schritt 2: Felder erzeugen
with st.form("verteilungs_form"):
    st.write("Bitte gib Namen und Prozentwerte ein:")
    for i in range(anzahl):
        col1, col2 = st.columns([2, 1])
        name = col1.text_input(f"Sache {i+1}", key=f"name_{i}")
        prozent = col2.number_input(f"Prozent {i+1}", min_value=0.0, max_value=100.0, step=0.1, key=f"prozent_{i}")
        namen.append(name)
        prozente.append(prozent)

    gesamt_summe = st.number_input("Gesamtsumme", min_value=0.0, step=1.0)

    submitted = st.form_submit_button("Berechnen")

# Schritt 3: Berechnung und Ergebnis
if submitted:
    if abs(sum(prozente) - 100.0) > 1e-6:
        st.error(f"Die Summe der Prozente muss 100 sein (aktuell: {sum(prozente):.2f})")
    else:
        st.success("Berechnung erfolgreich:")
        for name, prozent in zip(namen, prozente):
            wert = gesamt_summe * prozent / 100
            st.write(f"**{name}**: {wert:.2f}")