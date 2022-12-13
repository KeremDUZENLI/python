from hello2 import hello


def test_default():
    assert hello() == "Hello, world"

def test_arguments():
    assert hello("Kerem") == "Hello, Kerem"
 
