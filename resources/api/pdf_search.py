from flask_restful import Resource
from flask import request
from services import pdf_searcher


class PDFSearch(Resource):
    def get(self):
        search_term = str(request.args["search-term"]).strip()
        pdf_path = r"{}".format(request.args["pdf-abs-path"]).strip()
        print(pdf_path)
        if ',' in search_term:
            search_terms = list(
                map(lambda search_term: search_term.strip(), search_term.split(',')))
            return pdf_searcher.search_for_multiple(search_terms, pdf_path), 200
        return pdf_searcher.search_for(search_term, pdf_path), 200

    def post(self):
        pass
