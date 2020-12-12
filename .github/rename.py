import os
import re
files = os.listdir("../.")

jpgs = [i for i in files if re.search(".jpg", i)]
pngs = [i for i in files if re.search(".png", i)]

for v,i in enumerate(jpgs):
    newname = f"{str(v).zfill(4)}.jpg"
    if i != newname:
        os.rename(f"../{i}", f"../{newname}")

for v,i in enumerate(pngs):
    newname = f"{str(v+len(jpgs)).zfill(4)}.png"
    if i != newname:
        os.rename(f"../{i}", f"../{newname}")
