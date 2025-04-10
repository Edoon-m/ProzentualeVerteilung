# Prozent-Verteiler App

Mit dieser Streamlit-App kannst du beliebige Dinge prozentual aufteilen und auf Basis einer Gesamtsumme berechnen lassen, wie viel jede Sache bekommt.

## Funktionen

- Gib ein, wie viele Dinge du aufteilen möchtest
- Vergib Namen und Prozente für jede Sache
- Gib die Gesamtsumme ein
- Die App berechnet automatisch die Verteilung anhand der Prozentwerte

## Beispiel

Wenn du 3 Dinge mit 50%, 30% und 20% eingibst und eine Gesamtsumme von 1000 €, dann berechnet die App automatisch:

- Sache 1: 500 €
- Sache 2: 300 €
- Sache 3: 200 €

## Nutzung (lokal)

```bash
pip install -r requirements.txt
streamlit run app.py
