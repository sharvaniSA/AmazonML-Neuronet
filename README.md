

## Overview

This project involves developing a machine learning model to process images and predict specific entity values. The project includes data preparation, model development, and training components.

## Project Structure
student_resource3/  
├── src/  
│   ├── utils.py  
│   ├── model.py  
│   ├── train.py  
│   ├── test.py  
│   └── sanity.py  
├── dataset/  
│   ├── train.csv  
│   ├── test.csv  
│   ├── sample_test.csv  
│   └── sample_test_out.csv  
└── images/  
    ├── 1.jpg  
    ├── 2.jpg  
    └── ...  

- **`src/`**: Contains the source code for the project.
  - **`utils.py`**: Includes utility functions for data processing and image handling.
  - **`model.py`**: Defines the machine learning model architecture.
  - **`train.py`**: Handles the training process for the model.
  - **`test.py`**: Used for evaluating the model.
  - **`sanity.py`**: Contains sanity checks for the data and model.

- **`dataset/`**: Contains dataset files used for training and testing.
  - **`train.csv`**: CSV file containing training data.
  - **`test.csv`**: CSV file containing test data.
  - **`sample_test.csv`**: Sample test data file.
  - **`sample_test_out.csv`**: Output file for sample test results.

- **`images/`**: Directory containing image files used in the project.


## `utils.py`

### Functions

- **`common_mistake(unit)`**: Corrects common mistakes in unit names.
- **`parse_string(s)`**: Parses a string to extract numerical values and units.
- **`create_placeholder_image(image_save_path)`**: Creates a placeholder image for missing or invalid images.
- **`download_image(image_link, save_folder, retries=3, delay=3)`**: Downloads an image from a URL and saves it locally. Creates a placeholder image if the download fails.
- **`download_images(image_links, download_folder="student_resource3", allow_multiprocessing=True)`**: Downloads multiple images from URLs. Supports multiprocessing.
- **`preprocess_image(image_path)`**: Loads and preprocesses an image (resize and normalize).
- **`load_train_data(train_csv_path, images_dir)`**: Loads training data from a CSV file and preprocesses the corresponding images.

## `model.py`

- **Description**: Contains functions to build and compile the machine learning model.
- **Dependencies**: TensorFlow.

## `train.py`

- **Description**: Handles the training process of the model.
- **Functions**:
  - **Main Execution**: Loads training data, builds the model, trains it, and saves the trained model.
  - **Dependencies**: `load_train_data` from `utils.py`, `build_model` from `model.py`.

### Key Updates

- Fixed path issues by using relative paths for loading data.
- Ensured correct access to CSV and image files.

## `test.py`

- **Description**: Used for evaluating the model on test data.

## Errors and Resolutions

1. **ModuleNotFoundError**:
   - **Issue**: The `src` module could not be found.
   - **Resolution**: Added the parent directory of `src` to the Python path using `sys.path.append`.

2. **FileNotFoundError**:
   - **Issue**: Image files were not found.
   - **Resolution**: Verified paths and ensured correct image file names and locations.

3. **Handling Missing Images**:
   - Updated `download_images` function to create placeholder images for missing or inaccessible URLs.
   - Reduced multiprocessing pool size to avoid system errors.

## Next Steps

1. **Data Validation**: Ensure all image URLs in `train.csv` are valid and accessible.
2. **Model Tuning**: Experiment with model parameters and architecture for improved performance.
3. **Testing**: Thoroughly test the model with different datasets to evaluate its generalization ability.


