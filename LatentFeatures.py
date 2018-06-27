from sklearn.decomposition import PCA
class LatentFeatures:

   def __init__(self):
       self.pca=PCA(0.97)

   def fitData(self,fetaureData):
       self.pca.fit(fetaureData)

   def transformData(self,transformData):
       return self.pca.transform(transformData)

