import time
from time import perf_counter

start = perf_counter()
end = perf_counter()
something = perf_counter()

print(f"Time taken for 1 million calls: {start:.6f} {end:.6f} {something:.6f} seconds")
