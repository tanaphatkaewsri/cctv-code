
from flask import Flask,render_template,Response,request
import cv2

app=Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bangkokyai')
def bangkokyai():
    return render_template('bangkokyai.html')

@app.route('/dindang')
def dindang():
    return render_template('dindang.html')

@app.route('/dusit')
def dusit():
    return render_template('dusit.html')

@app.route('/huykwang')
def huykwang():
    return render_template('huykwang.html')

@app.route('/jatujak')
def jatujak():
    return render_template('jatujak.html')

@app.route('/patumwan')
def patumwan():
    return render_template('patumwan.html')

@app.route('/payatai')
def payatai():
    return render_template('payatai.html')

@app.route('/rachatewee')
def rachatewee():
    return render_template('rachatewee.html')

@app.route('/yannawa')
def yannawa():
    return render_template('yannawa.html')

@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

# def name():
#     name = input("")
#     print(name)
# a = name()

camera=cv2.VideoCapture("rtsp://admin:admin@10.114.128.39/nph-h264.cgi") #"rtsp://admin:admin@10.114.128.39/nph-h264.cgi"

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__=="__main__":
    app.run(debug=True)

