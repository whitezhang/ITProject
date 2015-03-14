# Web App
import urllib2
import json

def bookJSONParser(query):
    book_list = []
    url = "https://www.googleapis.com/books/v1/volumes?q="+query
    req = urllib2.Request(url=url)
    f = urllib2.urlopen(req)
    content = f.read()
    jsonData = json.loads(content)
    # Processing main body of data
    totalItems = int(jsonData['totalItems'])
    items = jsonData['items']
    for item in items:
        book = {}
        book['id'] = item['id']
        book['setLink'] = 'google.com'

        volumeInfo = item['volumeInfo']
        book['title'] = volumeInfo['title'].encode('utf-8')

        if 'description' in volumeInfo:
            book['description'] = volumeInfo['description'].encode('utf-8')

        book['authors'] = ''
        for info in volumeInfo['authors']:
            book['authors'] += ', '+info.encode('utf-8')
        book['authors'] = book['authors'][2:]

        book['publishedDate'] = volumeInfo['publishedDate']
        book['image'] = volumeInfo['imageLinks']['thumbnail']

        book['categories'] = []
        for info in volumeInfo['categories']:
            book['categories'].append(info.encode('utf-8'))
        # book['categories'] = volumeInfo['categories']     # List

        if 'searchInfo' in item:
            searchInfo = item['searchInfo']
            book['textSnippet'] = searchInfo['textSnippet']
        else:
            book['textSnippet'] = "Sorry. This might be a secret. :("

        accessInfo = item['accessInfo']
        book['webReaderLink'] = accessInfo['webReaderLink'].encode('utf-8')
        book_list.append(book)
    num = 9
    if len(book_list) < 9:
        num = len(book_list)
    return book_list[:num]


def relatedBookCrawler(query):
    related_books = []
    url = "https://www.googleapis.com/books/v1/volumes?q="+query
    req = urllib2.Request(url=url)
    f = urllib2.urlopen(req)
    content = f.read()
    jsonData = json.loads(content)
    # print content
    jsonData = json.loads(content)
    # Process the json file
    totalItems = int(jsonData['totalItems'])
    items = jsonData['items']
    for item in items:
        book = {}
        volumeInfo = item['volumeInfo']
        book['title'] = volumeInfo['title'].encode('utf-8')
        book['image'] = volumeInfo['imageLinks']['thumbnail']
        if 'description' in volumeInfo:
            book['description'] = volumeInfo['description'].encode('utf-8')
        related_books.append(book)

    return related_books
