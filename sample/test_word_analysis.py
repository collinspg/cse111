import pytest
from word_analysis import calculate_word_frequency, calculate_word_count

def test_calculate_word_count():
    text = "Once upon a time, in a faraway land, there lived a young princess named Aurora."
    word_count = calculate_word_count(text)
    assert word_count == 15

def test_calculate_word_frequency():
    text = "Once upon a time, in a faraway land, there lived a young princess named Aurora."
    word_frequency = calculate_word_frequency(text)
    expected_frequency = {
        'Once': 1, 'upon': 1, 'a': 3, 'time': 1, 'in': 1, 'faraway': 1, 'land': 1,
        'there': 1, 'lived': 1, 'young': 1, 'princess': 1, 'named': 1, 'Aurora': 1
    }
    assert word_frequency == expected_frequency

pytest.main(["-v", "--tb=line", "-rN", __file__])  