
from flask import *
import os 

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

@app.route('/upload' , methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER,filename))
    return 'File uploaded succesfully'

@app.route('/download/<filename>' , methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER , filename , as_attachment =True )

app.run()