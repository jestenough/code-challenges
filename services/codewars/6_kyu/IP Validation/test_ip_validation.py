from solution_ip_validation import is_valid_IP


def test_is_valid_IP():
    assert is_valid_IP('12.255.56.1') == True
    assert is_valid_IP('') == False
    assert is_valid_IP('abc.def.ghi.jkl') == False
    assert is_valid_IP('123.456.789.0') == False
    assert is_valid_IP('12.34.56') == False
    assert is_valid_IP('12.34.56 .1') == False
    assert is_valid_IP('12.34.56.-1') == False
    assert is_valid_IP('123.045.067.089') == False
    assert is_valid_IP('127.1.1.0') == True
    assert is_valid_IP('0.0.0.0') == True
    assert is_valid_IP('0.34.82.53') == True
    assert is_valid_IP('192.168.1.300') == False
