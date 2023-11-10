# ORB-Feature-Mapping-CV2

Sreamlit Link :
https://orb-feature-mapping-cv2git-pk87sanutxvgtrf7y8a3q2.streamlit.app/

## ORB
ORB (Oriented FAST and Rotated BRIEF) is a feature detection and descriptor extraction algorithm used in computer vision and image processing. It was developed to address the limitations of existing feature detection methods, such as SIFT (Scale-Invariant Feature Transform) and SURF (Speeded-Up Robust Features), by providing a fast and efficient alternative.

## Overview
This Streamlit web application allows users to upload an image and apply the ORB (Oriented FAST and Rotated BRIEF) feature mapping algorithm for keypoint detection and visualization.

## Features
- **File Uploader:** Users can upload images in jpg, png, or jpeg formats.
- **ORB Feature Mapping:** The application utilizes the ORB algorithm to detect keypoints in the uploaded image and overlays them with green points. The result is displayed alongside the original image.

## Usage
1. Install the required dependencies:

    ```bash
    pip install streamlit opencv-python numpy
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Open the provided URL in your web browser.

4. Upload an image using the file uploader.

5. View the ORB feature mapping result on the uploaded image.

## File Structure
- `app.py`: Main Streamlit application code.
- `requirements.txt`: List of required Python packages.
- (Add any additional files or directories as needed)

## How to Customize
- To modify the appearance or behavior of the web app, edit the `app.py` file.
- Customize the code based on your specific requirements.
- Feel free to extend the functionality or integrate additional features.

## Dependencies
- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

