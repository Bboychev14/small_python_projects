def document(func):
    def wrapper(*param):
        print('Function name: ', func.__name__)
        print('Arguments: ', param)
        result = func(*param)
        print('Result: ', result)
        return result
    return wrapper


def square(func):
    def wrapper(*param):
        result = func(*param) ** 2
        print("The Square of the result is: ", result)
        return result
    return wrapper


@document
@square
def multiply(a, b):
    return a * b


multiply(5, 9)