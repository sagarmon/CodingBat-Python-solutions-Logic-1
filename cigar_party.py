def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  return 40 <= cigars <= 60
  
  if is_weekend and cigars >= 40:
    return True
  elif 40 <= cigars <= 60:
    return True
  else:
    return False
