import time
import threading

# using monotonic time for performance testing
# start_time = time.monotonic()
# count = 0
# for i in range(200_000):
#     count += 1
# print(time.monotonic() - start_time)

# # using sleep to pause program execution for n seconds
# for i in range(5):
#     print("foo")
#     time.sleep(2)


# Running code in a separate thread without blocking the program
def delayed_print(text, seconds):
    time.sleep(seconds)
    print(text)


thread = threading.Thread(target=delayed_print, args=("printed after delay", 2))
thread.start()

print("printed before delay but after thread started")
