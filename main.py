def replace(text, old, new=''):   
  return ''.join(new if i in old else i for i in text)


def product(lst, start=1):
    return [start * i for i in lst] and start * lst[0] if lst else start