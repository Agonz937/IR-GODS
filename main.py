import json
import csv
from Models.grab_data.read_json import ReadFiles
from Models.bm25.BM25 import BM25
from Models.vector_space.vector_space_model import VectorSpace

if __name__ == "__main__":
    data = ReadFiles()

    corpus = data.get_corpus()

    # Vector Space
    vector_space = VectorSpace(corpus=corpus)
    result_vector_space = vector_space.search(["Bound Checking Validator"])
    for result in result_vector_space:
        for answers in result:
            print("DocID: {} and Ranking: {}".format(answers[0],answers[1]))
    # with open("vector_space_result.csv", mode='w') as csv_file:
    #     field_name = ['doc_id','ranking']
    #     writer = csv.DictWriter(csv_file,fieldnames=field_name)
        
    #     writer.writeheader()
    #     for result in result_vector_space:
    #         for answers in result:
    #             writer.writerow({'doc_id': answers[0],'ranking':answers[1]})

    # with open('output.tsv', 'wt') as out_file:
    #     print("Writing to file")
    #     tsv_writer = csv.writer(out_file, delimiter='\t')
    #     tsv_writer.writerow(['doc_id', 'ranked'])
    #     for result in result_vector_space:
    #         for answers in result:
    #             tsv_writer.writerow([answers[0],answers[1]])
    
    # # BM25 model 
    # process_bm25 = BM25(corpus)
    # process_bm25.search()

    
    
