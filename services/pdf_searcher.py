import PyPDF2

def search_for(search_term, file_path):
    reader = PyPDF2.PdfReader(file_path)
    result = {
        "pages": [],
        "content": search_term
    }
    for page_index in range(0, len(reader.pages)):
        page = reader.pages[page_index]
        page_number = page_index + 1
        page_content = page.extract_text()
        if search_term in page_content:
            result["pages"].append(page_number)
    return result

def search_for_multiple(search_terms, file_path):
    result_hashmap = {
        search_term: {
            "content": search_term,
            "pages": []
        } for search_term in search_terms
    }
    reader = PyPDF2.PdfReader(file_path)
    for page_index in range(0, len(reader.pages)):
        page = reader.pages[page_index]
        page_number = page_index + 1
        page_content = page.extract_text()
        for search_term in search_terms:
            
            if search_term in page_content:
                result_hashmap[search_term]["pages"].append(page_number)
    result_list = list(result_hashmap.values())
    return result_list

if __name__=="__main__":
    search_term = input("Provide search term: ")
    file_path = "resume-sample.pdf"
    print(search_for(search_term, file_path))
    print(search_for_multiple(["MS Office", "Visual Basic"], file_path))
    