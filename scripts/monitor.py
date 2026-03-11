import psutil
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

print("CPU bruk:", cpu)
print("RAM bruk:", ram)