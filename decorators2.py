import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

# Test it
result = my_function(3, 5)
print(f"Result: {result}")  # This will show: Result: 8