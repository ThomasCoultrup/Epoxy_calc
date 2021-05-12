import math

def round_up(n, decimals=0):
  multiplier = 10 ** decimals
  return math.ceil(n * multiplier) / multiplier

def ask_input(question):
  while True:
    val = input(question)
    if val.lower() == 'y' or val.lower() == 'n':
      return val.lower()
    else:
      print("Invalid input")
      continue

while True:
  user_sq_ft = input("Enter your square feet: ")

  sq_ft = int(user_sq_ft)

  covering_sides = ask_input("Are you covering the sides? Y or N: ")
  
  if covering_sides == 'y':
    gallons_flood_coat = ((sq_ft * 0.3) + sq_ft) / 14
  elif covering_sides == 'n':
    gallons_flood_coat = sq_ft / 14
  
  flood_coat = ask_input("Do you need a seal coat? Y or N: ")
  
  if flood_coat == 'n':
    print(f"{round_up(gallons_flood_coat)} gallons flood coat")
    continue
  
  seal_coat = ask_input("Does it need more than one seal coat? Y or N: ")

  if seal_coat == 'n':
    gallons_seal_coat = sq_ft / 48
  if seal_coat == 'y':
    gallons_seal_coat = (sq_ft * 3) / 48

  gallons_total = round_up(gallons_flood_coat) + round_up(gallons_seal_coat)
  
  print(f"{round_up(gallons_seal_coat)} gallons seal coat")
  print(f"{round_up(gallons_flood_coat)} gallons flood coat")
  print(f"{round_up(gallons_total)} gallons total")
