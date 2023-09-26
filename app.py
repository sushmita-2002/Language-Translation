from flask import Flask, render_template, send_file


app = Flask(__name__)
UPLOAD_FOLDER = 'static/pdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/school")
def school():
    #pdf_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("school.html")

@app.route("/university")
def university():
    return render_template("university.html")

@app.route("/industry")
def industry():
    return render_template("industry.html")

@app.route("/police")
def police():
    return render_template("police.html")

@app.route("/judiciary")
def judiciary():
    return rendertemplate("judiciary.html")



if __name__ == '__main__': 
   app.run(debug=True)