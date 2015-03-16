# Web App
import urllib2
import json
import re

def converter(text):
    text = text.replace('&nbsp;', ',').replace('&quot;', '"').replace('&#39;', "'")
    pattern = re.compile('<[^>]+>')
    return pattern.sub(' ', text)

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
        else:
            book['description'] = "Sorry. This might be a secret. :("

        book['authors'] = ''
        if 'authors' in volumeInfo:
            for info in volumeInfo['authors']:
                book['authors'] += ', '+info.encode('utf-8')
            book['authors'] = book['authors'][2:]

        if 'publishedDate' in volumeInfo:
            book['publishedDate'] = volumeInfo['publishedDate']
        else:
            book['publishedDate'] = 'Unknown'
        book['image'] = volumeInfo['imageLinks']['thumbnail']

        book['categories'] = []
        if 'categories' in volumeInfo:
            for info in volumeInfo['categories']:
                book['categories'].append(info.encode('utf-8'))
        # book['categories'] = volumeInfo['categories']     # List

        if 'searchInfo' in item:
            searchInfo = item['searchInfo']
            book['textSnippet'] = converter(searchInfo['textSnippet'].encode('utf-8'))
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
    query = query.encode('utf-8').replace(' ','%20')
    url = "https://www.googleapis.com/books/v1/volumes?q="+query
    print url
    # url ="https://www.googleapis.com/books/v1/volumes?q=Tensile%20Testing,%202nd%20Edition"
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
