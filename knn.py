#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import sys
import numpy
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.datasets import load_svmlight_file
from sklearn import preprocessing
import pylab as pl
import matplotlib.pyplot
import numpy as np

def main(data):

        # loads data
        print ("Loading data...")
        X_data, y_data = load_svmlight_file(data)
        # splits data
        print ("Spliting data...")
        X_train, X_test, y_train, y_test =  train_test_split(X_data, y_data, test_size=0.5, random_state = 5)

        X_train = X_train.toarray()
        X_test = X_test.toarray()

        # fazer a normalizacao dos dados #######
        #scaler = preprocessing.MinMaxScaler()
        #X_train = scaler.fit_transform(X_train_dense)
        #X_test = scaler.fit_transform(X_test_dense)
        
        # cria um kNN
        vet_k = []
        vet_acur = []
        for k in range(3,31):
                print('Para k=',k)
                neigh = KNeighborsClassifier(n_neighbors=k, metric='euclidean', n_jobs = -1)

                neigh.fit(X_train, y_train)

                # predicao do classificador
                y_pred = neigh.predict(X_test)

                # mostra o resultado do classificador na base de teste
                print ('Accuracy: ',  neigh.score(X_test, y_test))

                vet_k.append(k)
                vet_acur.append(neigh.score(X_test, y_test))

                # cria a matriz de confusao
                cm = confusion_matrix(y_test, y_pred)
                print (cm)
                print(classification_report(y_test, y_pred, labels=[0,1,2,3,4,5,6,7,8,9]))

        matplotlib.pyplot.xlabel('K')
        matplotlib.pyplot.ylabel('Accuracy')
        matplotlib.pyplot.plot(vet_k, vet_acur)
        matplotlib.pyplot.show()
       

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("Use: knn.py <data>")

        main(sys.argv[1])
     




