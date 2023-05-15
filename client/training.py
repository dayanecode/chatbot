# -*- coding: utf-8 -*-

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('data.json').read()
intents = json.loads(data_file)


for intent in intents['intents']:
    for pattern in intent['patterns']:

        #tokenize cada palavra
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #adicionar documentos no corpus
        documents.append((w, intent['tag']))

        # adicionar à nossa lista 
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmaztize e minimiza cada palavra e remova duplicatas
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
# documents = combinação entre padrões e intents
print (len(documents), "documents")
# classes = intents
print (len(classes), "classes", classes)
# words = todas as palavras, vocabulário
print (len(words), "unique lemmatized words", words)


pickle.dump(words,open('texts.pkl','wb'))
pickle.dump(classes,open('labels.pkl','wb'))

# criar nossos dados de treinamento
training = []
# create an empty array for our output
output_empty = [0] * len(classes)
# conjunto de treinamento, pacote de palavras para cada frase
for doc in documents:
    # inicializa nosso pacote de palavras
    bag = []
    # lista de palavras tokenizadas para o padrão
    pattern_words = doc[0]
    # lematize cada palavra - cria palavra base, na tentativa de representar palavras relacionadas
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # cria nosso array bag of words com 1, se a correspondência de palavras for encontrada no padrão atual
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    # a saída é um '0' para cada tag e '1' para a tag atual (para cada padrão)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])
# embaralhar nossos recursos e transformá-los em np.array
random.shuffle(training)
training = np.array(training)
# criar listas de treinamento e teste. X - padrões, Y - intenções
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")


# Criar modelo - 3 camadas. Primeira camada 128 neurônios, segunda camada 64 neurônios e 3ª camada de saída contém número de neurônios
# igual ao número de tentativas para prever a intenção de saída com softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compilar o modelo. A descida de gradiente estocástico com gradiente acelerado de Nesterov dá bons resultados para este modelo
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#ajustando e salvando o modelo
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('model.h5', hist)

print("model created")