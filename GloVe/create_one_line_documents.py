import os
from tqdm import tqdm
import spacy


nlp = spacy.load("en_core_web_md")
import_dir_1990 = "../RapGeniusScrapper/Results1990"
import_dir_2000 = "../RapGeniusScrapper/Results2000"
import_dir_2010 = "../RapGeniusScrapper/Results2010"


decades_1990 = []
decades_2000 = []
decades_2010 = []

current_list = decades_1990

with open("../RapGeniusScrapper/Rappers.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "-----":
            if current_list == decades_1990:
                current_list = decades_2000
            elif current_list == decades_2000:
                current_list = decades_2010
        else:
            current_list.append(line)

# decades_1990 = [
#     "ll cool j",
#     "too $hort",
#     "cypress hill",
#     "the notorious b.i.g.",
#     "bone thugs-n-harmony",
#     "lost boyz",
#     "outkast",
#     "2pac",
#     "m.c. hammer",
#     "a tribe called quest",
# ]
# decades_2000 = [
#     "t.i.",
#     "50 cent",
#     "jay-z",
#     "sean paul",
#     "kanye west",
#     "eminem",
#     "ludacris",
#     "nelly",
#     "lil wayne",
#     "ying yang twins",
# ]
# decades_2010 = [
#     "drake",
#     "nicki minaj",
#     "future",
#     "kendrick lamar",
#     "j. cole",
#     "post malone",
#     "travis scott",
#     "kanye west",
#     "fetty wap",
#     "eminem",
# ]


def preprocess(text):
    # Tokenize the text
    doc = nlp(text)
     # Lemmatize the tokens
    tokens = [token.lemma_ for token in doc]
    # Remove punctuation and non-alphabetic characters
    tokens = [token.text for token in doc if token.is_alpha and not token.is_punct]

    # Lowercase the tokens
    tokens = [token.lower() for token in tokens]

    # Remove stop words
    tokens = [token for token in tokens if token not in nlp.Defaults.stop_words]
   
    # Return the preprocessed tokens
    return tokens


## 1990
for dir_name in tqdm(os.listdir(import_dir_1990)):
    if dir_name not in decades_1990:
        continue
    for file_name in os.listdir(os.path.join(import_dir_1990, dir_name)):
        with open(
            os.path.join(import_dir_1990, dir_name, file_name), "r", encoding="utf-8"
        ) as f:
            text = f.read()
            for line in text.splitlines():
                doc = nlp(line)
                with open("one_line_1990_documents", "a", encoding="utf-8") as r:
                    for token in preprocess(line):
                        r.write(token + " ")
    with open("one_line_1990_documents", "a", encoding="utf-8") as r:
        r.write("\n")
## 2000
for dir_name in tqdm(os.listdir(import_dir_2000)):
    if dir_name not in decades_2000:
        continue
    for file_name in os.listdir(os.path.join(import_dir_2000, dir_name)):
        with open(
            os.path.join(import_dir_2000, dir_name, file_name), "r", encoding="utf-8"
        ) as f:
            text = f.read()
            for line in text.splitlines():
                doc = nlp(line)
                with open("one_line_2000_documents", "a", encoding="utf-8") as r:
                    for token in preprocess(line):
                        r.write(token + " ")
    with open("one_line_2000_documents", "a", encoding="utf-8") as r:
        r.write("\n")
## 2010
for dir_name in tqdm(os.listdir(import_dir_2010)):
    if dir_name not in decades_2010:
        continue
    for file_name in os.listdir(os.path.join(import_dir_2010, dir_name)):
        with open(
            os.path.join(import_dir_2010, dir_name, file_name), "r", encoding="utf-8"
        ) as f:
            text = f.read()
            for line in text.splitlines():
                doc = nlp(line)
                with open("one_line_2010_documents", "a", encoding="utf-8") as r:
                    for token in preprocess(line):
                        r.write(token + " ")
    with open("one_line_2010_documents", "a", encoding="utf-8") as r:
        r.write("\n")
