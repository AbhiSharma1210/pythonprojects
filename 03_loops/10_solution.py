import time

waitTime = 1
maxRetries = 5
attempts = 0
while attempts < maxRetries:
    print("Attempt", attempts + 1, "- wait time", waitTime, )
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1
