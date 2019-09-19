# 5.1.6.2 Useful exceptions

# this code cannot be terminated
# by pressing Ctrl-C

from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")