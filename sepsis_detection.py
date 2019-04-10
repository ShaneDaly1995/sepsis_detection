import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class dataset:
    def read_file(filename):
        array = pd.read_csv(filename, delimiter="|")
        return array
    
    def concatenate_datasets():
        vitals = pd.DataFrame()
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
            
            # cleaned_data = dataset.calculations(data)
            dataset.percentage(x)
            
            vitals = vitals.append(data, ignore_index=True)
            # print("{} files processed.".format(x))
        return vitals
    
    def calculations(data):
        # filter the dataset
        filteredDF = data.filter(['HR', 'O2Sat', 'Temp', 'Resp', 'Age', 'Gender', 'SepsisLabel'])
        print(filteredDF["SepsisLabel"])
        
        columns = ['HR', 'O2Sat', 'Temp', 'Resp', 'Age', 'Gender', 'SepsisLabel']
        averagedData = pd.DataFrame(columns=columns)
       
        # get the average of each column
        averagedData.loc["HR"] = filteredDF["HR"].mean()
        averagedData.loc["O2Sat"] = filteredDF["O2Sat"].mean()
        averagedData.loc["Temp"] = filteredDF["Temp"].mean()
        averagedData.loc["Resp"] = filteredDF["Resp"].mean()
        averagedData.loc["Age"] = filteredDF["Age"].mean()
        averagedData.loc["Gender"] = filteredDF["Gender"].mean()
        averagedData.loc["SepsisLabel"] = filteredDF["SepsisLabel"]
        # print(averagedData)
        return averagedData
        
    def percentage(part):
        whole = 5000
        ans = 100 * part/whole
        print("{:.0f}%".format(ans))
        
    
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
    print(len(data))
    print(data.values)
    list(data.columns.values)
    # train, test = dataset.tts(data)
    

main()