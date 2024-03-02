from flask import Flask , request , jsonify , render_template
import pandas as pd
import os 
import requests

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory , "files" , "data.xlsx")
data = pd.read_excel(file_path)




app = Flask(__name__)
@app.route("/")
def index():
    return render_template(current_directory+"/index.html")

if __name__ == '__main__':
    app.run(debug=True)



import sys
input = sys.argv[1]
output = data
print(output)
sys.stdout.flush()