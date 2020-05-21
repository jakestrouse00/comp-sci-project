import os

for folder in os.listdir("imageSets"):
    for file in os.listdir(f"imageSets/{folder}"):
        size = os.path.getsize(f"imageSets/{folder}/"+file)
        if int(size) == 0:
            os.remove(f"imageSets/{folder}/"+file)
            print('removed a file')
