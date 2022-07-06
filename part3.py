# Simple function  import to part2.py
def hello_world():
    print("hello world")


# Run code on line 8 only if it was called from this file
print(f"called from {__name__}.py") # see where it is calling from 
if __name__ == "__main__":
    hello_world()

