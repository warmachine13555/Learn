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

    #Anzahl Wörter
    print(f"Der Text enthält {len(Text)} Wörter.")

    #Durchschnittslänge Wörter
    for length in Text:
        word_length = (len(length))
        word_length_values.append(int(word_length))
    print(f"Die Durchschnittslänge eines Wortes is {statistics.median(word_length_values)}.")

    #Kürzestes Wort und die länge des Wortes
    min_word = word_length_values.index(min(word_length_values))
    min_word_value = min(word_length_values)
    print(f"Das kürzeste Wort ist - {Text[min_word]} - mit der Wortlänge {min_word_value}")

    #Längstes Wort und die länge des Wortes
    max_word = word_length_values.index(max(word_length_values))
    max_word_value = max(word_length_values)
    print(f"Das kürzeste Wort ist - {Text[max_word]} - mit der Wortlänge {max_word_value}")



analyze_text(Text)


