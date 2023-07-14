# from functools import wraps
# import time

# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
#         return result

# def func_decorator(func_to_decorate):
#     def decorated_func():
#         print("Start working")
#         func_to_decorate()
#         print("finished!")

#     return decorated_func