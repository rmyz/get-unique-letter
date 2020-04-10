from lib import get_first_unique_letter

first_input = 'AAB'
second_input = 'CBA'
third_input = 'ABAC'
fourth_input = 'ZXYXZ'

def test_first_input():
  assert get_first_unique_letter(first_input) == 'B'

def test_second_input():
  assert get_first_unique_letter(second_input) == 'C'

def test_third_input():
  assert get_first_unique_letter(third_input) == 'B'

def test_fourth_input():
  assert get_first_unique_letter(fourth_input) == 'Y'

def test_no_input():
  assert get_first_unique_letter() is None

def test_number_input():
  assert get_first_unique_letter(334) == '4'

def test_dict_input():
  assert get_first_unique_letter({"key": "value"}) is None

def test_list_input():
  assert get_first_unique_letter([1,2,3]) is None  