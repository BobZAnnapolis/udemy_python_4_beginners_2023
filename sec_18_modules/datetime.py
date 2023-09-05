import os
import datetime
from time import sleep

os.system('clear')

print("\nsection 18. MODULES - DATE_TIME\n")

print(dir(datetime.datetime))
#print(f"today(): {datetime.datetime.today()}")
# print(f"....5")
# sleep(1)
# print(f"...4")
# sleep(1)
# print(f"..3")
# sleep(1)
# print(f".2")
# sleep(1)
# print(f"1")
# sleep(1)
# print("CONTINUING")

base = "users/john"
folder = "work"
filename = "holidayplans.csv"
full = os.path.join(base, folder, filename)
print(full)

os.path.isdir()