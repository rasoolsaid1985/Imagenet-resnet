# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15QguEntPiuS3j6qa-R5sqVuxUhH_qvG_
"""

import streamlit as st
import pandas as pd
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

model = load_model(r"D:\R\pycharm\PyCharm Community Edition 2024.1.4\project\imagenet\my_model.h5")
class_labels = {
    0: "accordion",
    1: "airplane",
    2: "ant",
    3: "antelope",
    4: "apple",
    5: "armadillo",
    6: "artichoke",
    7: "axe",
    8: "baby bed",
    9: "backpack",
    10: "bagel",
    11: "balance beam",
    12: "banana",
    13: "band aid",
    14: "banjo",
    15: "baseball",
    16: "basketball",
    17: "bathing cap",
    18: "beaker",
    19: "bear",
    20: "bee",
    21: "bell pepper",
    22: "bench",
    23: "bicycle",
    24: "binder",
    25: "bird",
    26: "bookshelf",
    27: "bow",
    28: "bow tie",
    29: "bowl",
    30: "brassiere",
    31: "burrito",
    32: "bus",
    33: "butterfly",
    34: "camel",
    35: "can opener",
    36: "car",
    37: "cart",
    38: "cattle",
    39: "cello",
    40: "centipede",
    41: "chain saw",
    42: "chair",
    43: "chime",
    44: "cocktail shaker",
    45: "coffee maker",
    46: "computer keyboard",
    47: "computer mouse",
    48: "corkscrew",
    49: "cream",
    50: "croquet ball",
    51: "crutch",
    52: "cucumber",
    53: "cup or mug",
    54: "diaper",
    55: "digital clock",
    56: "dishwasher",
    57: "dog",
    58: "domestic cat",
    59: "dragonfly",
    60: "drum",
    61: "dumbbell",
    62: "electric fan",
    63: "elephant",
    64: "face powder",
    65: "fig",
    66: "filing cabinet",
    67: "flower pot",
    68: "flute",
    69: "fox",
    70: "french horn",
    71: "frog",
    72: "frying pan",
    73: "giant panda",
    74: "goldfish",
    75: "golf ball",
    76: "golfcart",
    77: "guacamole",
    78: "guitar",
    79: "hair dryer",
    80: "hair spray",
    81: "hamburger",
    82: "hammer",
    83: "hamster",
    84: "harmonica",
    85: "harp",
    86: "hat with a wide brim",
    87: "head cabbage",
    88: "helmet",
    89: "hippopotamus",
    90: "horizontal bar",
    91: "horse",
    92: "hotdog",
    93: "iPod",
    94: "isopod",
    95: "jellyfish",
    96: "koala bear",
    97: "ladle",
    98: "ladybug",
    99: "lamp",
    100: "laptop",
    101: "lemon",
    102: "lion",
    103: "lipstick",
    104: "lizard",
    105: "lobster",
    106: "maillot",
    107: "maraca",
    108: "microphone",
    109: "microwave",
    110: "milk can",
    111: "miniskirt",
    112: "monkey",
    113: "motorcycle",
    114: "mushroom",
    115: "nail",
    116: "neck brace",
    117: "oboe",
    118: "orange",
    119: "otter",
    120: "pencil box",
    121: "pencil sharpener",
    122: "perfume",
    123: "person",
    124: "piano",
    125: "pineapple",
    126: "ping-pong ball",
    127: "pitcher",
    128: "pizza",
    129: "plastic bag",
    130: "plate rack",
    131: "pomegranate",
    132: "popsicle",
    133: "porcupine",
    134: "power drill",
    135: "pretzel",
    136: "printer",
    137: "puck",
    138: "punching bag",
    139: "purse",
    140: "rabbit",
    141: "racket",
    142: "ray",
    143: "red panda",
    144: "refrigerator",
    145: "remote control",
    146: "rubber eraser",
    147: "rugby ball",
    148: "ruler",
    149: "salt or pepper shaker",
    150: "saxophone",
    151: "scorpion",
    152: "screwdriver",
    153: "seal",
    154: "sheep",
    155: "ski",
    156: "skunk",
    157: "snail",
    158: "snake",
    159: "snowmobile",
    160: "snowplow",
    161: "soap dispenser",
    162: "soccer ball",
    163: "sofa",
    164: "spatula",
    165: "squirrel",
    166: "starfish",
    167: "stethoscope",
    168: "stove",
    169: "strainer",
    170: "strawberry",
    171: "stretcher",
    172: "sunglasses",
    173: "swimming trunks",
    174: "swine",
    175: "syringe",
    176: "table",
    177: "tape player",
    178: "tennis ball",
    179: "tick",
    180: "tie",
    181: "tiger",
    182: "toaster",
    183: "traffic light",
    184: "train",
    185: "trombone",
    186: "trumpet",
    187: "turtle",
    188: "tv or monitor",
    189: "unicycle",
    190: "vacuum",
    191: "violin",
    192: "volleyball",
    193: "waffle iron",
    194: "washer",
    195: "water bottle",
    196: "watercraft",
    197: "whale",
    198: "wine bottle",
    199: "zebra",
}
def process_image(image):
  img = image.resize((224, 224))
  image_array = img_to_array(img)
  image_array = np.expand_dims(image_array, axis=0)
  image_array /= 255.0
  return image_array

def predict(img_array, model):
  prediction = model.predict(img_array)
  return prediction

"""##Streamlit work"""

st.title("Imagene Detection")
st.write("Upload an image and get a prediction")

upload_files = st.file_uploader("Upload Files", type=['png', 'jpg'], accept_multiple_files=True)

if upload_files is not None:
  for uploaded_file in upload_files:
    image = load_img(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    processed_image = process_image(image)
    prediction = predict(processed_image, model)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_index]

    st.write(f"Prediction: {prediction}")
    st.write(f"Predicted Class: {predicted_class_label}")
    st.image(image, caption='Processed Image', use_column_width=True)



