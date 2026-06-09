import ipywidgets as widgets
from IPython.display import display, clear_output

def starte_quiz():
    # Das Layout wird hier direkt übergeben, damit der lange Text sauber angezeigt wird
    optionen = widgets.RadioButtons(
        options=[
            '1 mal',
            '10 mal',
            'Gar nicht'
        ],
        value=None, # Das 'value=None' muss IN die Klammer der RadioButtons hinein!
        layout=widgets.Layout(width='max-content') # Verhindert das Überlappen
    )
    
    button = widgets.Button(description="Prüfen", button_style='info')
    ausgabe = widgets.Output()

    def antwort_pruefen(b):
        with ausgabe:
            clear_output()
            if optionen.value == '10 mal':
                print("🎉 Richtig!")
            elif optionen.value is None:
                print("⚠️ Bitte wähle zuerst eine Antwort aus.")
            else:
                print("❌ Falsch!")

    button.on_click(antwort_pruefen)
    display(optionen, button, ausgabe)
