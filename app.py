from flask import Flask,request,render_template
import os
from main import run_eda
app = Flask(__name__)
UPLOAD_FOLDER = 'data'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure required directories exist (Crucial for cloud deployments like Render)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static/outputs', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        file=request.files['file']
        filepath=os.path.join(app.config["UPLOAD_FOLDER"],file.filename)
        file.save(filepath)
        results=run_eda(filepath)
        return render_template("result.html",results=results)
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)