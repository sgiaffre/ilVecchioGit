# Iniziale impostazione per un Fantacalcio
# L'utente sceglie da una lista e i nomi compaiono in una nuova lista
import PySimpleGUI as sg

giocatori = ['Mazzola', 'Rivera', 'Riva']
squadra = []
layout = [[
    sg.Listbox(giocatori,
               size=(15, len(giocatori)),
               key='-GIOCATORI-'),
    sg.Listbox(squadra,
               size=(15, len(squadra)),
               key='-SQUADRA-')],
    [sg.Button('Aggiungi', button_color='Green', key='-ADD-')],
    [sg.Button('Rimuovi', button_color='Red', key='-REMOVE-')]
    ]

window = sg.Window('FANTACALCIO', layout, resizable=True)

while True:  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # se è scelto un giocatore da aggiungere:
    if event=='-ADD-' and values['-GIOCATORI-']  :
        ungiocatore = values['-GIOCATORI-'][0]
        squadra.append(ungiocatore)
        window['-SQUADRA-'].update(squadra)
        giocatori.remove(ungiocatore)
        window['-GIOCATORI-'].update(giocatori)    
   
    # se è scelto un giocatore da togliere:
    if event=='-REMOVE-' and values['-SQUADRA-']  :
        ungiocatore = values['-SQUADRA-'][0]
        giocatori.append(ungiocatore)
        window['-GIOCATORI-'].update(giocatori)
        squadra.remove(ungiocatore)
        window['-SQUADRA-'].update(squadra)    

window.close()
