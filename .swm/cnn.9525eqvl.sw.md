---
title: CNN
---
# Introduction

This document will walk you through the implementation of the Convolutional Neural Network (CNN) feature.

The feature involves setting up a CNN for image classification using <SwmToken path="/cnn.py" pos="1:2:2" line-data="import tensorflow as tf">`tensorflow`</SwmToken> and Keras.

We will cover:

1. Data preprocessing


2. Model architecture


3. Training setup

# Code flow

## Data preprocessing

<SwmSnippet path="/cnn.py" line="1">

---

We start by defining the data augmentation for the training dataset. This helps in improving the model's generalization by applying random transformations to the input images.

```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np


# Assuming you have a dataset of images organized into folders
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
```

---

</SwmSnippet>

<SwmSnippet path="/cnn.py" line="13">

---

Next, we set up the data generator for the training dataset. This generator will read images from the specified directory, apply the transformations, and rescale the pixel values.

```

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'path/to/train',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical')
```

---

</SwmSnippet>

<SwmSnippet path="/cnn.py" line="21">

---

Similarly, we set up the data generator for the validation dataset. This generator will only rescale the pixel values without applying any transformations.

```

validation_generator = test_datagen.flow_from_directory(
        'path/to/validation',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical')

```

---

</SwmSnippet>

## Model architecture

<SwmSnippet path="/cnn.py" line="28">

---

We define the CNN model using the Sequential API. The model consists of multiple convolutional and pooling layers followed by fully connected layers. This architecture is designed to extract features from the images and perform classification.

```

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2,   
 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(num_classes, activation='softmax')
])
```

---

</SwmSnippet>

# Conclusion

This document explained the implementation of the CNN feature by covering data preprocessing, model architecture, and training setup. The data generators handle image loading and augmentation, while the model architecture is designed to effectively classify the images.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc3dpbW0lM0ElM0FHb3plbjI0" repo-name="swimm"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
