import pytest
from utilities import sentences_amount, average_sentence_len, non_declarative_sentences_amount, average_word_len, top_k_n_grams

@pytest.mark.parametrize("sample,ans",
                            [
                                ("hello! world?",2),
                                ("SOME.BODY?ONCE!TOLD...ME!THE?WORLD?IS GONNA ROLL ME.",8),
                                ("..................",0),
                                ("................    .",0),
                                ("dwadaweweaweweaw ew eavdsgsdf  adas.",1)
                            ]
                         )
def test_sentences_amount(sample,ans):
    assert sentences_amount(sample)==ans



@pytest.mark.parametrize("sample,ans",
                            [
                                ("hello! world?",5.5),
                                ("SOME.BODY?ONCE!TOLD...ME!THE?WORLD?IS GONNA ROLL ME.",5.25),
                                ("..................",0),
                                ("................    ",0),
                                ("dwadaweweaweweaw ew eavdsgsdf  adas.",35)
                            ]
                         )
def test_average_sentence(sample,ans):
    assert average_sentence_len(sample)==ans



@pytest.mark.parametrize("sample,ans",
                            [
                                ("hello! world?",2),
                                ("SOME.BODY?ONCE!TOLD...ME!THE?WORLD?IS GONNA ROLL ME.",5),
                                ("well.",0),
                                ("? hello",1),
                                ("!.!",0)
                            ]
                         )
def test_non_declarative(sample,ans):
    assert non_declarative_sentences_amount(sample) == ans




@pytest.mark.parametrize("sample,ans",
                            [
                                ("hello! world?",5),
                                ("SOME.BODY?ONCE!TOLD...ME!THE?WORLD?IS GONNA ROLL ME.",39.0/11),
                                ("..................",0),
                                ("12345 1k3 k13 ",3),
                                ("dwadaweweaweweaw ew eavdsgsdf  adas.",7.75)
                            ]
                         )
def test_average_word(sample,ans):
    assert average_word_len(sample)==ans




@pytest.mark.parametrize("sample,k,n,ans",
                            [
                                ("SCoI hell SCoI hell",2,2,[(('SCoI', 'hell'), 2), (('hell', 'SCoI'), 1)]),
                                ("wasd wasd wasd wasd wasd ijkl ijkl ijkl",3,2,[(('wasd', 'wasd'), 4), (('ijkl', 'ijkl'), 2), (('wasd', 'ijkl'), 1)]),
                                ("igfderisgbirfsgbilfds,bfbib",7,3,None),
                                ("Somebody once told me the world is gonna roll me",8,3,[(('Somebody', 'once', 'told'), 1), (('once', 'told', 'me'), 1), (('told', 'me', 'the'), 1), (('me', 'the', 'world'), 1), (('the', 'world', 'is'), 1), (('world', 'is', 'gonna'), 1), (('is', 'gonna', 'roll'), 1), (('gonna', 'roll', 'me'), 1)])
                            ]
                         )
def test_ngrams(sample,k,n,ans):
    assert top_k_n_grams(sample,k,n)==ans

