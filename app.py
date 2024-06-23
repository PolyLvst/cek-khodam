from flask import Flask,render_template,jsonify,request
from logging.handlers import RotatingFileHandler
from datetime import datetime
import logging
import random
import json
import os

app = Flask(__name__)
with open("./khodams.json","r") as data:
    khodams = json.load(data)["khodam_names"]
# Configure logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route("/",methods=["GET"])
def home():
    app.logger.info("GET / HTTP/1.1")
    return render_template("index.html")

@app.route("/q",methods=["GET"])
def q():
    name = str(request.args.get("name"))
    app.logger.info("GET /q?name="+name+" HTTP/1.1")
    app.logger.info("#: "+name+" :#")
    name = name+datetime.now().strftime("%d-%m-%Y")
    # Check if saved khodams is exist
    if os.path.exists("./khodams_saved.json"):
        app.logger.info("Opening save khodams")
        # Get all previous generated khodams
        with open("./khodams_saved.json","r") as data:
            khodam_prev = json.load(data)
        # Get the khodam of name
        khodam = khodam_prev.get(name)
        # Check if exist
        if not khodam:
            app.logger.info("User doesnt have khodam today")
            khodam = random.choice(khodams)
            with open("./khodams_saved.json","w") as data:
                khodam_prev[name] = khodam
                json.dump(khodam_prev,data)
            app.logger.info("Saved khodams updated")
            # Save khodam for that name
    else:
        app.logger.info("User getting random khodam")
        khodam = random.choice(khodams)
        with open("./khodams_saved.json","w") as data:
            khodam_prev = {name:khodam}
            json.dump(khodam_prev,data)
        app.logger.info("Khodams save file created")
    return jsonify({"name":name,"khodam":khodam})

if __name__ == "__main__":
    app.run("0.0.0.0","5000",True)