import json
import os
import time
from offline_search.search.documents import Abstract


def load_documents():
    start = time.time()
    print("files:", os.getcwd())
    # root = '/data'
    # root = r'C:\Users\shahmihi\Documents\new_offline_search\data'
    # for root, dirnames, filenames in os.walk(root):
    #     for filename in filenames:
    #         if filename.endswith('.json'):
                # path = os.path.join(root, filename)
    with open('/offline_search/offline_search/bod_dump.json', 'r', encoding="utf-8") as file:
        doc_id = 0
        bod_Data = json.load(file)
        for idx, js in enumerate(bod_Data):
            yield Abstract(ID=doc_id, title=js['title'], topic_ID=js['id'], content=js['content'])
            doc_id += 1
    end = time.time()
    print(f'Parsing JSon took {end - start} seconds')
