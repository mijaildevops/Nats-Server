from flask import Flask, request
from flask import render_template
from flask import jsonify

import requests
# DB
#import pymysql

import json
import os

# GUID
import uuid 

# Cors
from flask_cors import CORS

# Mkdir
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# FecHa
from datetime import date
from datetime import datetime

# Cors access
app=Flask(__name__,template_folder='templates')
cors = CORS(app)

# Numero Random
import random2

# Email 
#import smtplib


from datetime import datetime
now = datetime.utcnow() 


#//////////////////////////////////////////////////////////////////////////
# Index
#//////////////////////////////////////////////////////////////////////////
@app.route('/')
def home():
    return 'Api Rest External (App V3)'


#//////////////////////////////////////////////////////////////////////////
# Index
#//////////////////////////////////////////////////////////////////////////
@app.route('/FaceDetetion')
def NatsFace():
    #///////////////////////////////////////////
    # Generamos Un GUID 
    #///////////////////////////////////////////
    IdUnico = uuid.uuid4()
    imageid = str(IdUnico)

    Temperature = [98.6, 96.26, 95, 103.1, 102.2, 97.34, 100.4, 100.22, 97.52, 95.36]
    confidence = [0.9998735189437866, 0.9535711189237866, 0.8598735189437866, 0.7298735189437866, 0.9398735189437866, 0.7998735189437866]
    position = [[132,41], [385,609], [785,206], [405,38], [789,321], [415,552]]
    size = [[222,303], [258,352], [234,314], [259,395], [199,287], [276,315]]
    Fecha=str(now.strftime("%Y-%m-%d %H:%M:%S.%f"))


    #varr = '{"detections": [{ "Temperature":"98.6","FaceDetector": { "confidence": 0.9998735189437866,"image_id": 0.0, "label": 1,"position": [132,41],"size": [222,303 ]},"LandmarksDetector": { "left_eye": [134,147],"left_lip_corner": [ 136, 242],"nose_tip": [210,204 ],"right_eye": [300,145],"right_lip_corner": [307,240]}, "PoseEstimator": {"ypr": [-3.50416898727417,3.2856898307800293,-0.45209193229675293] },"FrameTimestamp":"UTC Time" } " '
    return jsonify({ "detections": {"Temperature": random2.choice(Temperature), "FaceDetector": {"confidence": random2.choice(confidence), "image_id": imageid, "label": 1,  "position": random2.choice(position), "size": random2.choice(size) , "LandmarksDetector": {"left_eye": [ 134,147], "left_lip_corner": [136,242],"nose_tip": [210,204 ], "right_eye": [300,145],"right_lip_corner": [307,240]}, "PoseEstimator": {"ypr": [-3.50416898727417, 3.2856898307800293,-0.45209193229675293] } },"FrameTimestamp": Fecha}})
    #return jsonify (varr)


#***************************************************************************
#//////////////////////////////////////////////////////////////////////////
# Host Api
#//////////////////////////////////////////////////////////////////////////
#***************************************************************************
if __name__ == '__main__':
    app.run(host='192.168.100.51', port=5080, debug=True)