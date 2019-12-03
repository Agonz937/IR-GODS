""" This main file will process the models """
import json
from Models.grab_data.read_json import ReadFiles
from Models.vector_space_model.vector_space import VectorSpaceModel
from Models.bm25.BM25 import BM25
from Models.boolean_retrieval_model.preprocess import Preprocess

if __name__ == "__main__":

    data = ReadFiles()

    corpus = data.get_corpus()

    test = Preprocess(corpus)

    # # Vector Space Model
    # vector_space_model = VectorSpaceModel(corpus)
    # vector_space_model.search(10,"Luz de ti")
    # # BM25 model 
    # process_bm25 = BM25(corpus)
    # process_bm25.search()

    
    
