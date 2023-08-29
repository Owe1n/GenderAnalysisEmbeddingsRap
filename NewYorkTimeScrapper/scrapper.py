import pandas as pd
import os

folder_path = "NYTA/"

# create a dictionary to store the sentences by year
sentences_by_year = {}

# iterate over all csv files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        df = pd.read_csv(folder_path + file_name)
        for index, row in df.iterrows():
            year, sentence = row["year"], row["sentence"]
            # add the sentence to the dictionary, using the year as key
            if year in sentences_by_year:
                sentences_by_year[year].append(sentence)
            else:
                sentences_by_year[year] = [sentence]


# write the sentences to separate files for each year
for year in sentences_by_year:
    filename = str(year) + ".txt"
    with open(filename, "w", encoding="utf-8") as file:
        for sentence in sentences_by_year[year]:
            file.write(sentence + "\n")
