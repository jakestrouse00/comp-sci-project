import tensorflow as tf
import numpy as np
import random
import os
import matplotlib.pyplot as plt


class Predict:
    def __init__(self, model, images):
        self.labels = os.listdir('imageSets')
        self.imageFile = images
        # loads the model passed for future uses
        self.reloaded = tf.keras.models.load_model(model)

    def saveAndLoad(self, doRandom, fileNumber):
        """Chooses a random image from the testing folder, and writes it to the test folder to be predicted. Then the filename for the images is returned"""
        if doRandom == 2:
            randomFile = random.choice(os.listdir(f"{self.imageFile}"))
        else:
            randomFile = os.listdir(f"{self.imageFile}")[int(fileNumber)]
        with open(f'testing/{randomFile}', 'rb') as f:
            savedFile = f.read()
        savedName = "".join(random.choices("1234567890", k=5)) + ".jpeg"
        with open(f'test/placment/{savedName}', 'wb') as fp:
            fp.write(savedFile)
        return savedName

    def removeTest(self, fileName):
        """Removes the image from the test folder. This is called after a prediction has been made."""
        os.remove(f'test/placment/{fileName}')

    def loadImage(self):
        """Loads the image into the model and formats it. The image data is returned."""
        image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255)
        image_data = image_generator.flow_from_directory(directory=str("test"), target_size=(224, 224))
        return image_data

    def displayShapes(self, image_data):
        """Displays the shape of the image"""
        for image_batch, label_batch in image_data:
            print("Image batch shape: ", image_batch.shape)
            print("Label batch shape: ", label_batch.shape)
            break

    def makePrediction(self, image_data, imageName):
        # makes a prediction
        reloaded_result_batch = self.reloaded.predict(image_data[0][0])
        # translates the prediction into the category
        predicted_class_name = self.labels[int(np.argmax(reloaded_result_batch))]
        # loads the image to be displayed to the user along with the prediction
        with open(f'test/placment/{imageName}', 'rb') as image_file:
            image = plt.imread(image_file)
        plt.grid(False)
        plt.imshow(image, cmap=plt.cm.binary)
        plt.title(f"Prediction: {predicted_class_name}")
        plt.show()


