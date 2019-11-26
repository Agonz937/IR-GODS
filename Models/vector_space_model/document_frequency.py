
import enum

class Processing(enum.Enum):
    done = 0
    working = 1

class DocumentFrequency:
    """ This class will focus on creating a Inverting index and returning the term frequency """
    def __init__(self, corpus):
        if type(corpus) != list and corpus != []:
            print("A list must be send")

        self.state = Processing.working
        self.DF = {}

        if len(corpus) > 0:
            self._invert_index(corpus)
    

    def get_document_frequency(self):
        return self.DF if self.state == Processing.done else None

    def _invert_index(self, corpus):
        """ We are going to create an inverted index then get the frequency for these terms"""


        # We need to get the size of posting
        for i in range(len(corpus)):
            tokens = corpus[i]
            for word in tokens:
                if word not in self.DF:
                    self.DF[word] = []
                if word in self.DF[word]:
                    continue
                self.DF[word].append(i+1)
        for i in self.DF:
            self.DF[i] = len(self.DF[i])
        
        self.state = Processing.done

