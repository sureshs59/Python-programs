
print("############MATCH:######################")

DAY = 3

match DAY:
	case 1:
		print("MONDAY")
	case 2:
		print("TUESDAY")
	case 3:
		print("WEDNESDAY")
	case 4:
		print("THURSDAY")
	case 5:
		print("FRIDAY")
	case 6:
		print("SATURDAY")
	case 7:
		print("SUNDAY")
	case _: # default block if nothing matches
		print("Looking forward to the Weekend")
		
print("#######Combine Values ##########")

print("*****Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one****")

day = 3

match day:
	case 1 | 2 | 3 | 4 | 5:
		print("Its a week day..")
	case 6 | 7:
		print("Its a weeked..")
		
print("#######If Statements as Guards##########")

		
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
	
	
	
	