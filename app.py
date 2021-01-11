# active.bare is the location of image!!
# active.juan is Recolor

import os

from cs50 import SQL
import subprocess
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField
from tempfile import mkdtemp
from werkzeug.utils import secure_filename
import PIL
from PIL import Image, ImageFilter, ImageChops
import matplotlib.pyplot as plt
from flask_caching import Cache

app = Flask(__name__)
app.debug = True
app.run()
app.config["TEMPLATES_AUTO_RELOAD"] = True
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# For more configuration options, check out the documentation
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/examples.html")
def example():
    return render_template("examples.html")

app.config["IMAGE_UPLOADS"] = "C:/Users/ab/Documents/GitHub/picture-website/static/saved"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]
def allowed_image(filename):
    
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/active", methods=["GET", "POST"])
@app.route("/active.html", methods=["GET", "POST"])
def active():
    if request.method == "POST":

        if request.files:
            
            image = request.files["image"]
            
            if image.filename == "":
                return render_template("active.html", message="Image must have a filename")
                
            if not allowed_image(image.filename):
                return render_template("active.html", message="This image is not valid")
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                active.bare = "".join(["static/", filename])
                active.juan = "".join(["python colorization/demo_release.py -i static/", filename, " -o static/"])
                active.jose = "".join(["glitch_this -f -c -g ./static/", filename, " 5 -o ./static/glitched"])

            return render_template("active.html", message="Image saved")
        
    return render_template("active.html")


class ChooseForm(FlaskForm):
    choices = SelectField('choices', choices=[ ('Blur'), ('Grayscale'), ('Inversion'), ('Reflect'), ('Recolor'), ('Glitch') ])

@app.route("/choices", methods=["GET", "POST"])
@app.route("/choices.html", methods=["GET", "POST"])
def choices():

    form = ChooseForm()
    if request.method == "POST":
        fm = form.choices.data
        image = Image.open(active.bare)

        if fm == "Blur":
            blurred_image = image.filter(ImageFilter.BoxBlur(10))
            blurred_image.save("static/blurred.jpg")
            message = "blur"
        
        if fm == "Grayscale":
            gray_image = image.convert('L')
            gray_image.save("static/grayscale.jpg")
            message = "grayscale"
        
        if fm == "Inversion":
            invert_image = ImageChops.invert(image)
            invert_image.save("static/inverted.jpg")
            message = "invert"
        
        if fm == "Reflect":
            reflected_image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            reflected_image.save("static/reflected.jpg")
            message = "reflect"

        if fm == "Recolor":
            os.system(active.juan)
            message = "recolor"

        if fm == "Glitch":
            os.system(active.jose)
            message = "glitch"

        return render_template("choices.html", form=form, message=message)
    else:
        return render_template("choices.html", form=form)

        # need to get their file, and for which thingy they are uploading as well
        # will probably need a request.form.get for EACH upload type"""

if __name__ == "__main__":
    socketio.run(app)