import pytest
from main import glossary_letters

@pytest.mark.parametrize("test_input,expected", [
    ('Привет как дела?', 5),
    ('Вгнксмртл дщжбч', 0),
    ('ВаГоН БеЖиТ КаЧАЕтсЯ', 8),
    ('аоуэыяёюеи', 10),
])

def test_glossary_letters(test_input, expected):
    assert glossary_letters(test_input) == expected

