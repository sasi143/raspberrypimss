from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "App running successfully sasi"
  
  
if __name__ == "__main__":
  app.run(host="0.0.0.0",port="5000")