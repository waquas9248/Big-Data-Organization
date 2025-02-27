from skimage.feature import hog
from skimage.io import imread
from skimage.transform import rescale
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import StandardScaler, Normalizer
import skimage
import sys
import os
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from array import array
from sklearn.cluster import MiniBatchKMeans
from google.cloud import storage
import psutil

Image.MAX_IMAGE_PIXELS=None
dataframe = pd.DataFrame(columns=["Data", "URL"])
entriesPerFrame = 1000


os.environ['516778109899-compute@developer.gserviceaccount.com'] = r'/mnt/se-413-375302-7cd244d5721a.json'


pd.set_option("display.max_colwidth", None)
count = 1
fileNum = 0
client = storage.Client()
bucket = client.get_bucket('schooldataset')
for dirpath, dirnames, files in os.walk('/mnt/Google'):
    for f in files:
        if f.endswith(".jpg") and os.path.getsize(os.path.join(dirpath,f)) <= 6000000:
           # scale down the image to one third
            print(os.path.join(dirpath,f))
            img = imread(os.path.join(dirpath,f), as_gray=True)
            img = resize(img, (150, 150))

            # calculate the hog and return a visual representation.
            dog_hog, dog_hog_img = hog(img, pixels_per_cell=(21,21), cells_per_block=(2, 2), orientations=9, visualize=True, block_norm='L2-Hys')
 
            df = pd.DataFrame({"Data": [dog_hog], "URL": os.path.join(dirpath,f)})
            dataframe = pd.concat([dataframe,df])
            print('RAM memory % used:', psutil.virtual_memory()[2])
            if count % entriesPerFrame == 0:
                dataframe.to_csv(f'/mnt/d/Users/nate6/Documents/Dataframes/frame{fileNum}.csv', index=False)
                fileNum = fileNum + 1
                dataframe = pd.DataFrame(columns=["Data", "URL"])

            count = count + 1
            print(count)
            print('RAM memory % used:', psutil.virtual_memory()[2])
            plt.close()

print("Finish")
