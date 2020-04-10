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

if __name__ == '__main__':
  print('AAB ->', get_first_unique_letter('AAB'))
  print('CBA ->', get_first_unique_letter('CBA'))
  print('ABAC ->', get_first_unique_letter('ABAC'))
  print('ZXYXZ ->', get_first_unique_letter('ZXYXZ'))
