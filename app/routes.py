
from flask import render_template, request
from werkzeug import secure_filename
from PIL import Image
from app import app
#setting the upload folder app->templates->test_images 
##could add a configuration to check for uploaded file formats 
##and filter out files that are not images
UPLOAD_FOLDER = 'app/templates/test_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#main page that comes up first 
@app.route('/')
@app.route('/index')
def index():
	#renders the templade with Choose File and Submit buttons
    return render_template('upload.html', title='Home')

#the page that loads after the upload with function output
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	#requesting the file from the upload
    	f = request.files['file']
    	image_name = f.filename
    	#concatenates file path from upload folder defined above and the image name
    	image_path = app.config['UPLOAD_FOLDER'] + "/" + secure_filename(image_name)
       	#saving the file inside the specified biosight folder 
    	f.save(image_path)
    	#opening image with PIL
    	image = Image.open(image_path)
    	first = 0
    	#testing ability to preform image manipulation; transform the image pixels/data into a list
    	image_data = list(image.getdata()) 
    	for pixel in image_data:
    		if pixel == image_data[0]:
    			first += 1
    	#renders the template for displaying the image manipulation
        return render_template('post.html', count = first)

