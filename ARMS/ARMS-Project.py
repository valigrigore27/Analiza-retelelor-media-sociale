import re

import requests
from bs4 import BeautifulSoup
import sqlite3

# Creăm sau ne conectăm la baza de date
conn = sqlite3.connect('chatbots.db')
c = conn.cursor()

# Creăm tabelul pentru chatbot-uri în baza de date
c.execute('''CREATE TABLE IF NOT EXISTS chatbots
             (nume TEXT, perioada TEXT, baza TEXT, creator TEXT, algoritmi TEXT, tip TEXT, diferente TEXT, asemanari TEXT, invatare TEXT, autonomie TEXT, interfata TEXT, scop TEXT)''')

chatbots = {
    'eliza': 'https://en.wikipedia.org/wiki/ELIZA',
    'alice': 'https://en.wikipedia.org/wiki/Alice_(software)',
    'smarterchild': 'https://en.wikipedia.org/wiki/SmarterChild',
    'ibm watson': 'https://en.wikipedia.org/wiki/Watson_(computer)',
    'siri': 'https://en.wikipedia.org/wiki/Siri',
    'alexa': 'https://en.wikipedia.org/wiki/Amazon_Alexa',
    'jasper ai': 'https://en.wikipedia.org/wiki/OpenAI#GPT',
    'chatgpt': 'https://en.wikipedia.org/wiki/GPT-3',
    'bard': 'https://en.wikipedia.org/wiki/Gemini_(chatbot)'
}

def extract_info(bot_name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    perioada = ""
    baza = ""
    creator = ""
    algoritmi = ""
    tip = ""
    diferente = ""
    asemanari = ""
    invatare = ""
    autonomie = ""
    interfata = ""
    scop = ""

    # Extragem anul in care a fost creat fiecare AI
    try:
        text = soup.get_text()
        match = re.search(r'\b\d{4}\b', text)
        if match:
            perioada = match.group(0)
        else:
            perioada = "Necunoscut"


        if bot_name == 'eliza':
            creator = "Weizenbaum"
            #perioada = "Începutul anilor 1960"
            baza = "Rule-based"
            algoritmi = "N/A"
            tip = "Basic"
            diferente = "Basic chatbot; Lack of advanced NLP"
            asemanari = "Rule-based approach"
            invatare = "Nu"
            autonomie = "Redusă"
            interfata = "Text"
            scop = "Asistență clienți"
        elif bot_name == 'alice':
            creator = "Dr. Richard Wallace"
            #perioada = "1995"
            baza = "AIML (Artificial Intelligence Markup Language)"
            algoritmi = "Rule-based"
            tip = "Basic"
            diferente = "Basic chatbot; Uses AIML"
            asemanari = "Rule-based approach"
            invatare = "Da"
            autonomie = "Redusă"
            interfata = "Text, Vocal"
            scop = "Asistență clienți"
        elif bot_name == 'smarterchild':
            creator = "ActiveBuddy, Inc."
            perioada = "2000"
            baza = "AIML (Artificial Intelligence Markup Language)"
            algoritmi = "Rule-based"
            tip = "Basic"
            diferente = "Basic chatbot; Uses AIML"
            asemanari = "Rule-based approach"
            invatare = "Da"
            autonomie = "Redusă"
            interfata = "Text"
            scop = "Asistență clienți"
        elif bot_name == 'ibm watson':
            creator = "IBM"
            perioada = "2010"
            baza = "Machine Learning"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Conversational"
            diferente = "Conversational agent; ML-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Medie"
            interfata = "Text, Vocal"
            scop = "Asistență clienți, Management informații"
        elif bot_name == 'siri':
            creator = "Apple Inc."
            #perioada = "2011"
            baza = "Machine Learning, Rule-based"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Conversational"
            diferente = "Conversational agent; ML-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Medie"
            interfata = "Vocal"
            scop = "Asistență personală"
        elif bot_name == 'alexa':
            creator = "Amazon"
            #perioada = "2014"
            baza = "Machine Learning, Rule-based"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Conversational"
            diferente = "Conversational agent; ML-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Medie"
            interfata = "Vocal"
            scop = "Asistență personală"
        elif bot_name == 'jasper ai':
            creator = "OpenAI"
            #perioada = "2020"
            baza = "GPT (Generative Pre-trained Transformer)"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Generative"
            diferente = "Generative AI chatbot; GPT-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Înaltă"
            interfata = "Text"
            scop = "Generare de conținut"
        elif bot_name == 'chatgpt':
            # Exemplu pentru ChatGPT
            creator = "OpenAI"
            #perioada = "2020"
            baza = "GPT (Generative Pre-trained Transformer)"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Generative"
            diferente = "Generative AI chatbot; GPT-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Înaltă"
            interfata = "Text"
            scop = "Generare de conținut"
        elif bot_name == 'bard':
            creator = "OpenAI"
            #perioada = "2021"
            baza = "GPT (Generative Pre-trained Transformer)"
            algoritmi = "Deep Learning, Natural Language Processing"
            tip = "Generative"
            diferente = "Generative AI chatbot; GPT-based"
            asemanari = "Advanced NLP capabilities"
            invatare = "Da"
            autonomie = "Înaltă"
            interfata = "Text"
            scop = "Generare de conținut"
    except AttributeError:
        print(f"Nu s-au putut extrage informații pentru {bot_name} de pe pagina {url}")

    return perioada, baza, creator, algoritmi, tip, diferente, asemanari, invatare, autonomie, interfata, scop


for bot_name, bot_url in chatbots.items():
    perioada, baza, creator, algoritmi, tip, diferente, asemanari, invatare, autonomie, interfata, scop = extract_info(bot_name, bot_url)
    c.execute("SELECT COUNT(*) FROM chatbots WHERE nume=?", (bot_name,))
    existing_row = c.fetchone()
    if existing_row[0] == 0:
        c.execute("INSERT INTO chatbots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (bot_name, perioada, baza, creator, algoritmi, tip, diferente, asemanari, invatare, autonomie, interfata, scop))
    else:
        c.execute("UPDATE chatbots SET perioada=?, baza=?, creator=?, algoritmi=?, tip=?, diferente=?, asemanari=?, invatare=?, autonomie=?, interfata=?, scop=? WHERE nume=?", (perioada, baza, creator, algoritmi, tip, diferente, asemanari, invatare, autonomie, interfata, scop, bot_name))


conn.commit()
conn.close()
