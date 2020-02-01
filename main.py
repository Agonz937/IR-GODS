<<<<<<< HEAD
import json
import csv
from Models.grab_data.read_json import ReadFiles
from Models.bm25.BM25 import BM25
from Models.vector_space.vector_space_model import VectorSpace

if __name__ == "__main__":
=======
""" This main file will process the models """
import json
from Models.grab_data.read_json import ReadFiles
from Models.vector_space_model.vector_space import VectorSpaceModel
from Models.bm25.BM25 import BM25
from Models.boolean_retrieval_model.preprocess import Preprocess

if __name__ == "__main__":

>>>>>>> 631dd5d49728ea7d9c9fb3d8ac3fd076908bf9ca
    data = ReadFiles()

    corpus = data.get_corpus()

<<<<<<< HEAD
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
    
=======
    test = Preprocess(corpus)

    # # Vector Space Model
    # vector_space_model = VectorSpaceModel(corpus)
    # vector_space_model.search(10,"Luz de ti")
>>>>>>> 631dd5d49728ea7d9c9fb3d8ac3fd076908bf9ca
    # # BM25 model 
    # process_bm25 = BM25(corpus)
    # process_bm25.search()

    
    
