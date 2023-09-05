import os
from time import sleep

os.system('clear')

print("\nsection 18. MODULES - OS   \n")

#print(f"print(dir(os)): {dir(os)}")
print(f"os.getcwd(): {os.getcwd()}")
#print(f"os.chdir(BAD_PATH): {os.chdir('BAD_PATH')}")
print(f"os.chdir(sec_18_modules): {os.chdir('sec_18_modules')}")
print(f"os.getcwd(): {os.getcwd()}")
print(f"os.chdir(..)")
os.chdir("..")
print(f"os.getcwd(): {os.getcwd()}")
print(f"os.mkdir(NEW_DIR): {os.mkdir('NEW_DIR')}")
sleep(2)
print(f"os.rmdir(NEW_DIR) {os.rmdir('NEW_DIR')}")
print(f"os.getcwd(): {os.getcwd()}")
print(f"os.listdir(os.getcwd()): \n\t{os.listdir(os.getcwd())}")
for f in os.listdir(os.getcwd()):
    print(f)
print(f"os.walk(os.getcwd()): \n\t{os.walk(os.getcwd())}")
for f in os.walk(os.getcwd()):
    print(f)




print(" ")
