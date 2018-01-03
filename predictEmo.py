from PIL import Image
import numpy
from loadModel import loadModel
def predict(imageLocation="p.png"):

    im = Image.open(imageLocation).convert("L")
    numpyArray = numpy.array(im)
    returnList = loadModel(imageArray = numpyArray.flatten())
    print(returnList)

if __name__ == "__main__":
    predict()