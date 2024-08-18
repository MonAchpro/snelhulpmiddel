#alles extra
import os
import webbrowser as web
try:
    import AppOpener as ap
except:
    print("AppOpener is niet geinstalleerd. Download AppOpener via de terminal. (pip install AppOpener)")
try:
    import wikipedia as wiki
except:
    print("Wikipedia is niet geinstalleerd. Download Wikipedia via de terminal. (pip install wikipedia)")
try:
    import googletrans 

except:
    print("Googletrans is niet geinstalleerd. Download Googletrans via de terminal. (pip install googletrans)")
import requests


#functies
def clear_screen():
    #maakt het scherm leeg door een command line command
    os.system('cls' if os.name == 'nt' else 'clear')

def ip_tracker():
    ip = input("welke ip wilt u tracken? ")
    url = f"https://ipinfo.io/{ip}/json"
    #Vraagt de informatie van de url
    response = requests.get(url)
    data = response.json()
    #Extraheer breedte- en lengtegraad
    loc = data['loc'].split(',')
    latitude = loc[0]
    longitude = loc[1]
    print(data)
    print("https://www.google.nl/maps/?q=" + latitude + "," + longitude)


def change_color():
    #verandert de kleur van het scherm door een command line command
    color = input("welke kleur? ")
    if os.name == "nt":
        if color == "zwart":
            os.system('color 0')
        elif color == "blauw":
            os.system('color 1')
        elif color == "groen":
            os.system('color 2')
        elif color == "aqua":
            os.system('color 3')
        elif color == "rood":
            os.system('color 4')
        elif color == "paars":
            os.system('color 5')
        elif color == "geel":
            os.system('color 6')
        elif color == "wit":
            os.system('color 7')
        elif color == "grijs":
            os.system('color 8')
        elif color == "lichtblauw":
            os.system('color 9')
        elif color == "lichtgroen":
            os.system('color A')
        elif color == "lichtaqua":
            os.system('color B')
        elif color == "lichtrood":
            os.system('color C')
        elif color == "lichtpaars":
            os.system('color D')
        elif color == "lichtgeel":
            os.system('color E')
        elif color == "helderwit":
            os.system('color F')
        elif color == "lijst":
            everycolor = ["zwart","blauw","groen","aqua","rood","paars","geel","wit","grijs","lichtblauw","lichtgroen","lichtaqua","lichtrood","lichtpaars","lichtgeel","helderwit"]
            print("\n".join(everycolor))


def install_file(url, name):
    #vraagt de url bestand
    response = requests.get(url)
    #slaat het betand op in een variabele
    content = response.content
    with open(name, "wb") as f:
        #scrijft de variabele op in een bestand
        f.write(content)
    #start het bestand
    os.startfile(name)







def install():
    #maakt gebruik van een andere functie om een app te installeren
    app = input("welke app wilt u installeren? ")
    if app == "discord":
        install_file("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64", "discord.exe")
    elif app == "steam":
        install_file("https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe", "steam.exe")
    elif app == "spotify":
        install_file("https://download.scdn.co/SpotifySetup.exe", "spotify.exe")
    elif "epic" in app:
        install_file("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi", "epicgames.msi")
    elif app == "vlc":
        install_file("https://ftp.halifax.rwth-aachen.de/videolan/vlc/3.0.21/win64/vlc-3.0.21-win64.exe", "vlc.exe")
    elif "obs" in app:
        install_file("https://cdn-fastly.obsproject.com/downloads/OBS-Studio-30.2.2-Windows-Installer.exe", "obs.exe")
    elif app == "virtualbox":
        install_file("https://download.virtualbox.org/virtualbox/7.0.20/VirtualBox-7.0.20-163906-Win.exe", "virtualbox.exe")
    elif "google" and "earth" in app:
        install_file("https://dl.google.com/tag/s/appguid%3D%7B65E60E95-0DE9-43FF-9F3F-4F7D2DFF04B5%7D%26iid%3D%7B65E60E95-0DE9-43FF-9F3F-4F7D2DFF04B5%7D%26lang%3Dnl%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Earth%2520Pro%26needsadmin%3DTrue%26brand%3DGGGE/earth/client/GoogleEarthProSetup.exe", "googleearth.exe")
    elif app == "firefox":
        install_file("https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US", "firefox.exe")
    else:
        print("app niet gevonden")

