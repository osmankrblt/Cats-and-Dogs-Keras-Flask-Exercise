from flask import Flask,render_template,request,flash
import cv2
import os
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np

ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
UPLOADED_FILE_NAME = "uploadedImage.png"
STATIC_FOLDER='static'

app = Flask(__name__,)

app.config['STATIC_FOLDER'] = STATIC_FOLDER


if os.listdir(app.config['STATIC_FOLDER'])!= []:
     os.remove(os.path.join(STATIC_FOLDER,UPLOADED_FILE_NAME))
    

model = load_model("model/myModel.h5")




def predictImage(image, model):
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    result = np.squeeze(model.predict(np.array(image)))

    index = np.argmax(result)

    if result[index] < 0.6:
        return "None Type"

    return "Cat" if index == 0 else "Dog"

def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def upload():
    if 'file' not in request.files:
        flash('No file part')
        return render_template("mainPage.html")
    file = request.files['file']
       
        
    if file.filename == '':
        flash('No selected file')
        return  render_template("mainPage.html") 

    if file and allowed_file(file.filename):
            
            
        file.save(os.path.join(app.config['STATIC_FOLDER'], UPLOADED_FILE_NAME))
        return True
    return False

def predict():
    
    imgPath = os.path.join(STATIC_FOLDER, UPLOADED_FILE_NAME)

    selectedImage = cv2.resize(cv2.imread(imgPath),(224,224))
        
    result =  predictImage(selectedImage,model)
        
   
    return imgPath,result
 
  

@app.route('/',methods=['POST',"GET"])
def home():
    if request.method == 'POST' and upload():
       
        selectedImage,result = predict()
   
        return render_template("mainPage.html",result=result,selectedImage=selectedImage) 
    
    return render_template("mainPage.html") 
    
        
if __name__ == '__main__':
    app.run(debug=True)

