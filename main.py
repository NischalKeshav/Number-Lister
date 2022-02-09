nums_list = []
numberOf = float(input("How namy numbers do you want to compare? ")) - 1
nums = float(input("Enter your first numbers: "))
nums_list.append(nums)
state = True
while state is True:
  while numberOf > 0:
    nums = float(input("Enter your next number: "))
    nums_list.append(nums)
    numberOf = numberOf - 1
  if numberOf == 0:
    while state is True:  
      nums_list = sorted(nums_list, reverse = False)
      print(nums_list)
      state  = False
      break