def news():
    newssearch = input("welk nieuws wilt u opzoeken? ")
    #vraagt informatie via de url via de variabele nenwssearch en newsapi voor de api
    url = f'https://newsapi.org/v2/everything?q={newssearch}&from=2024-08-01&sortBy=popularity&apiKey={newsapi}&language=nl'

    #slaat de informatie op in een variabele
    response = requests.get(url)

    #schrijft de variabele
    print(response.json())


def weather():
    weathersearch = input("Van welke plaats wilt u het weer weten? ")

    #vraagt informatie via de url via de variabele weathersearch en weatherapi voor de api
    url = f'https://api.weatherapi.com/v1/current.json?key={weatherapi}&q={weathersearch}&aqi=yes'

    #slaat de informatie op in een variabele
    response = requests.get(url)

    #schrijft de variabele
    print(response.json())        


def translate(what, lang):
    #maakt gebruik van googletrans library om te vertalen
    translation = googletrans.Translator().translate(what, dest=lang)
    #en geeft de vertaling terug zodat je dit kan gebruiken als een variabele
    return translation.text


def recept():
    #vraagt het recept en vertaalt het naar het engels
    receptname = input("Van welke eten wilt u het recept weten? ")
    receptname = translate(receptname, "en")
    url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={receptname}'
    print(url)
    response = requests.get(url)

    print(response.json()) 

def klein_url():
    #verkleint een url via ulvis.net en een bijnaam 
    kleine_url = input("Welke url wilt u kleiner maken? (voeg de https:// erbij) ")
    fakename = input("Welke bijnaam? ")
    url = f'https://ulvis.net/API/write/get?url={kleine_url}&custom={fakename}&private=1'

    response = requests.get(url)

    print(response.json()) 


def ISS():
    #slaat een url op in een variabele
    url = f'http://api.open-notify.org/iss-now.json'
    url2 = f'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    print("De locatie van de ISS is: ")
    print(response.json())
    response = requests.get(url2)
    print("het aantal mensen in de ruimte is:") 
    print(response.json())



#dingetjes belangrijk voor de code
#zet de wikipedia taal in het Nederlands
wiki.set_lang("nl")
print("Bepaalde functies zullen niet werken zonder internet.")
print("dit is een hulpmiddel wat u sneller informatie laat vinden en sneller apps opent. Schrijf help voor alle commands")
#kijkt of er een newsapi.txt bestand bestaat zo niet maakt het een bestand met jouw api erin
if not os.path.exists("newsapi.txt"):
    ai = input("Zou u ook nieuws willen?")
    if "ja" in ai:
        newsapi = input("Als u een newsapi account heeft geef uw newsapi alstublieft anders zou u er een kunnen maken en het nu typen of nee typen om het te annuleren. ")
        if newsapi == "nee":
            pass
        else:
            with open("newsapi.txt", "w") as file:
                file.write(newsapi) 
    with open ("newsapi.txt", "r") as file:
        newsapi = file.read()
#kijkt of er een newsapi.txt bestand bestaat zo niet maakt het een bestand met jouw api erin
if not os.path.exists("weatherapi.txt"):
    ai = input("Wilt u ook informatie over het weer? ")
    if "ja" in ai:
        weatherapi = input("Als u een weatherapi account heeft geef uw weatherapi alstublieft anders zou u er een kunnen maken en het nu typen of nee typen om het te annuleren. ")
        if weatherapi == "nee":
            pass
        else:
            with open("weatherapi.txt", "w") as file:
                file.write(weatherapi)
    with open("weatherapi.txt", "r") as file:
        weatherapi = file.read()
print("Dit zijn alle talen die je kunt vertalen\n")
#schrijft alle mogelijke talen waarmee je kan vertalen
print(googletrans.LANGUAGES)
input("")
#maakt het scherm leeg
clear_screen()
with open ("newsapi.txt", "r") as file:
    #slaat de api in een variabele op
    newsapi = file.read()
