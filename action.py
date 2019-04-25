import requests, cStringIO
import schema
import io
from BeautifulSoup import BeautifulSoup
from PIL import Image
from graphql import GraphQLError

def get_request(url):
    try:
        html_page = requests.get(url)
        success = 0
        returnCode = get_returnCode(html_page)
        html_page.raise_for_status()
        p_size = get_page_size(html_page.text)
        soup = BeautifulSoup(html_page.text)
        returnCode = get_returnCode(html_page)
        if returnCode < 400:
            success = 1
        images = get_img(url, soup, html_page.content)
        numberOfImages = get_numberOfImages(images)
        return schema.UrlDescript(success = success, returnCode = returnCode, 
        size = p_size, images = images, numberOfImages = numberOfImages)
    except requests.exceptions.HTTPError as err:
        raise GraphQLError('url is invalid, please provide valid url')


def get_img(url, soup, r_content):   
    url_neddle = '://'
    images = []
    for img in soup.findAll('img'):
        url_src = img.get('src').encode('utf-8') 
        pos = url_src.find(url_neddle)
        if pos not in range(3, 7):
            url_src = url + url_src  
        s =  get_size(url_src)
        if s == None:
            img_size = '(0, 0)'
            img_valid = 0
        else:
            img_size = s
            img_valid = 1
        img_obj = schema.Img(url = url_src, size = img_size, valid = img_valid)
        images.append(img_obj)
    return images;


def get_returnCode(resp_header):
    return resp_header.status_code
def get_numberOfImages(img_list):
    return len(img_list)

def get_size(url):
    try:
        r = requests.get(url)
    except requests.exceptions.HTTPError as err:
        # print("HTTPError({0}): {1}".format(err.errno, err.strerror))
        return None
    try:
        file = cStringIO.StringIO(r.content)
        im=Image.open(file)
    except IOError as e:
        # print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
    return im.size

def get_page_size(text):
    return len(text)

