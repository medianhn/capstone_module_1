from datetime import datetime

nowA = datetime.now()

#suatu proses A

waktu_komputasiA = datetime.now() - nowA

nowB = datetime.now()

# suatu proses B

waktu_komputasiB = datetime.now() - nowB

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)