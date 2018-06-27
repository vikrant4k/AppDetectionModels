from SaveModels import SaveModels
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import svm
class BaggingClassifier:

    def __init__(self, key):
        model = SaveModels.readModel(key, "bagging")
        if (model is not None):
            print("File Model Used")
            self.clf = model
        else:
            print("New Model Created")
            self.clf=GradientBoostingClassifier(n_estimators=200,max_depth=7)

    def train(self, userData, output):
        print("SVM Fitting started ")
        self.clf.fit(userData, output)

    def saveModel(self, key):
        SaveModels.saveModel(key, self.clf, "bagging")

    def predict(self, userData):
        userData = np.reshape(userData, (1, -1))
        return self.clf.predict(userData)

    def predictProbability(self, userData):
        userData = np.reshape(userData, (1, -1))
        probability = self.clf.predict_proba(userData)
        probability = np.reshape(probability, (probability.shape[1]))
        ##probability=probability.tolist()
        ##print(probability)
        problList = []
        for i in range(0, len(probability)):
            temp = []
            temp.append(probability[i])
            temp.append(i)
            problList.append(temp)
        ##print(problList)
        for i in range(0, len(problList)):
            for j in range(i + 1, len(problList)):
                if (problList[i][0] < problList[j][0]):
                    temp = problList[i]
                    problList[i] = problList[j]
                    problList[j] = temp
        indexs = []
        for i in range(0, 4):
            indexs.append(problList[i][1])
        return indexs