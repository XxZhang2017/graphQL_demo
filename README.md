Implement a python service that exposes a simple GraphQL API: analyzeUrl(Url: String)


Example:

query {
	analyzeUrl(url:”https://www.google.com/”){
		success
		returnCode
		size
		numberOfImages
		images{
			url                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			size	
		}
	}
}

- success “OK”, “Not OK”
- return code (e.g 200 if it was successful, 404 if the URL was invalid / page not found…)
- size of the page hosted at that url
- number of images
- and for each image referenced at that URL the URL of the image and their size and wether the URL was valid

- server: flask
- support http and https. certificate It is self-signed certificate. To run https or http, you can read the code in app.py.
- interface: /graphql