with open ("weatherapi.txt", "r") as file:
    weatherapi = file.read()


#main
while True:
    ai = input("wat wil je doen? ")
    if ai == "stop":
        break
    elif "open gmail" in ai:
        web.open("https://mail.google.com/mail/u/0/#inbox")
    elif "open youtube" in ai:
        web.open("https://www.youtube.com/")
    elif "open facebook" in ai:
        web.open("https://www.facebook.com/")
    elif "open google" in ai:
        web.open("https://www.google.com/")
    elif "open google" and "maps" in ai:
        web.open("https://www.google.be/maps")
    elif "open kladblok" in ai:
        ap.open("kladblok")
    elif "open rekenmachine" in ai:
        ap.open("Rekenmachine")
    elif "open paint" in ai:
        ap.open("Paint")
    elif "search" in ai:
        ai = input("wat wilt u specifiek opzoeken op google? ")
        web.open("https://www.google.com/search?q=" + ai)
    elif ai == "clear":
        clear_screen()
    elif "open whatsapp" in ai:
        ai = input("de web versie of de app (web/app)? ")
        if ai == "web":
            web.open("https://web.whatsapp.com/")
        elif ai == "app":
            ap.open("WhatsApp")
    elif "open vs" in ai:
        ap.open("Visual Studio Code")
    elif "verander" and "kleur" in ai:
        change_color()
    elif "open" and "app" in ai:
        ai = input("welk app wil je openen? ")
        ap.open(ai)
    elif "wat is" in ai:
        wikip = input("wilt u iets opzoeken op wikipedia? (ja/nee) ")
        if wikip == "ja":
            wikip = ai
            wikip.replace("wat is", " ")
            print(wiki.summary(wikip))
            ai = input("wilt u nog meer opzoeken informatie over dit onderwerp? (ja/nee) ")    
            if ai == "ja":
                print(wiki.page(wikip).content)
    elif "install" in ai:
        install()
    elif "nieuws" in ai:
        news(ai)
    elif "vertaal" in ai:
        whattranslate = input("wat wilt u vertalen? ")
        print(googletrans.LANGUAGES)
        langtranslate = input("welke taal wilt u vertalen?(je kiest 1 van de bovenstaande afkortingen) ")
        print(translate(whattranslate, langtranslate))
    elif "weer" in ai:
        weather()
    elif "url" and "klein" in ai:
        klein_url()
    elif ai == "help":
        lijst = ["stop: stopt het programma", "open gmail: opent de gmail website", "open youtube: opent de youtube website", "open facebook: opent de facebook website", "open google: opent de website van google", "open kladblok: opent de app kladblok", "open rekenmachine: opent de app rekenmachine", "open paint: opent de app paint", "search: zoekt iets op op google", "clear: maakt het scherm leeg", "help: een lijst van alle commands", "open whatsapp: opent de whatsapp website/app", "open vs: opent de app Visual Studio Code", "verander kleur: verandert de kleur van de tekst", "open app: opent een app naar keuze", "zoek op wikipedia door wat is: zoekt iets op op wikipedia(wat achter wat is is)", "install app: installeert een app", "vertaal: vertaalt een tekst naar keuze", "nieuws: laat de laatste nieuwsberichten zien", "weer: laat het weer zien van een plaats naar keuze", "url verkorten:verkort een url naar keuze(je moet ook https:// in je url zetten)", "ip: laat de locatie van een IP adres zien", "recept: laat het recept van een gerecht zien()", "iss"]
        print("\n".join(lijst))
    elif "ip" in ai:
        ai = input("Wil je de locatie van een IP adres zien? ")
        if "ja" in ai:
            ip_tracker()
    elif "recept" in ai:
        recept()
    elif "iss" in ai:
        ISS()
    elif ai == "":
        pass
    else:
        print("dit commando bestaat niet")
        print("Dit is nog in het begin van mijn werk en wat jij net hebt ingetypt wordt hopelijk later toegevoegd.\nschrijf help voor alle commands")







print("klaar")
exit()
