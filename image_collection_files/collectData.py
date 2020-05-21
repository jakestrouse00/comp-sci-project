import requests
import urllib.request
import threading
import os


def download(data, number, fileName):
    print(f"Downloading image number: {number}")
    r = requests.get(data['webformatURL'])
    with open(f'imageSets/{fileName}/{number}.jpeg', 'wb') as f:
        f.write(r.content)


# make_image_classifier --image_dir imageSets --tfhub_module https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4 --image_size 224 --saved_model_dir new_model --labels_output_file class_labels.txt

fileNames = ['tulip']


for fileName in fileNames:
    counter = 1
    os.makedirs(f'imageSets/{fileName}')
    print(f"Using {fileName}")


    terms = [f"blooming+{fileName}", f"growing+{fileName}", f"flowering+{fileName}", f"{fileName}+flower"]
    for term in terms:
        print(f"Searching for: {term}\n\n")
        for i in range(1, 6):
            print(f"Getting page {i}\n")
            payload = {
                #
                # 16280751-99ba762cf34dc9decbe913457
                'key': '16294474-358fcbcc51ad1592dd7d3c0af',
                'q': term,
                'image_type': 'photo',
                'colors': 'rgb',
                'per_page': 200,
                'page': i

            }
            try:
                r = requests.get('https://pixabay.com/api/', params=payload)
                b = r.json()
            except Exception as e:
                break
            for image in r.json()['hits']:
                threading.Thread(target=download, args=(image, counter,fileName)).start()
                counter += 1
