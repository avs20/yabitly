import pytest
import sys 
sys.path.append('.')



from src.yabitly.generateUrl import *


def test_for_base_encode_hex():
    """
    This tests if the base encoding in hexadecimal is working fine or not. 
    """
    # good cases
    input = 10
    expected = 'A'
    actual = base_encode(input)
    assert actual == expected

    input = 2403
    expected = '963'
    actual = base_encode(input)
    assert actual == expected

    input = 3108
    expected = 'C24'
    actual = base_encode(input)
    assert actual == expected

    input = None
    expected = None
    actual = base_encode(input)
    assert actual == expected

    # bad cases
    input = "ashu"
    # this should raise an exception 
    with pytest.raises(ValueError):
        actual = base_encode(input)
    
    input = 1.2
    # this should raise an exception 
    with pytest.raises(ValueError):
        actual = base_encode(input)





def test_for_generateUrl():
    """
    This should convert a number to hexa decimal string.
    """
    pass