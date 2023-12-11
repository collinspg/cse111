import pytest
from word_analysis import calculate_word_frequency, calculate_word_count

def test_calculate_word_count():
    text1 = "Once upon a time, in a faraway land, there lived a young princess named Aurora."
    text2 = "She had flowing golden hair, sparkling blue eyes, and a kind heart."
    
    word_count1 = calculate_word_count(text1)
    assert word_count1 == 15
    
    word_count2 = calculate_word_count(text2)
    assert word_count2 == 12

def test_calculate_word_frequency():
    text1 = "Once upon a time, in a faraway land, there lived a young princess named Aurora."
    text2 = "She had flowing golden hair, sparkling blue eyes, and a kind heart."
    
    word_frequency1 = calculate_word_frequency(text1)
    expected_frequency1 = {
        'Once': 1, 'upon': 1, 'a': 3, 'time': 1, 'in': 1, 'faraway': 1, 'land': 1,
        'there': 1, 'lived': 1, 'young': 1, 'princess': 1, 'named': 1, 'Aurora': 1
    }
    
    assert word_frequency1 == expected_frequency1
    
    word_frequency2 = calculate_word_frequency(text2)
    expected_frequency2 = {
        'She': 1, 'had': 1, 'flowing': 1, 'golden': 1, 'hair': 1, 'sparkling': 1,
        'blue': 1, 'eyes': 1, 'and': 1, 'a': 1, 'kind': 1, 'heart': 1
    }
    
    assert word_frequency2 == expected_frequency2
pytest.main(["-v", "--tb=line", "-rN", __file__])