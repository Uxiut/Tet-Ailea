import webbrowser

chrome_path = r"C:\Users\tr0640\AppData\Local\Google\Chrome\Application\chrome.exe"
#webbrowser.open_new("google.com")
url = 'google.com'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(url)