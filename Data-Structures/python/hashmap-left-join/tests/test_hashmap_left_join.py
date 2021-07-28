from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join

def test_version():
    assert __version__ == '0.1.0'

def test_leftJoin():
    hash1={'fond': 'enamored','wrath': 'anger','diligent': 'employed','outfit':'grab','guide':'usher' }
    hash2={'fond': 'averse','wrath': 'diligent','diligent': 'idle','guide':'follow','flow':'jam' }
    actual= left_join(hash1,hash2)
    expected= [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'diligent'], ['diligent', 'employed', 'idle'], ['outfit', 'grab', None], ['guide', 'usher', 'follow']]
    assert actual == expected

