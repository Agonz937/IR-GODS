from nltk.tokenize import word_tokenize

def query_terms():
    query = "Something im querying and batman"
    query = word_tokenize(query)
    connecting_words = []
    cnt = 1
    different_words = []
    for word in query:
        if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
            different_words.append(word.lower())
        else:
            connecting_words.append(word.lower())
    print(different_words)
    print(connecting_words)



def main():
    files_with_index = ["Adrian is cool","Adrian is not wack","I mean he be cute"]
    query = "Something im querying and batman"
    query = word_tokenize(query)
    connecting_words = []
    cnt = 1
    different_words = []
    for word in query:
        if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
            different_words.append(word.lower())
        else:
            connecting_words.append(word.lower())
    print("Query Words: ")
    print(different_words)
    print(connecting_words)
    print("-----------------------")
    total_files = len(files_with_index)
    zeroes_and_ones = []
    zeroes_and_ones_of_all_words = []
    for word in (different_words):
        if word.lower() in unique_words_all:
            zeroes_and_ones = [0] * total_files
            linkedlist = linked_list_data[word].head
            print(word)
            while linkedlist.nextval is not None:
                zeroes_and_ones[linkedlist.nextval.doc - 1] = 1
                linkedlist = linkedlist.nextval
            zeroes_and_ones_of_all_words.append(zeroes_and_ones)
        else:
            print(word," not found")
    print(zeroes_and_ones_of_all_words)
# for word in connecting_words:
#     word_list1 = zeroes_and_ones_of_all_words[0]
#     word_list2 = zeroes_and_ones_of_all_words[1]
#     if word == "and":
#         bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,word_list2)]
#         zeroes_and_ones_of_all_words.remove(word_list1)
#         zeroes_and_ones_of_all_words.remove(word_list2)
#         zeroes_and_ones_of_all_words.insert(0, bitwise_op);
#     elif word == "or":
#         bitwise_op = [w1 | w2 for (w1,w2) in zip(word_list1,word_list2)]
#         zeroes_and_ones_of_all_words.remove(word_list1)
#         zeroes_and_ones_of_all_words.remove(word_list2)
#         zeroes_and_ones_of_all_words.insert(0, bitwise_op);
#     elif word == "not":
#         bitwise_op = [not w1 for w1 in word_list2]
#         bitwise_op = [int(b == True) for b in bitwise_op]
#         zeroes_and_ones_of_all_words.remove(word_list2)
#         zeroes_and_ones_of_all_words.remove(word_list1)
#         bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,bitwise_op)]
# zeroes_and_ones_of_all_words.insert(0, bitwise_op);
        
# files = []    
# print(zeroes_and_ones_of_all_words)
# lis = zeroes_and_ones_of_all_words[0]
# cnt = 1
# for index in lis:
#     if index == 1:
#         files.append(files_with_index[cnt])
#     cnt = cnt+1
    
# print(files)

if __name__ == "__main__":
    """For testing this Model """
    main()