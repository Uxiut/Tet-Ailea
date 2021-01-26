from easygui import *
import sys
import webbrowser
valinta1_nettisivu = "https://www.mauno.fi/fi/lounaslistat"
valinta2_nettisivu = "https://www.unica.fi/ravintolat/kupittaa/deli-pharma"
valinta3_nettisivu = "https://www.raflaamo.fi/fi/turku/bistro-elli/menu"
chrome_path = r"C:\Users\tr0640\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser(chrome_path))

ruokakysely_teksti = "Huomenta, Missä halajat syödä tänään? "
ruokakysely_otsikko = "Ruoka"
ruokakysely_valinnat = ["Maunossa!", "Deli-Pharmassa!", "Elli-bistrossa!", "Haluan nähdä kaikki!"]
ruokakysely = choicebox(ruokakysely_teksti, ruokakysely_otsikko, ruokakysely_valinnat)

#
if ruokakysely == ruokakysely_valinnat[0]:
    webbrowser.get('chrome').open(valinta1_nettisivu)
    
elif ruokakysely == ruokakysely_valinnat[1]:
    webbrowser.get('chrome').open(valinta2_nettisivu)
    
elif ruokakysely == ruokakysely_valinnat[2]:
    webbrowser.get('chrome').open(valinta3_nettisivu)

elif ruokakysely == ruokakysely_valinnat[3]:
    webbrowser.get('chrome').open(valinta1_nettisivu)
    webbrowser.get('chrome').open(valinta2_nettisivu)
    webbrowser.get('chrome').open(valinta3_nettisivu)
