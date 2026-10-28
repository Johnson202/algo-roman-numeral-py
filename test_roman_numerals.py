from roman_numerals import to_roman
import pytest

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
    
# added tests to cover different edge cases
