# import re
# import constants
# import os
# import requests
# import pandas as pd
# import multiprocessing
# import time
# from time import time as timer
# from tqdm import tqdm
# import numpy as np
# from pathlib import Path
# from functools import partial
# import requests
# import urllib
# from PIL import Image

# def common_mistake(unit):
#     if unit in constants.allowed_units:
#         return unit
#     if unit.replace('ter', 'tre') in constants.allowed_units:
#         return unit.replace('ter', 'tre')
#     if unit.replace('feet', 'foot') in constants.allowed_units:
#         return unit.replace('feet', 'foot')
#     return unit

# def parse_string(s):
#     s_stripped = "" if s==None or str(s)=='nan' else s.strip()
#     if s_stripped == "":
#         return None, None
#     pattern = re.compile(r'^-?\d+(\.\d+)?\s+[a-zA-Z\s]+$')
#     if not pattern.match(s_stripped):
#         raise ValueError("Invalid format in {}".format(s))
#     parts = s_stripped.split(maxsplit=1)
#     number = float(parts[0])
#     unit = common_mistake(parts[1])
#     if unit not in constants.allowed_units:
#         raise ValueError("Invalid unit [{}] found in {}. Allowed units: {}".format(
#             unit, s, constants.allowed_units))
#     return number, unit


# def create_placeholder_image(image_save_path):
#     try:
#         placeholder_image = Image.new('RGB', (100, 100), color='black')
#         placeholder_image.save(image_save_path)
#     except Exception as e:
#         return

# def download_image(image_link, save_folder, retries=3, delay=3):
#     if not isinstance(image_link, str):
#         return

#     filename = Path(image_link).name
#     image_save_path = os.path.join(save_folder, filename)

#     if os.path.exists(image_save_path):
#         return

#     for _ in range(retries):
#         try:
#             urllib.request.urlretrieve(image_link, image_save_path)
#             return
#         except:
#             time.sleep(delay)
    
#     create_placeholder_image(image_save_path) #Create a black placeholder image for invalid links/images

# # def download_images(image_links, download_folder="student_resource 3", allow_multiprocessing=True):
# #     if not os.path.exists(download_folder):
# #         os.makedirs(download_folder)
# #     print(f"Images will be downloaded to: {os.path.abspath(download_folder)}")
# #     if allow_multiprocessing:
# #         download_image_partial = partial(
# #             download_image, save_folder=download_folder, retries=3, delay=3)

# #         with multiprocessing.Pool(64) as pool:
# #             list(tqdm(pool.imap(download_image_partial, image_links), total=len(image_links)))
# #             pool.close()
# #             pool.join()
# #     else:
# #         for image_link in tqdm(image_links, total=len(image_links)):
# #             download_image(image_link, save_folder=download_folder, retries=3, delay=3)

# def download_images(image_links, download_folder="student_resource3", allow_multiprocessing=True):
#     if not os.path.exists(download_folder):
#         os.makedirs(download_folder)
#     print(f"Images will be downloaded to: {os.path.abspath(download_folder)}")
    
#     if allow_multiprocessing:
#         download_image_partial = partial(
#             download_image, save_folder=download_folder, retries=3, delay=3)

#         # Reduce the number of workers to avoid the ValueError
#         with multiprocessing.Pool(16) as pool:  # Change from 64 to 16 workers
#             list(tqdm(pool.imap(download_image_partial, image_links), total=len(image_links)))
#             pool.close()
#             pool.join()
#     else:
#         for image_link in tqdm(image_links, total=len(image_links)):
#             download_image(image_link, save_folder=download_folder, retries=3, delay=3)



# from PIL import Image
# import numpy as np

# def preprocess_image(image_path):
#     """Load and preprocess an image for model input."""
#     try:
#         image = Image.open(image_path)
#         image = image.resize((224, 224))  # Resize to 224x224
#         image = np.array(image) / 255.0  # Normalize pixel values
#         return image
#     except Exception as e:
#         print(f"Error processing image {image_path}: {e}")
#         return None


# import pandas as pd
# import os

