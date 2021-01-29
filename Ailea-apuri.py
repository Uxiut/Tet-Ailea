from easygui import *
import sys
import webbrowser
valinta1_nettisivu = "https://teams.microsoft.com/go#"
valinta2_nettisivu = "https://outlook.office365.com/mail/inbox"
valinta3_nettisivu = "github.com"
valinta4_nettisivu = "discordapp.com/activity"
chrome_path = r"C:\Users\tr0640\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser(chrome_path))

apuri_kysymys_teksti = "Kuinka voin auttaa?"
apuri_kysymys_otsikko = "Apuri"
apuri_valinnat = ["Avaa Teams", "Avaa Outlook", "Avaa Github", "Avaa Discord", "Avaa kaikki"]
Apuri = choicebox(apuri_kysymys_teksti, apuri_kysymys_otsikko, apuri_valinnat)

if Apuri == apuri_valinnat[0]:
    webbrowser.get('chrome').open(valinta1_nettisivu)
    
elif Apuri == apuri_valinnat[1]:
    webbrowser.get('chrome').open(valinta2_nettisivu)
    
elif Apuri == apuri_valinnat[2]:
    webbrowser.get('chrome').open(valinta3_nettisivu)

elif Apuri == apuri_valinnat[3]:
    webbrowser.get('chrome').open(valinta4_nettisivu)

elif Apuri == apuri_valinnat[4]:
    webbrowser.get('chrome').open(valinta1_nettisivu)
    webbrowser.get('chrome').open(valinta2_nettisivu)
    webbrowser.get('chrome').open(valinta3_nettisivu)
    webbrowser.get('chrome').open(valinta4_nettisivu)