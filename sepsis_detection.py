import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class dataset:
    def read_file(filename):
        array = pd.read_csv(filename, delimiter="|")
        return array
    
    def concatenate_datasets():
        raw_data =  pd.DataFrame()
        training_directory = "training/"
        training_filename = "p"
        training_extension = ".psv"
        
        for x in range(1,5001):
            if x < 10:
                name = "{}{}0000{}{}".format(training_directory, training_filename, x, training_extension)
                data = dataset.read_file(name)
            elif x >= 10 and x < 100:
                name = "{}{}000{}{}".format(training_directory, training_filename, x, training_extension)
                data = dataset.read_file(name)
            elif x >=100 and x < 1000:
                name = "{}{}00{}{}".format(training_directory, training_filename, x, training_extension)
                data = dataset.read_file(name)
            else:
                name = "{}{}0{}{}".format(training_directory, training_filename, x, training_extension)
                data = dataset.read_file(name)
                
            raw_data = raw_data.append(data, ignore_index=True)
            print("{} files processed.".format(x))
        return raw_data
    
    def tts(raw_data):
        train, test = train_test_split(raw_data, test_size=0.3, random_state=42)
        
        trainVals = train[:,:-1]
        trainTarget = train[:,-1]        
        testVals = test[:,:-1]
        testTarget = test[:,-1]
        
        
        ## Instantiate the model with 5 neighbors. 
        knn = KNeighborsClassifier(n_neighbors=5)
        ## Fit the model on the training data.
        knn.fit(trainVals, trainTarget)
        ## See how the model performs on the test data.
        knn.score(testVals, testTarget)


def main():
    data = dataset.concatenate_datasets()
    train, test = dataset.tts(data)
    

main()