# def load_train_data(train_csv_path, images_dir):
#     """Load training data from CSV and preprocess images."""
#     df = pd.read_csv(train_csv_path)
#     images = []
#     labels = []

#     for index, row in df.iterrows():
#         image_path = os.path.join(images_dir, f"{index + 1}.jpg")  # Use 1-based indexing for image filenames
#         image = preprocess_image(image_path)
#         if image is not None:
#             images.append(image)
#             labels.append(row['entity_value'])
    
#     return np.array(images), np.array(labels)
import os
import requests
import pandas as pd
import multiprocessing
import time
from tqdm import tqdm
import numpy as np
from pathlib import Path
from functools import partial
import urllib
from PIL import Image
import constants
import re

def common_mistake(unit):
    if unit in constants.allowed_units:
        return unit
    if unit.replace('ter', 'tre') in constants.allowed_units:
        return unit.replace('ter', 'tre')
    if unit.replace('feet', 'foot') in constants.allowed_units:
        return unit.replace('feet', 'foot')
    return unit

def parse_string(s):
    s_stripped = "" if s == None or str(s) == 'nan' else s.strip()
    if s_stripped == "":
        return None, None
    pattern = re.compile(r'^-?\d+(\.\d+)?\s+[a-zA-Z\s]+$')
    if not pattern.match(s_stripped):
        raise ValueError("Invalid format in {}".format(s))
    parts = s_stripped.split(maxsplit=1)
    number = float(parts[0])
    unit = common_mistake(parts[1])
    if unit not in constants.allowed_units:
        raise ValueError("Invalid unit [{}] found in {}. Allowed units: {}".format(
            unit, s, constants.allowed_units))
    return number, unit

def create_placeholder_image(image_save_path):
    try:
        placeholder_image = Image.new('RGB', (100, 100), color='black')
        placeholder_image.save(image_save_path)
    except Exception as e:
        print(f"Error creating placeholder image: {e}")

def download_image(image_link, save_folder, retries=3, delay=3):
    if not isinstance(image_link, str):
        return

    filename = Path(image_link).name
    image_save_path = os.path.join(save_folder, filename)

    if os.path.exists(image_save_path):
        return

    for _ in range(retries):
        try:
            urllib.request.urlretrieve(image_link, image_save_path)
            return
        except Exception as e:
            print(f"Error downloading image {image_link}: {e}")
            time.sleep(delay)
    
    create_placeholder_image(image_save_path)  # Create a black placeholder image for invalid links/images

def download_images(image_links, download_folder="student_resource3", allow_multiprocessing=True):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    print(f"Images will be downloaded to: {os.path.abspath(download_folder)}")

    if allow_multiprocessing:
        download_image_partial = partial(
            download_image, save_folder=download_folder, retries=3, delay=3)

        # Reduce the number of workers to avoid the ValueError
        with multiprocessing.Pool(16) as pool:  # Change from 64 to 16 workers
            list(tqdm(pool.imap(download_image_partial, image_links), total=len(image_links)))
            pool.close()
            pool.join()
    else:
        for image_link in tqdm(image_links, total=len(image_links)):
            download_image(image_link, save_folder=download_folder, retries=3, delay=3)

def preprocess_image(image_path):
    """Load and preprocess an image for model input."""
    try:
        image = Image.open(image_path)
        image = image.resize((224, 224))  # Resize to 224x224
        image = np.array(image) / 255.0  # Normalize pixel values
        return image
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def load_train_data(train_csv_path, images_dir):
    """Load training data from CSV and preprocess images."""
    df = pd.read_csv(train_csv_path)
    images = []
    labels = []

    # Download images
    image_links = [row['image_link'] for index, row in df.iterrows()]
    download_images(image_links, download_folder=images_dir)

    # Load and preprocess images
    for index, row in df.iterrows():
        image_path = os.path.join(images_dir, f"{index + 1}.jpg")  # Use 1-based indexing for image filenames
        image = preprocess_image(image_path)
        if image is not None:
            images.append(image)
            labels.append(row['entity_value'])
    
    return np.array(images), np.array(labels)
