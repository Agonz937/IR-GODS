import vector_space
import operator

# vector_space = vector_space.VectorSpace(["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."])


# #Search for cat
# print (vector_space.search(["cat","disabled"]))

# #Show score for relatedness against document 0
# #print (vector_space.related(0)) 

# Read files
#Grabs all of the file from Data directory and stores them into a list

import os
import codecs

def getAllFile():
    docs = {}
    sortFiles = {}
    text = ""

    #iterates through the data directory and store them in list
    for filename in os.listdir("/Volumes/Samsung_T5/Information Retrival/Project2/data"):
        if filename.startswith("data"):
            id = str(filename)
            id = str(int(id[4:-4]))
            sortFiles.update({id : os.path.join("data/",filename)})
    
    fileName = 'data/data1.txt'
    with open(fileName, "r", encoding="ISO-8859-1") as f:
        text = f.read()
        text  = text.replace("\n", "")
    
    
    
    w = open("Models/vector_space_model/result.txt", "w")
    w.write(text)
    w.close()
    w.close()

    # for i in sorted(sortFiles):
    #     print ((i, sortFiles[i]), end ="\n") 
            #sortFiles.append(os.path.join("data/",filename))

    # Reads each file and stores the result as a list
    # for key, file in sortFiles.items():
    #     try:
    #         with open(file,'r', encoding="ISO-8859-1") as f:
    #             text = f.readline()
    #             #text = text.replace("\n \r", "")
    #             # while text:
    #             #     print(text)
    #             #docs.update({key: text})
    #         f.close()
    #     except IOError:
    #         error = "Couldn't read file: {}".format(file)
    #         print(error)
    return docs

#doc = getAllFile()


# for key, value in doc.items():
#     files = "file: {} ----> text: {}\n".format(key,value)
#     print(files)

documents = []

doc1 = """ 
The cat \n cat 
in the hat \n
disabled
"""


doc2 = """ 
"A cat \n
is a \n
fine pet \n
ponies."
"""
doc3 = """ 
Dogs \n
and \n
cats make \ngood pets.
"""

doc4 = """ 
I haven't\n got a hat.\n
"""

documents.append(doc1)
documents.append(doc2)
documents.append(doc3)
documents.append(doc4)

vector_space = vector_space.VectorSpace(["The cat cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."])

#vector_space = vector_space.VectorSpace(documents)



#Search for cat
rating = vector_space.search(["cat","hat","disabled","cat"])

# items = sorted(rating.items(), key=operator.itemgetter(1))
# items.sort(reve)
# print(items)
#rint (vector_space.search(["cat","hat","disabled"]))

#Show score for relatedness against document 0
#print (vector_space.related(0)) 