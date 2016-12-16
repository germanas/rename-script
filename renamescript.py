import os
for filename in os.listdir("."):
    if filename.startswith("dchha"):
        fileindex = filename.index(" ")
        os.rename(filename, filename[fileindex +1:])
