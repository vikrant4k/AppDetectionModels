import pickle
import os.path
class SaveModels:

    def __init__(self):
        print("save model initiated")

    def saveModel(key,model,modelName):
        with open(key+modelName+'.pkl', 'wb') as output:
            pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)

    def readModel(key,modelName):
        if(os.path.exists(key+modelName+'.pkl')==True):
            with open(key+modelName+'.pkl', 'rb') as pickle_file:
                model = pickle.load(pickle_file)
            return model
        else:
            return None
