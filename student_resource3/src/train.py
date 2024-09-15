import sys
import os
from src.utils import load_train_data
from src.model import build_model

# Add the parent directory of `src` to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Construct paths relative to the `src` directory
train_csv_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'train.csv')
images_dir = os.path.join(os.path.dirname(__file__), '..', 'images')

# Load the data
images, labels = load_train_data(train_csv_path, images_dir)

# Build and train the model
model = build_model()
model.fit(images, labels, epochs=10, validation_split=0.2)
model.save('model.h5')
