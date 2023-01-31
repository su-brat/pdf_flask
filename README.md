###API endpoint:
`/api/pdf-search`

###Example query urls:
- GET `localhost:5000/api/pdf-search?search-term=Visual Basic,MS Office&pdf-abs-path=D:\pdf-search-python\resume-sample.pdf`
- GET `localhost:5000/api/pdf-search?search-term=MS Office&pdf-abs-path=D:\pdf-search-python\resume-sample.pdf`

**Note**: `search-term` and `pdf-abs-path` query parameters are required to make a successful API call.