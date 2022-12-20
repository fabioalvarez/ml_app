import json
import os
import time

import numpy as np
import redis
import settings
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = redis.Redis(host=settings.REDIS_IP,
                 port=settings.REDIS_PORT,
                 db=settings.REDIS_DB_ID)
# TODO
# Load your ML model and assign to variable `model`
# See https://drive.google.com/file/d/1ADuBSE4z2ZVIdn66YDSwxKv-58U7WEOn/view?usp=sharing
# for more information about how to use this model.
model = ResNet50(include_top=True, weights="imagenet")


def predict(image_name):
    """
    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.

    Parameters
    ----------
    image_name : str
        Image filename.

    Returns
    -------
    class_name, pred_probability : tuple(str, float)
        Model predicted class as a string and the corresponding confidence
        score as a number.
    """
    class_name = None
    pred_probability = None
    # TODO

    # Image load
    img = image.load_img(os.path.join(settings.UPLOAD_FOLDER, image_name), target_size=(224, 224))

    # We need to convert the PIL image to a Numpy
    # array before sending it to the model
    x = image.img_to_array(img)

    # Also we must add an extra dimension to this array
    # because our model is expecting as input a batch of images.
    # In this particular case, we will have a batch with a single
    # image inside
    x_batch = np.expand_dims(x, axis=0)

    # Now we must scale pixels values
    x_batch = preprocess_input(x_batch)

    # Run model on batch of images
    preds = model.predict(x_batch)

    # We can get and print the predicted label 
    # with the highest probability
    pred = decode_predictions(preds, top=1)

    class_name = pred[0][0][1]
    pred_probability = round(pred[0][0][2], 4)

    return class_name, pred_probability


def classify_process():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, uses the loaded ML
    model to get predictions and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.
    """
    while True:
        # Inside this loop you should add the code to:
        #   1. Take a new job from Redis
        job = db.brpop(settings.REDIS_QUEUE)[1]

        job = json.loads(job.decode("utf-8"))

        image_name = job["image_name"]
        job_id = job["id"]

        #   2. Run your ML model on the given data
        prediction, score = predict(image_name)

        #   3. Store model prediction in a dict with the following shape:
        rpse = { "prediction": str(prediction), "score": float(score)}

        #   4. Store the results on Redis using the original job ID as the key
        db.set(job_id, json.dumps(rpse))

        # Don't forget to sleep for a bit at the end
        time.sleep(settings.SERVER_SLEEP)


if __name__ == "__main__":
    # Now launch process
    print("Launching ML service...")
    classify_process()