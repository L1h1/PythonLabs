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
    pass


def top_k_n_grams(text:str,k=10, n=4):
    pass