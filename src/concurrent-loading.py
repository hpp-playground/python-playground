import concurrent.futures
import random
import time


def sample_func(index):
    print("index: %s started." % index)
    sleep_seconds = random.randint(2, 4)
    time.sleep(sleep_seconds)
    print("index: %s ended." % index)
    return index


future_list = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(20):
        future = executor.submit(sample_func, index=i)
        future_list.append(future)
    res_future = concurrent.futures.as_completed(fs=future_list)

print("completed.")
for r in res_future:
    print(r.result())
