from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test case:
    given_name = "Sally"
    family_name = "Brown"
    expected_result = "Brown; Sally"
    assert make_full_name(given_name, family_name) == expected_result

    
def test_extract_family_name():
    # Test case:
    full_name = "Brown; Sally"
    expected_result = "Brown"
    assert extract_family_name(full_name) == expected_result
    
    
def test_extract_given_name():
    # Test case:
    full_name = "Brown; Sally"
    expected_result = "Sally"
    assert extract_given_name(full_name) == expected_result
    
    
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])