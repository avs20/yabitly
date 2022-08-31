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




from uuid import UUID
def test_for_generateUrl(mocker):
    """
    This should convert a number to hexa decimal string.
    """
    mocker.patch('src.yabitly.generateUrl.uuid4', return_value = UUID('b88e5416-4296-4179-969a-d18248c1f4b6'))
    expected =  "B88E541642964179"
    result = generateUrl("test.com")
    assert result == expected