time = int(input("Enter the time:"))
timeinhr = time%60
timeinmint = timeinhr//60
timeinsec = timeinmint%60
print(f"your time in HH:MM:SS {timeinhr}:{timeinmint}:{timeinsec}")
