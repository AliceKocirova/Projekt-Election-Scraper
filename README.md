

# Engeto-pa-3-projekt

Třetí projekt na Python Akademii od Engeta. 

# Popis projektu

Tento projekt slouží k automatickému stažení a zpracování výsledků voleb do Poslanecké sněmovny 2017 pro okres Prostějov.
Výsledkem je CSV soubor s kompletními daty za všechny obce a všechny politické strany.


# Instalace knihoven

requests — pro stažení HTML obsahu

BeautifulSoup (bs4) — pro parsování HTML

csv — pro zápis výstupu

os — pro otevření výsledného souboru

pip install requests beautifulsoup4


Stažení volebních dat z volby.cz

Zpracování výsledků za všechny obce

Vygenerování čistého CSV souboru připraveného k otevření v Excelu

Automatické otevření výsledného souboru po stažení

# Použité knihovny



requests — pro stažení HTML obsahu

BeautifulSoup (bs4) — pro parsování HTML

csv — pro zápis výstupu

os — pro otevření výsledného souboru

sys - pro zpracování argumentů příkazové řádky


Před spuštěním jsem si  nainstalovala knihovny příkazem:

pip install -r requirements.txt
pip install beautifulsoup4

# Spuštění programu

Program spouštíte pomocí dvou argumentů příkazové řádky:

URL — odkaz na stránku s výsledky daného územního celku.

Název výstupního souboru — např. vysledky_prostejov.csv.

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" 
"vysledky_prostejov.csv"

# Průběh stahování 

kontroluji obce

Nalezeno 97 obcí

Názvy politických stran

Zpracovávám 97 obcí...

Hotovo! Data jsou uložená ve vysledky_prostejov.csv.



# Výstup
Program vytvoří CSV soubor se strukturou:

code	location	registered	envelopes	valid	Občanská demokratická strana	ANO 2011	SPD	...
506761	Alojzov	       205	      145	     144	   29	                            32	    15	...
589322	Brodek     	  1224	      656	     655	   54	                           02   	107	...













