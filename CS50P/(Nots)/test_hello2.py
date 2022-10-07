from hello2 import hello


def test_default():
    assert hello() == "Hello, world"


def test_arguments():
    for i in ["Hermione", "Harry", "Ron"]:
        assert hello(i) == f"Hello, {i}"




