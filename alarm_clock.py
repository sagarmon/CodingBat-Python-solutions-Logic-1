def alarm_clock(day, vacation):
  weekdays = [1, 2, 3, 4, 5]
  weekends = [0, 6]
  
  if day in weekdays:
    if vacation:
      return "10:00"
    return "7:00"
  elif day in weekends:
    if vacation:
      return "off"
    return "10:00"
