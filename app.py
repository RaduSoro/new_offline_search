from flask import Flask
from flask import request
from flask import render_template
from offline_search.load import load_documents
from offline_search.search.timing import timing
from offline_search.search.index import Index, analyzed_query
import os

app = Flask(__name__)

@timing
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)
        if i % 259 == 0:
            print(f'Indexed {i} documents', end='\r')
    return index

@app.route('/')
def hell_world():
    return render_template('index.html')


@app.route('/query/', methods=['GET'])
def query():
    query = request.args.get("query")
    index = index_documents(load_documents(), Index())
    retrieved_documents = index.search(query, search_type='AND & OR', rank=True)
    # offline_search_result = retrieved_documents[:5]
    
    offline_search_result = []
    for i, document in enumerate(retrieved_documents[:5]):
        # final_results = {'title': document[0], 'content': document[2], 'topic_score': document[3]}
        final_results = {'title': document[0], 'topic_score': document[1]}
        offline_search_result.append(final_results)
    return render_template('index.html', offline_search_result=offline_search_result, query=query)
    # return render_template('index.html', retrieved_documents=retrieved_documents, query=query)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)