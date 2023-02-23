import re


def sentences_amount(text:str):
    return len([element for element in re.split(r"[.!?]+",text) if len(element.split())])


def non_declarative_sentences_amount(text:str):
    text=text.replace('.','')
    potential_ans=len([element for element in re.split(r"[!?]+",text) if len(element.split())])

    if potential_ans==1:
        if not '!' in text and not '?' in text:
            return 0
        else:
            return potential_ans
            
    return potential_ans if text[len(text)-1]=='?' or text[len(text)-1]=='!' else potential_ans-1



def average_sentence_len(text:str):
    sentences_lengths = [len(element) for element in re.split(r"[.!?]+",text) if len(element.split())]
    return 0 if not len(sentences_lengths) else sum(sentences_lengths)/len(sentences_lengths)


def average_word_len(text:str):
    word_lengths=[len(element) for element in re.split(r"[.!? \|/;:-=+*#$%']",text) if re.match(r"\w*[a-zA-z]\w*",element) and len(element.split())]
    return 0 if not len(word_lengths) else sum(word_lengths)/len(word_lengths)


def top_k_n_grams(text:str,k=10, n=4):
    (k,n)= (k,n) if k>0 and n>0 else (10,4)
    ngram_dict = {} # key: ngram, value: count
    words = tuple(re.split(r"[.!? \|/;:-=+*#$%']",text))
    if(len(words)<n):
        print("Incorrect input")
        return
    for i in range(len(words) - n + 1):
        ngram = words[i:i+n]
        ngram_dict[ngram] = ngram_dict[ngram] + 1 if ngram in ngram_dict.keys() else 1

    result = sorted(ngram_dict.items(), key=lambda pair: pair[1], reverse=True)
    return result[:k]    



