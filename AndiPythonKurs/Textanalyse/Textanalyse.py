import os
import csv
import statistics

#vars
Text = []
word_length_values = []

def analyze_text(Text):



    # Text Importieren
    if not os.path.isfile('Text.csv'):
        print("ERROR FILE not found")
        exit()

    with open('Text.csv', 'r') as datafile:
        for line in datafile:
            words = line.split()
            Text.extend(words)

    #Durchschnittslänge Wörter
    for length in Text:
        word_length = (len(length))
        word_length_values.append(int(word_length))

    #Kürzestes Wort und die länge des Wortes
    min_word = word_length_values.index(min(word_length_values))
    print(Text[min_word])





analyze_text(Text)


#Ausgaben

print(Text)

#Anzahl Wörter
print(f"Der Text enthält {len(Text)} Wörter.")

#Durchschnittslänge Wörter
print(statistics.median(word_length_values))

#Kürzestes Wort und die länge des Wortes
print(min(word_length_values))
