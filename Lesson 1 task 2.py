time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = (time //60 - hours *60)
seconds = time % 60
print(f"Time is displayed in the following format: hh:mm:ss:  {hours} : {minutes} : {seconds}")
