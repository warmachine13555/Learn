import os
import csv
import statistics

#vars
Text = []
word_length_values = []
min_word = 0
max_word = 0
min_word_value = 0
max_word_value = 0

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
    min_word_value = min(word_length_values)
    print(min_word)
    print(min_word_value)

    #Längstes Wort und die länge des Wortes
    max_word = word_length_values.index(max(word_length_values))
    max_word_value = max(word_length_values)
    print(Text[max_word])
    print(max(word_length_values))




analyze_text(Text)


#Ausgaben

print(Text)

#Anzahl Wörter
print(f"Der Text enthält {len(Text)} Wörter.")

#Durchschnittslänge Wörter
print(statistics.median(word_length_values))

#Kürzestes Wort und die länge des Wortes
print(f"Das kürzeste Wort is {min_word} mit der Wortlänge {min_word_value}")

#Längstes Wort und die länge des Wortes
print(max(word_length_values))
print(Text[max_word])
