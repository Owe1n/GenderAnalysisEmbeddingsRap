import os
from tqdm import tqdm
import spacy

nlp = spacy.load("en_core_web_md")
import_dir = "../NewYorkTimeScrapper/Result"


def preprocess(text):
    # Tokenize the text
    doc = nlp(text)
    # Lemmetize
    tokens = [token.lemma_ for token in doc]
    # Remove punctuation and non-alphabetic characters
    tokens = [token.text for token in doc if token.is_alpha and not token.is_punct]

    # Lowercase the tokens
    tokens = [token.lower() for token in tokens]

    # Remove stop words
    tokens = [token for token in tokens if token not in nlp.Defaults.stop_words]

    

    # tokens = [token.lemma_ for token in doc] Need to decided wheter lemmatize or not
    # Return the preprocessed tokens
    return tokens


decades = {"1990": "", "2000": "", "2010": ""}

for file_name in os.listdir(import_dir):
    year = file_name.split(".")[0]
    if int(year) < 1990 or int(year) >= 2020:
        continue
    decade = year[:3] + "0"
    with open(os.path.join(import_dir, file_name), "r") as f:
        if decade in decades:
            text = f.read()
            nb_line = 0
            for line in tqdm(text.splitlines()):
                if nb_line == 5001:
                    break
                preprocessed_line = ""
                doc = nlp(line)
                for token in preprocess(doc):
                    preprocessed_line += token + " "
                decades[decade] += preprocessed_line
                nb_line += 1
for decade in decades:
    with open(f"{decade}_document", "w") as f:
        f.write(decades[decade])
    print(f"Decade: {decade} Document saved as {decade}_document")
