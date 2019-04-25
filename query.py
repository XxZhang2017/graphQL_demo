import graphene
import action
import schema
import json

class Query(graphene.ObjectType):
    analyzeUrl = graphene.Field(schema.UrlDescript, url = graphene.String(required = True))
    def resolve_analyzeUrl(self, info, url = 'https://www.google.com/'):
        r = action.get_request(url)
        return r
schema = graphene.Schema(query=Query)
def query_url(url, q):
    schema = graphene.Schema(query=q)
    query_string = '{ analyzeUrl(url: " ' + url + '"){ \
		success \
		returnCode \
		size \
		numberOfImages \
		images{ \
			url  \
            size \
            valid } \
         }\
        }'
    try:
        result = schema.execute(query_string)
    except:
        return 'url is invalid, please provide valid url'
    pretty_result = json.dumps(result.data['analyzeUrl'],indent=4)
    return pretty_result
# result = schema.execute(
# '{ analyzeUrl(url: "https://www.google.com/"){ \
# 		success \
# 		returnCode \
# 		size \
# 		numberOfImages \
# 		images{ \
# 			url  \
#             size \
#             valid } \
#          }\
#     }')
# print(result.data['analyzeUrl'])















