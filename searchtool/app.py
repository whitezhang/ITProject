# Web App
import urllib2
import json
import re
import random
from dao import daoGetCategoriesByUser

# Alchemy API
def taxonomyDecoder(username):
    taxList = []
    categories = daoGetCategoriesByUser(username)
    # bookInfo = ["Computer", "Java", "C%20program"]
    AlchemyKey = "3f07faf2bf9dc29f4a0d40072dfc09e6e3e2fbd9"
    for info in categories:
        url = "http://access.alchemyapi.com/calls/text/TextGetRankedTaxonomy?apikey="+AlchemyKey+"&outputMode=json&text="+info
        print url
        req = urllib2.Request(url=url)
        f = urllib2.urlopen(req)
        content = f.read()
        jsonData = json.loads(content)
        # Processing main body of data
        if jsonData['status'] == 'OK':
            if 'taxonomy' in jsonData:
                taxonomy = jsonData['taxonomy']
                # Just need the first one
                # /technology and computing/hardware/computer etc.
                taxList.append(taxonomy[0]['label'])
    return taxList

def getChildren(node, links):
    return [x[1] for x in links if x[0] == node]

def getNodes(index, name, links):
    jsonNode = {}
    jsonNode['id'] = index
    jsonNode['name'] = name
    children = getChildren(name, links)
    if children:
        jsonNode['children'] = [getNodes(index+random.randint(1, 10000), child, links) for child in children]
    return jsonNode

def taxonomyGenerator(username):
    links = []
    taxList = taxonomyDecoder(username)
    for taxonomy in taxList:
        # taxonomy = '/technology and computing/hardware/computer'
        tax = taxonomy.encode('utf-8').split('/')
        # pre-process the taxonomy, replace space with <br> and set in center
        for index in range(len(tax)-1):
            ta = tax[index].split(' ')
            # Get the maximum length of string
            maxLen = 0
            tmpTaxonomy = ''
            for word in ta:
                maxLen = max(len(word), maxLen)
            # print maxLen
            for word in ta:
                tmpTaxonomy += '&nbsp;'*((maxLen-len(word))/2+2)+word+'<br>'
            # print tmpTaxonomy
            tax[index] = tmpTaxonomy
        # print tax
        for index in range(len(tax)-2):
            links.append((tax[index+1], tax[index+2]))
    # Remove the duplicated item
    uniqueLinks = []
    [uniqueLinks.append(item) for item in links if item not in uniqueLinks]
    parents, children = zip(*uniqueLinks)
    rootNodes = {x for x in parents if x not in children}
    for node in rootNodes:
        uniqueLinks.append(('Me', node))
    ontologyJSON = getNodes(0, 'Me', uniqueLinks)
    return ontologyJSON

# Google Book API
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
    if not 'items' in jsonData:
        return
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

        if 'imageLinks' in volumeInfo and 'thumbnail' in volumeInfo['imageLinks']:
            book['image'] = volumeInfo['imageLinks']['thumbnail']
        else:
            book['image'] = 'http://www.rossettiarchive.org/img/9p-1850.virginia.endp4.jpg'

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

        if 'accessInfo' in item:
            accessInfo = item['accessInfo']
        else:
            accessInfo = 'Unknown'
        if 'webReaderLink' in accessInfo:
            book['webReaderLink'] = accessInfo['webReaderLink'].encode('utf-8')
        else:
            book['webReaderLink'] = 'Unknown'
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
    if not 'items' in jsonData:
        return
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

        if 'imageLinks' in volumeInfo and 'thumbnail' in volumeInfo['imageLinks']:
            book['image'] = volumeInfo['imageLinks']['thumbnail']
        else:
            book['image'] = 'http://www.rossettiarchive.org/img/9p-1850.virginia.endp4.jpg'

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

        if 'accessInfo' in item:
            accessInfo = item['accessInfo']
        else:
            accessInfo = 'Unknown'
        if 'webReaderLink' in accessInfo:
            book['webReaderLink'] = accessInfo['webReaderLink'].encode('utf-8')
        else:
            book['webReaderLink'] = 'Unknown'
        related_books.append(book)

    return related_books
