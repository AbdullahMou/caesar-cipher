import nltk
nltk.download('words')
words_list= nltk.corpus.words.words()
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(msg, key):
    sentence =''
    msg = msg.lower()
    for char in msg:
        if char  not in letters :
            sentence+= char
        else:
            index = letters .index(char)
            sentence+= letters [(index + (key%26)) % len(letters )]
    return sentence  


def decrypt(msg,key):
    sentence =''
    msg = msg.lower()
    for char in msg:
        if char  not in letters :
            sentence+= char
        else:
            index = letters .index(char)
            sentence+= letters [(index - (key%26)) % len(letters )]
    return sentence  


def english_words(msg):
    words = msg.split()
    count = 0

    for word in words:
        if word in words_list:
            count += 1    
    if (count/len(words)) > 0.5:
        return count
    else: 
        return 0


def crack(msg):
    longest_sentence = ''
    max = 0
    for key in range(26):
        decrypted = decrypt(msg ,key)
        count_words = english_words(decrypted)
        if count_words > max:
            longest_sentence = decrypted
    return longest_sentence    
