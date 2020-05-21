import os
import random

for i in range(10):
    for folder in os.listdir('imageSets'):
        totalFiles = len(os.listdir(f"imageSets/{folder}"))
        p = random.randint(0, totalFiles)
        randomFile = random.choice(os.listdir(f"imageSets/{folder}"))
        print(randomFile)
        with open(f'imageSets/{folder}/{randomFile}', 'rb') as f:
            savedFile = f.read()
        os.remove(f'imageSets/{folder}/{randomFile}')
        with open(f'testing/{"".join(random.choices("1234567890", k=5))}.jpeg', 'wb') as fp:
            fp.write(savedFile)