from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World! Your Flask app is running successfully on AWS EKS!"

if __name__ == '__main__':
    # חייב להאזין על 0.0.0.0 כדי שיהיה נגיש מחוץ לקונטיינר
    app.run(host='0.0.0.0', port=5000)