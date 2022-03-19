"""This is a pytest for three dictionary funtions."""

__author__ = "730528983"


from dictionary import invert, favorite_color, count


# For funtion invert:
def test_invert_empty() -> None:
    """This is one edge case for a dicionary function called invert and it is entered by empty value."""
    all_one: dict[str, str] = {"": ""}
    assert invert(all_one) == {"": ""}


def test_invert_many_item1() -> None:
    """This is one use edge case for a dictionart function called invert using two groups."""
    all_one: dict[str, str] = {'kris': 'jordan', 'michael': 'lee'}
    assert invert(all_one) == {'jordan': 'kris', 'lee': 'michael'}


def test_invert_many_item2() -> None:
    """This is one use edge case for a dictionart function called invert using three groups."""
    all_one: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(all_one) == {'z': 'a', 'y': 'b', 'x': 'c'}


# For function favorite_color:
def test_favorite_color_empty() -> None:
    """This is one edge case for a dicionary function called favorite_color and it shows what will happen if there is an empty entry."""
    assert favorite_color({"": "", "": ""}) == ""


def test_favorite_color_many_items1() -> None:
    """This is one edge case for a dicionary function called favorite_color and the most frequency color is blue."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_many_items2() -> None:
    """This is one edge case for a dicionary function called favorite_color and the most frequency word is green."""
    assert favorite_color({"Marc": "yellow", "Ezri": "green", "Kris": "green"}) == "green"


# For function count:
def test_count_empty() -> None:
    """This is one edge case for a dicionary function called count and it shows what will happen if count is empty."""
    assert count([]) == {}


def test_count_many_items1() -> None:
    """This is one edge case for a dicionary function called count using two different colors as an example."""
    assert count(["yellow", "blue", "blue"]) == {"yellow": 1, "blue": 2}


def test_count_many_items2() -> None:
    """This is one edge case for a dicionary function called count."""
    assert count(["yellow", "green", "green", "green", "red", "pink"]) == {"yellow": 1, "green": 3, "red": 1, "pink": 1}
