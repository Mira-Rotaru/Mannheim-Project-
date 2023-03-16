import os
from flask import Flask, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r'C:\Users\Rotaru Mira\Documents\flask_app\static\images'
ALLOWED_EXTENSIONS = {'dcm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/file/upload', methods=['GET','POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'media not provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'no file uploaded'}), 400
    elif file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        #file_size = os.stat(file)
        #print(f'File Size in MB: {file_size.st_size/(1024*1024)}')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        print('File path' + file_path)
        print(f'File size in Bytes: {os.path.getsize(file_path)}' )
        return jsonify({"message": 'file successfully uploaded'})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)