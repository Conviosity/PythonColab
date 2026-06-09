import ipywidgets as widgets
from IPython.display import display, clear_output

def starte_quiz():
    optionen = widgets.RadioButtons(options=['Der Computer druckt das Wort Hallo auf Papier aus.', 'Es gibt eine Fehlermeldung, weil der Computer "Hallo" für einen Befehl hält, den er nicht kennt.', 'Nichts.'], value=None, description='Antworten:')
    button = widgets.Button(description="Prüfen", button_style='info')
    ausgabe = widgets.Output()

    def antwort_pruefen(b):
        with ausgabe:
            clear_output()
            if optionen.value == 'Es gibt eine Fehlermeldung, weil der Computer "Hallo" für einen Befehl hält, den er nicht kennt.':
                print("🎉 Richtig!")
            else:
                print("❌ Falsch!")

    button.on_click(antwort_pruefen)
    display(optionen, button, ausgabe)
