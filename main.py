nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0].upper()
numbers = nric[1:8]
suffix = nric[8:]
valid = False

dictST = "JZIHGFEDCBA"
dictFG = "XWUTRQPNMLK"

if prefix in "STFG" and numbers.isdigit() and len(suffix) == 1 and suffix.isalpha():
  check = 0
  weight = [2, 7, 6, 5, 4, 3, 2]
  for i in range(7):
    check += weight[i] * int(numbers[i])
  if prefix in "TG":
    check += 4
  checknum = check % 11
  if prefix in "ST":
    if suffix == dictST[checknum]:
      valid = True
  else:
    if suffix == dictFG[checknum]:
      valid = True

if valid:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")