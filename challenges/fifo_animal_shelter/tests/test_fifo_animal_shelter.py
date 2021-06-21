from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Cat, Node,AnimalShelter,Cat,Dog,Queue


def test_version():
    assert __version__ == '0.1.0'

def test_all():
    dog1=Dog('red')
    dog2=Dog('blue')
    cat1=Cat('lol')
    cat2=Cat('king')
    shelter=AnimalShelter()
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    actual = shelter.dequeue('dog')
    expected1 = 'blue'
    expected2 = 'lol'
    actual1 = shelter.dequeue('dog')
    actual2 = shelter.dequeue('cat')
    
    assert actual1 == expected1
    assert actual2 == expected2

    
