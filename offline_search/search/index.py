import math

from .timing import timing
from .analyzer import analyze
from .spell_correction import correction

"indexing pre-processed data, TF-IDF vectorizing, and retreiving document"

class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    #indexing document
    def index_document(self, document):
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            document.analyze()

        for token in analyze(document.full_text):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.ID)

    #TF-IDF
    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        return math.log10(len(self.documents) / self.document_frequency(token))

    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]



    @timing
    def search(self, query, search_type='AND', rank=False):
        """
        Search; based on query words provided, retrieved documents will be returned
        based on ranking

        Parameters:
          - query: the query string
          - search_type: ('AND', 'OR') do all query terms have to match, or just one
          - score: (True, False) if True, rank results based on TF-IDF score
        """
        # if search_type not in ('AND', 'OR'):
        #     return []

        query_chunks = analyze(query)
        correct_command=[]
        for chunks in query_chunks:
            if chunks == correction(chunks):
                correct_command.append(chunks)
            else:
                chunks = correction(chunks)
                correct_command.append(chunks)
        corrected_command = ' '.join(correct_command)

        analyzed_query = analyze(corrected_command)
        print('-----------------------------')
        print("Searching for:", analyzed_query)
        print('-----------------------------')
        results = self._results(analyzed_query)


        # if search_type == 'AND':
        #     # all tokens must be in the document
        #     documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
        # if search_type == 'OR':
        #     # only one token has to be in the document
        #     documents = [self.documents[doc_id] for doc_id in set.union(*results)]

        documents = [self.documents[doc_id] for doc_id in set.union(*results) and set.intersection(*results)]
        if rank:
            return self.rank(analyzed_query, documents)
        return documents


    def rank(self, analyzed_query, documents):
        results = []
        if not documents:
            return results
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document.title, score))
        final_result = sorted(results, key=lambda doc: doc[1], reverse=True)
        return final_result
