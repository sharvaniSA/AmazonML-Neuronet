from src.utils import preprocess_image
import pandas as pd
import numpy as np
import os
import tensorflow as tf

def load_test_data(test_csv_path, images_dir):
    """Load and preprocess test images."""
    df = pd.read_csv(test_csv_path)
    images = []

    for index, row in df.iterrows():
        image_path = os.path.join(images_dir, f"{row['index']}.jpg")
        image = preprocess_image(image_path)
        if image is not None:
            images.append(image)
    
    return np.array(images)

def predict_and_save(model_path, test_csv_path, images_dir, output_csv_path):
    """Load the model, make predictions, and save results to a CSV file."""
    model = tf.keras.models.load_model(model_path)
    test_images = load_test_data(test_csv_path, images_dir)
    predictions = model.predict(test_images)
    
    # Assuming predictions are in a format that needs to be converted to your required format
    df_test = pd.read_csv(test_csv_path)
    df_test['prediction'] = [f"{pred[0]:.2f} unit" for pred in predictions]  # Adjust formatting as needed
    df_test[['index', 'prediction']].to_csv(output_csv_path, index=False)

model_path = 'model.h5'
test_csv_path = 'dataset/test.csv'
images_dir = 'images/'
output_csv_path = 'dataset/test_out.csv'

predict_and_save(model_path, test_csv_path, images_dir, output_csv_path)
