import time

wait_time = 1 #sec
max_retries = 3
attempts = 0

while attempts < max_retries:
    # print("Attempts",attempts+1, "-wait time: ",wait_time)
    print(f"Attempts {attempts+1}, having waiting time: {wait_time}")
    time.sleep(wait_time)

    wait_time *=2
    attempts +=1