import graphene
from BeautifulSoup import BeautifulSoup


class Img(graphene.ObjectType):
    url = graphene.String()
    size = graphene.String()
    valid = graphene.Int()

class UrlDescript(graphene.ObjectType):
    success = graphene.Boolean()
    returnCode = graphene.Int()
    size = graphene.Int()
    numberOfImages = graphene.Int()
    images = graphene.List(Img)