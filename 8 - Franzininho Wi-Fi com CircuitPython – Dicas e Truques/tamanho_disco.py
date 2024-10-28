import os
import gc

fs_stat = os.statvfs('/')
print("Disk size in MB", fs_stat[0] * fs_stat[2] / 1024 / 1024)
print("Free space in MB", fs_stat[0] * fs_stat[3] / 1024 / 1024)
print( gc.mem_free() )
