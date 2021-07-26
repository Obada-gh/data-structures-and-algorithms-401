from hashmap_repeated_word import __version__
from hashmap_repeated_word import word
from hashmap_repeated_word.word import repeated_word


def test_version():
    assert __version__ == '0.1.0'


def test_samples():
    sample1="Once upon a time, there was a brave princess who..."
    sample2="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    sample3="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    actual1=repeated_word(sample1)
    actual2=repeated_word(sample2)
    actual3=repeated_word(sample3)

    expected1 = 'a'
    expected2 = 'it'
    expected3 = 'summer'

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3


def test_noRepetded():
    word='Man Of Hard Time'
    actual=repeated_word(word)
    expected='None'
    assert actual == expected
    


