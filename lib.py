def get_first_unique_letter(input = ''):
  if(type(input) != str and type(input) != int):
    return None

  counter = []
  
  for letter in str(input):
    if(letter in counter):
      counter.remove(letter)
    else:
      counter.append(letter)

  try:
    return counter[0]
  except IndexError:
    return None
