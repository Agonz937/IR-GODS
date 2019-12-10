import json
import types

try:
    import Models.bm25.parse
except Exception as err:
    print(err)

class ReadFiles():
    """ 
    Read Files class is responsible for fetching the json files
    and returning back a list of descriptions based on:
    Author, Date, Type, Platform, verified, CVE.
    """

    def __init__(self, author="", date="", types="", platform="", verified=None, cve=""):
        self.data = ""
        self.list_description = []
        self._author = author.lower()
        self._date = date
        self._type = types.lower()
        self._platform = platform.lower()
        self._flag = verified
        self._cve = cve

        # fetch the data
        with open("data/new_output.json") as json_file:
            self.data = json.load(json_file)

        #Fetch by parameters
        if self._author != "":
            self._get_by_author()

        # TODO testing
        self._get_all()

    def get_corpus(self):
        return self.list_description

    def printData(self,position):
        position = position + 1
        position = str(position)
        return self.data[position]["description"]
            

    def _get_by_author(self):
        for index in self.data:
            author = self.data[index]["author"]
            if author.lower() == self._author:
                self.list_description.append(self.data[index]["description"])

    def _get_by_date(self):
        for index in self.data:
            date = self.data[index]["date"]
            date = date.split("-")
            if date[0] == self.date[0]:
                self.list_description.append(self.data(index)["description"])

    def _get_by_type(self):
        for index in self.data:
            types = self.data[index]["type"]
            if types.lower() == self._type:
                self.list_description.append(self.data(index)["description"])

    def _get_by_platform(self):
        for index in self.data:
            platform = self.data[index]['platform']
            if platform.lower() == self._platform:
                self.list_description.append(self.data(index)["description"])

    def _get_by_verified(self):
        for index in self.data:
            verified = self.data[index]["verified"]
            if verified.lower() == "verified":
                self.list_description.append(self.data(index)["description"])

    def _get_by_cve(self):
        for index in self.data:
            pass
    
    def _get_all(self):
        for index in self.data:
            self.list_description.append(self.data[index]["description"])





if __name__ == '__main__':

    corpus = ReadFiles()


    # vector_space = VectorSpaceModel(corpus.get_list())

    # vector_space.search(k=10,query="IObit")

    corpus = corpus.get_list()

    # 41859

    # index = [41857,35926, 35883,  8564, 37315, 35804, 35844, 35809, 35794, 35778]
    # index = [41857  ,8564 ,35926 ,35883 ,27070 ,27073 ,13975 ,13949 ,13955 ,13954]
    index = [35926,35883,41857,41858,13949,13956,13955,13954,13953,13952]

