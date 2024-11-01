import marqo

# Initialize Marqo client
mq = marqo.Client(url='http://localhost:8882')

def text_similarity_tool_function(query):
    results = mq.index('tweets-index').search(query)
    if results['hits']:
        return [hit['tweet'] for hit in results['hits']]
    else:
        return 'No similar documents found'