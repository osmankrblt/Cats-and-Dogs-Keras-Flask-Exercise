from keras.applications.vgg16 import preprocess_input
import numpy as np


def  predictImage(image,model):

    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
   
    result = np.squeeze(model.predict(np.array(image)))

    index = np.argmax(result)
    
  
    if result[index]<0.6:
        return "None Type"

    return   "Cat" if index == 0 else "Dog"