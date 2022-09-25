from solution_reverse_words import reverse_words

def test_reverse_words():
    assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    assert reverse_words('apple') == 'elppa'
    assert reverse_words('a b c d') == 'a b c d'
    assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'
