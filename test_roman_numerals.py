from roman_numerals import to_roman
import pytest

@pytest.mark.parametrize("test_input,expected", [("to_roman(1)", "I"), 
                                                 ("to_roman(5)", "V"), 
                                                 ("to_roman(10)", "X"),
                                                 ("to_roman(50)", "L"), 
                                                 ("to_roman(100)", "C"), 
                                                 ("to_roman(500)", "D"), 
                                                 ("to_roman(1000)", "M"),
                                                 ("to_roman(3)", "III"),
                                                 ("to_roman(8)", "VIII"),
                                                 ("to_roman(12)", "XII"),
                                                 ("to_roman(27)", "XXVII"),
                                                 ("to_roman(39)", "XXXIX"),
                                                 ("to_roman(4)", "IV"),
                                                 ("to_roman(9)", "IX"),
                                                 ("to_roman(40)", "XL"),
                                                 ("to_roman(90)", "XC"),
                                                 ("to_roman(400)", "CD"),
                                                 ("to_roman(900)", "CM"),
                                                 ("to_roman(944)", "CMXLIV"),
                                                 ("to_roman(1987)", "MCMLXXXVII"),
                                                 ("to_roman(3999)", "MMMCMXCIX")
                                                 ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
'''
def test_01_a_single_number():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"

def test_02_multiple_entries():
    assert to_roman(3) == 'III'
    assert to_roman(8) == 'VIII'
    assert to_roman(12) == 'XII'
    assert to_roman(27) == 'XXVII'
    assert to_roman(39) == 'XXXIX'

def test_03_odd_numerals():
    assert to_roman(4) == 'IV'
    assert to_roman(9) == 'IX'
    assert to_roman(40) == 'XL'
    assert to_roman(90) == 'XC'
    assert to_roman(400) == 'CD'
    assert to_roman(900) == 'CM'

def test_04_all_edge_cases():
    assert to_roman(944) == 'CMXLIV'
    assert to_roman(1987) == 'MCMLXXXVII'
    assert to_roman(3999) == 'MMMCMXCIX'
'''    
# added tests to cover different edge cases
