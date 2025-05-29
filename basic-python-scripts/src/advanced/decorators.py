def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed.")

if __name__ == "__main__":
    display()