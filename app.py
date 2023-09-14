from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
import torch
from torchvision import transforms
from model import MnistModel

app = Flask(__name__)

upload_folder = 'uploads'
app.config['UPLOAD_FOLDER'] = upload_folder

file_counter = 0

###### MODEL ######
model = MnistModel()
model.load_state_dict(torch.load('models/MNIST_HWDR_2D-feedforward.pth', map_location=torch.device('cpu')))
model.eval()

transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28,28)),
    transforms.ToTensor(),
])

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    global file_counter

    if 'image' not in request.files:
        return "No File Found"

    file = request.files['image']

    if file.filename == '':
        return "No File Selected"
    
    if file:
        file_counter +=1
        filename = os.path.join(app.config['UPLOAD_FOLDER'], str(file_counter) + '.jpg')
        file.save(filename)

        with Image.open(filename) as img:
            img = transforms(img)
            img = img.unsqueeze(0)
            img = img.float()


        with torch.no_grad():
            prediction = model(img)

        predicted_class = torch.argmax(prediction).item()
        print(predicted_class)
        class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        return render_template('index.html', prediction=class_names[predicted_class])

if __name__ == '__main__':
    app.run(debug=True)