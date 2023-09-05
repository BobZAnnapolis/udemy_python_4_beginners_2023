import os

os.system('clear')

print("\nsection 16.ERROR HANDLING\n")

print("")

def floor_divide(a: int, b: int) -> int:
    """Return a floor divided by b."""
    # Write your try/except statement in the function body.
    try:
        return a // b
    except:
        return 0
print(floor_divide(10, 2))
print(floor_divide(100, 25))
print(floor_divide(100, 0))

def food_selection(choice: int) -> str:
    """Return a specific food from the list."""
    # Write your try/except statement in the function body.
    foods = ["Ham", "Cheese", "Tomato", "Bread"]
    try:
        return foods[choice]
    except IndexError:
        return False
    except TypeError:
        return 0

print(food_selection(1))
print(food_selection(9))
print(food_selection("ABC"))
