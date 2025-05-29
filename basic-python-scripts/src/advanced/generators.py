def simple_generator():
    yield "First value"
    yield "Second value"
    yield "Third value"

# Example usage of the generator
if __name__ == "__main__":
    for value in simple_generator():
        print(value)