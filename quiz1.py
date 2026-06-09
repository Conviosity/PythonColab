import ipywidgets as widgets
from IPython.display import display, clear_output

def starte_quiz():
    frage = widgets.HTML(value="<h3>Frage: Welcher Planet ist der Sonne am nächsten?</h3>")
    optionen = widgets.RadioButtons(options=['Venus', 'Erde', 'Merkur', 'Mars'], value=None, description='Antworten:')
    button = widgets.Button(description="Prüfen", button_style='info')
    ausgabe = widgets.Output()

    def antwort_pruefen(b):
        with ausgabe:
            clear_output()
            if optionen.value == 'Merkur':
                print("🎉 Richtig!")
            else:
                print("❌ Falsch!")

    button.on_click(antwort_pruefen)
    display(frage, optionen, button, ausgabe)
