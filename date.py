__author__ = 'wyatt'

def populate():
    booklist = []
    book1 = {"id":"Ql6QgWf6i7cC", "title": "Thinking in JAVA", "authors": "Bruce Eckel",
             "setLink":"https://www.googleapis.com/books/v1/volumes/Ql6QgWf6i7cC",
             "publishedDate": "2003", "categories":"Computers",
             "imageLink": "http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
             "webReaderLink": "http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api",

    }
    print book1

if __name__ == '__main__':
    print "Searchtool population"
    populate()