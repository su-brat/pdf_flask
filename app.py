from flask import Flask
from flask_restful import Resource, Api 
from resources.api.pdf_search import PDFSearch

app = Flask(__name__)
api = Api(app)

@app.route("/")
def welcome():
    return "<p>This is a PDF search service API implemented in Flask</p>"

api.add_resource(PDFSearch, "/api/pdf-search")

if __name__=="__main__":
    app.run(port=5000)