import numpy as np
from os import listdir

def read_img(path):
    """
    read and convert data from img
    """
    data = open(path).read().replace("\n","")
    return np.array([int(item) for item in data])

def PCA():
    '''
    PCA procedure
    '''
    path = "D:/digits/testDigits"
    ims = []
    for pim in listdir(path):
        ims.append(read_img(path+'/'+pim))
    ims = np.array(ims)
    cov = np.dot(ims,ims.T)
    div = []
    for i in range(len(cov)):
        div.append(cov[i]/946)
    
    print(np.linalg.eig(div))


PCA()
