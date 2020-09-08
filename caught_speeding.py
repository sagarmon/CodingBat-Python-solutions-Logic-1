def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 60 + 5:
      return 0
    elif 61 + 5 <= speed <= 80 + 5:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif 61 <= speed <= 80:
      return 1
    else:
      return 2
