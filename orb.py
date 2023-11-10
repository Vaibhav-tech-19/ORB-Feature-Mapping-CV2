import streamlit as st
import cv2
import numpy as np

st.title("ORB Feature Mapping WebApp")
st.markdown("**Developed by Vaibhav**", unsafe_allow_html=True)

# Function to apply ORB feature mapping
def apply_orb(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find the keypoints with ORB
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Draw the keypoints on the image
    orb_image = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)

    return orb_image

image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if image is not None:
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    height, width = image.shape[:2]

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Apply ORB feature mapping
    orb_image = apply_orb(image)
    st.image(orb_image, caption="ORB Feature Mapping", use_column_width=True)
