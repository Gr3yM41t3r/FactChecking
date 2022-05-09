import csv
import urllib
from time import strftime

import spacy
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import datefinder
import nltk


"""
# foction de netyoyage de obama says --> reste a voir s'il exite des phrases de type "..." a dit Obama
def clean(sentence):
    doc = nlp(sentence)
    for word in doc:
        if stemmer.stem(word.text) == 'say':
            print(sentence)
            sentence = sentence[word.idx + len(word) + 1:]
            print(sentence)
"""

claims = []
claims.append("Hillary Clinton says she helped usher Iran to the negotiating table")
claims.append("In his first TV interview as president, Obama said we ''should talk to Iran")
claims.append("Paul Begala says Mitt Romney said he would pay no taxes under Paul Ryan's tax plan")


# fonction de nettoyage avec spacy
def nettoyage(sentences):
    # selection de la racine de chaque phrase
    document = list(nlp(sentences).sents)
    sentence_root = []
    for sentence in document:
        if sentence.root is not None:
            sentence_root.append(sentence.root)

    # selection des elements a supprimer
    for roo in sentence_root:
        elmt_to_rmv = [roo]
        for child in roo.children:
            if child.dep_ == 'nsubj':
                elmt_to_rmv.append(child)
        for c in elmt_to_rmv:
            if c != roo and [elem for elem in c.children] is not []:
                c2 = [c for c in c.children]
                if len(c2) == 1:
                    elmt_to_rmv.append(c2[0])

        # supression
        newsentences = ''
        for token in nlp(sentences):
            if token.idx not in [e.idx for e in elmt_to_rmv]:
                if len(newsentences) < 1:
                    newsentences = str(token)
                else:
                    newsentences += ' ' + str(token)
        return newsentences


'''
#displacy.serve(nlp(claims[0]), style="dep")
for cl in claims:
    print(cl,"...",nettoyage(cl))
'''

########################### AJOUT AUTEUR+DATE #################################

csvfile = 'inputCSV/claims_prof_3.csv'
csvoutput= 'outputCSV/test.csv'
with open(csvfile) as inputData, open(csvoutput, 'w+') as fout:
    header = ["Annotations","Score","CR Author A","CR Author B","Review URL A","Review URL B",
    "Text Fragments A","Text Fragments B"",Entities A","Entities B", "Keywords A", "Keywords B",
    "Author Text A", "Author Text B", "Date Text A", "Date Text B", "Url A keywords", "Url B keywords"]
    writer = csv.writer(fout)
    reader = csv.reader(inputData)
    claims = list(reader)
    writer.writerow(header)
    for row in claims:
        print(row[4][11])
        if row[4][11]!="p":
            pass
        else:
            col = []
            url = row[4]
            url2 = row[5]
            print(url, url2)
            
            # suppression des 4 dernieres colonnes
            row = row[:-4]

            # ouverture de la page
            page = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
            page2 = urlopen(Request(url2, headers={'User-Agent': 'Mozilla'}))
            # on charge le code la page
            codedelap = bs(page,features="html.parser")
            codedelap2 = bs(page2,features="html.parser")

            # recuperation de l'auteur
            nom_auteur= codedelap.find("a", class_="m-statement__name").get_text()
            nom_auteur2= codedelap.find("a", class_="m-statement__name").get_text()
            col.append(nom_auteur[1:-2])
            col.append(nom_auteur2[1:-2])

            # recuperation date
            date_ = codedelap.find("div",class_="m-statement__desc").get_text()
            date_2 = codedelap2.find("div",class_="m-statement__desc").get_text()
            #transformation de la variable de tpe datetime
            match = datefinder.find_dates(date_)
            for m in match:
                col.append(strftime("%Y-%m-%d"))
            match2 = datefinder.find_dates(date_2)
            for m in match2:
                col.append(m.strftime("%Y-%m-%d"))

            #recuperation de la claim
            claim1 = codedelap.find("div", class_="m-statement__quote").get_text()
            claim2 = codedelap2.find("div", class_="m-statement__quote").get_text()
            row[6] = claim1
            row[7] = claim2

            #recupération des mots clés
            listmc=[]
            listmc2=[]
            mc = codedelap.find_all("a", class_="c-tag")
            mc2 = codedelap2.find_all("a", class_="c-tag")
            for lien in mc:
                txt = lien.find("span")
                listmc.append(txt.get_text())
            for lien in mc2:
                txt = lien.find("span")
                listmc2.append(txt.get_text())
            
            print(listmc, listmc2)
            col.append(listmc)
            col.append(listmc2)

            print(col)

            writer.writerow(row + [col])
