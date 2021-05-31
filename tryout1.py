
def my_function():
  print("Hello from a function")
 
def do_stuff_with_file():
    f = open("c:\\my_python_tryout\\tryout1.py", "r")
    print(f.read())
    
    f = open("c:\\my_python_tryout\\output.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


def main():
    the_world_is_flat = True
    if the_world_is_flat:
        print("Be careful not to fall off!")
    my_function()
    my_function()
    
    #do_stuff_with_file()
    
    assert sum([1, 1, 1]) == 3
    test_sum()
    test_sum_tuple()

if __name__ == "__main__":
    main()
    print("Everything passed")