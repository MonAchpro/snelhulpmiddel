#alles extra
import os
import webbrowser as web
import AppOpener as ap
import wikipedia as wiki
import requests


#dingetjes belangrijk voor de code
wiki.set_lang("nl")
print("dit is een hulpmiddel wat u sneller informatie laat vinden en sneller apps opent. Schrijf help voor alle commands")



#functies
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def change_color():
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


def install():
    app = input("welke app wilt u installeren? ")
    if app == "discord":
        url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
        response = requests.get(url)
        content = response.content
        with open("discord.exe", "wb") as f:
            f.write(content)
        os.startfile("discord.exe")
    elif app == "steam":
        url = "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe"
        response = requests.get(url)
        content = response.content
        with open("steam.exe", "wb") as f:
            f.write(content)
        os.startfile("steam.exe")
    elif app == "spotify":
        url = "https://download.scdn.co/SpotifySetup.exe"
        response = requests.get(url)
        content = response.content
        with open("spotify.exe", "wb") as f:
            f.write(content)
        os.startfile("spotify.exe")
    elif "epic" in app:
        url = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi"
        response = requests.get(url)
        content = response.content
        with open("epic_games.exe", "wb") as f:
            f.write(content)
        os.startfile("epic_games.exe")
    elif app == "vlc":
        url = "https://ftp.halifax.rwth-aachen.de/videolan/vlc/3.0.21/win64/vlc-3.0.21-win64.exe"
        response = requests.get(url)
        content = response.content
        with open("vlc.exe", "wb") as f:
            f.write(content)
        os.startfile("vlc.exe")
    elif "obs" in app:
        url = "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-30.2.2-Windows-Installer.exe"
        response = requests.get(url)
        content = response.content
        with open("obs.exe", "wb") as f:
            f.write(content)
        os.startfile("obs.exe")
    elif app == "virtualbox":
        url = "https://download.virtualbox.org/virtualbox/7.0.20/VirtualBox-7.0.20-163906-Win.exe"
        response = requests.get(url)
        content = response.content
        with open("virtualbox.exe", "wb") as f:
            f.write(content)
        os.startfile("virtualbox.exe")
    elif "google" and "earth" in app:
        url = "https://dl.google.com/tag/s/appguid%3D%7B65E60E95-0DE9-43FF-9F3F-4F7D2DFF04B5%7D%26iid%3D%7B65E60E95-0DE9-43FF-9F3F-4F7D2DFF04B5%7D%26lang%3Dnl%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Earth%2520Pro%26needsadmin%3DTrue%26brand%3DGGGE/earth/client/GoogleEarthProSetup.exe"
        response = requests.get(url)
        content = response.content
        with open("google_earth.exe", "wb") as f:
            f.write(content)
        os.startfile("google_earth.exe")
    elif app == "firefox":
        url = "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
        response = requests.get(url)
        content = response.content
        with open("firefox.exe", "wb") as f:
            f.write(content)
        os.startfile("firefox.exe")
    else:
        print("app niet gevonden")        





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
    elif "open notepad" in ai:
        ap.open("kladblok")
    elif "open calculator" in ai:
        ap.open("Rekenmachine")
    elif "open paint" in ai:
        ap.open("Paint")
    elif "search" in ai:
        ai = input("wat wilt u specifiek opzoeken op google? ")
        web.open("https://www.google.com/search?q=" + ai)
    elif ai == "clear":
        clear_screen()
    elif ai == "help":
        lijst = ["stop", "open gmail", "open youtube", "open facebook", "open google", "open notepad", "open calculator", "open paint", "search", "clear", "help", "open whatsapp", "open vs", "verander kleur", "open app", "zoek op wikipedia door wat is", "install app"]
        print("\n".join(lijst))
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

    else:
        print("dit commando bestaat niet")
        print("Dit is nog in het begin van mijn werk en wat jij net hebt ingetypt wordt hopelijk later toegevoegd.\nschrijf help voor alle commands")







print("klaar")
exit()
