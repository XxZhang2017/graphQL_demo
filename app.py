import graphene
import os
import json
from flask import Flask, url_for, redirect, request
from flask_graphql import GraphQLView
from query import Query, query_url
from OpenSSL import SSL
from graphql import GraphQLError

app = Flask(__name__)
view_func = GraphQLView.as_view(
'graphql', schema = graphene.Schema(query=Query), graphiql = True)
app.add_url_rule('/graphql', view_func = view_func)



@app.route("/", methods = ['GET'])
def hello():
    return redirect(url_for('static', filename='index.html'))

@app.route("/graphQL", methods=['GET'])
def queryURL():   
    url = request.args.get('url')
    if url != None and url != '' and url != ' ':
        try:
            reg = query_url(url, Query)
            if reg == 'null':
                print('reg is ' + reg)
                return 'url is invalid, please provide valid url'   
            return reg
        except GraphQLError as e:
            return e.message
    else:
        print("url is none")
        return 'Please provide url string'
    

if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 5000),
    ssl_context=context, debug = True)
    # app.run(host='127.0.0.1', port=os.environ.get('PORT', 5000), debug = True)