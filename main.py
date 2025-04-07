

"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Alice Kočířová
email: A.kocirova@gmail.com

import ...

"""

# main.py

import requests
from bs4 import BeautifulSoup
import csv
import os
import sys

def get_obce_links(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    obce_links = []

    tables = soup.find_all('table')
    if not tables:
        raise Exception("Obce nebyly nalezeny")

    base_url = "https://www.volby.cz/pls/ps2017nss/"

    for table in tables:
        rows = table.find_all('tr')[2:]
        for row in rows:
            cells = row.find_all('td')
            if not cells:
                continue
            links = row.find_all('a')
            if links:
                code = cells[0].text.strip()
                location = cells[1].text.strip()
                href = base_url + links[0]['href']
                obce_links.append((code, location, href))

    return obce_links

def get_party_names(obec_url):
    response = requests.get(obec_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    party_names = []

    tables = soup.find_all('table', {"class": "table"})
    for table in tables:
        rows = table.find_all('tr')[2:]

        for row in rows:
            cells = row.find_all('td')
            if cells and len(cells) >= 3:
                party_name = cells[1].text.strip()
                # Vynecháme volební účast
                if party_name and not party_name.replace('%', '').replace(',', '').replace('.', '').isdigit():
                    party_names.append(party_name)

    return party_names

def get_obec_data(obec_url):
    response = requests.get(obec_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    tds = soup.select('td[headers="sa2"], td[headers="sa3"], td[headers="sa6"]')
    registered = tds[0].text.strip().replace('\xa0', '').replace(' ', '')
    envelopes = tds[1].text.strip().replace('\xa0', '').replace(' ', '')
    valid = tds[2].text.strip().replace('\xa0', '').replace(' ', '')

    party_votes = []

    tables = soup.find_all('table', {"class": "table"})
    for table in tables:
        rows = table.find_all('tr')[2:]

        for row in rows:
            cells = row.find_all('td')
            if cells and len(cells) >= 3:
                party_name = cells[1].text.strip()
                if party_name and not party_name.replace('%', '').replace(',', '').replace('.', '').isdigit():
                    votes = cells[2].text.strip().replace('\xa0', '').replace(' ', '')
                    party_votes.append(votes)

    return registered, envelopes, valid, party_votes

def main():
    if len(sys.argv) != 3:
        print("Špatný počet argumentů!")
        print("Použití: python main.py <URL> <název_výstupního_souboru>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    print("kontroluji obce")
    obce_links = get_obce_links(url)

    if not obce_links:
        print("Žádné obce nebyly nalezeny!")
        return

    print(f"Nalezeno {len(obce_links)} obcí.")

    print("Názvy politických stran")
    party_names = get_party_names(obce_links[0][2])

    header = ["code", "location", "registered", "envelopes", "valid"] + party_names
    data = [header]

    print(f"Zpracovávám {len(obce_links)} obcí...")

    for code, location, link in obce_links:
        registered, envelopes, valid, party_votes = get_obec_data(link)
        row = [code, location, registered, envelopes, valid] + party_votes
        data.append(row)

    with open(output_file, mode="w", newline='', encoding="cp1250") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data)

    print(f"Hotovo! Data jsou uložená ve {output_file}.")

    try:
        os.startfile(output_file)
    except Exception as e:
        print(f"Soubor se nepodařilo automaticky otevřít: {e}")

if __name__ == "__main__":
    main()