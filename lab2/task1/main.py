from utilities import sentences_amount, non_declarative_sentences_amount, average_sentence_len,average_word_len, top_k_n_grams

task_template="""
What to do?
[1]amount of sentences in the text;
[2]amount of non-declarative sentences in the text;
[3]average length of the sentence in characters (words count only);
[4]average length of the word in the text in characters;
[5]top-K repeated N-grams in the text (K and N are taken from input if needed; by default K=10, N=4).
"""

def main():
    user_input_text = input("Input your text:")
    operation_case=int(input(task_template))
    match operation_case:
        case 1:
           print(sentences_amount(user_input_text))
        case 2:
            print(non_declarative_sentences_amount(user_input_text))
        case 3:
            print(average_sentence_len(user_input_text))
        case 4:
            print(average_word_len(user_input_text))
        case 5:
            k = int(input("Enter k: 0 - set default"))
            n = int(input("Enter n: 0 - set default"))
            print(top_k_n_grams(user_input_text,k,n))

if __name__=="__main__":
    main()