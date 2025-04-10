import tkinter as tk
from tkinter import messagebox

class ProzentVerteiler:
    def __init__(self, root):
        self.root = root
        self.root.title("Prozentuale Verteilung")

        self.entries = []
        self.prozente = []
        self.labels = []

        self.setup_anzahl_input()

    def setup_anzahl_input(self):
        self.clear_window()

        tk.Label(self.root, text="Wie viele Sachen willst du aufteilen?").pack(pady=5)
        self.anzahl_entry = tk.Entry(self.root)
        self.anzahl_entry.pack(pady=5)

        tk.Button(self.root, text="Weiter", command=self.create_fields).pack(pady=10)

    def create_fields(self):
        try:
            self.anzahl = int(self.anzahl_entry.get())
            if self.anzahl <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gib eine gültige Anzahl ein.")
            return

        self.clear_window()
        self.entries = []
        self.prozente = []

        for i in range(self.anzahl):
            frame = tk.Frame(self.root)
            frame.pack(pady=3)

            tk.Label(frame, text=f"Sache {i + 1}").pack(side="left", padx=5)

            name_entry = tk.Entry(frame, width=20)
            name_entry.pack(side="left", padx=5)
            self.entries.append(name_entry)

            prozent_entry = tk.Entry(frame, width=10)
            prozent_entry.pack(side="left", padx=5)
            self.prozente.append(prozent_entry)

            tk.Label(frame, text="%").pack(side="left")

        # Summeingabe
        tk.Label(self.root, text="Gesamtsumme:").pack(pady=5)
        self.summe_entry = tk.Entry(self.root)
        self.summe_entry.pack(pady=5)

        # Button & Ergebnisanzeige
        tk.Button(self.root, text="Berechnen", command=self.berechne).pack(pady=10)

        self.ergebnis_frame = tk.Frame(self.root)
        self.ergebnis_frame.pack()

    def berechne(self):
        namen = [e.get() for e in self.entries]
        try:
            prozentwerte = [float(p.get()) for p in self.prozente]
            gesamt_summe = float(self.summe_entry.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")
            return

        if sum(prozentwerte) != 100:
            messagebox.showerror("Fehler", f"Die Summe der Prozente muss 100 sein (aktuell: {sum(prozentwerte)}).")
            return

        # Ergebnisse anzeigen
        for widget in self.ergebnis_frame.winfo_children():
            widget.destroy()

        for name, prozent in zip(namen, prozentwerte):
            wert = gesamt_summe * prozent / 100
            text = f"{name}: {wert:.2f}"
            tk.Label(self.ergebnis_frame, text=text).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = ProzentVerteiler(root)
    root.mainloop()
