import streamlit as st
import cv2
import numpy as np

st.title("ORB Feature Matching WebApp")
st.markdown("**Developed by Vaibhav**", unsafe_allow_html=True)

# Function to perform ORB feature matching
def orb_feature_matching(query_img, train_img):
    # Convert images to grayscale
    query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and compute descriptors for query and train images
    query_keypoints, query_descriptors = orb.detectAndCompute(query_img_bw, None)
    train_keypoints, train_descriptors = orb.detectAndCompute(train_img_bw, None)

    # Initialize the BFMatcher
    matcher = cv2.BFMatcher()

    # Match descriptors
    matches = matcher.match(query_descriptors, train_descriptors)

    # Draw matches on the images
    matched_image = cv2.drawMatches(query_img, query_keypoints, train_img, train_keypoints, matches[:20], None)

    return matched_image

# File uploaders for query and train images
query_image = st.file_uploader("Upload Query Image", type=["jpg", "png", "jpeg"])
train_image = st.file_uploader("Upload Train Image", type=["jpg", "png", "jpeg"])

if query_image is not None and train_image is not None:
    # Read images
    query_img = cv2.imdecode(np.frombuffer(query_image.read(), np.uint8), cv2.IMREAD_COLOR)
    train_img = cv2.imdecode(np.frombuffer(train_image.read(), np.uint8), cv2.IMREAD_COLOR)

    st.image(query_img, caption="Query Image", use_column_width=True)
    st.image(train_img, caption="Train Image", use_column_width=True)

    # Perform ORB feature matching
    result_image = orb_feature_matching(query_img, train_img)
    
    st.image(result_image, caption="ORB Feature Matching Result", use_column_width=True)

# import streamlit as st
# import cv2
# import numpy as np

# st.title("ORB Feature Mapping WebApp")
# st.markdown("**Developed by Vaibhav**", unsafe_allow_html=True)

# # Function to apply ORB feature mapping
# def apply_orb(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Initialize ORB detector
#     orb = cv2.ORB_create()

#     # Find the keypoints with ORB
#     keypoints, descriptors = orb.detectAndCompute(gray, None)

#     # Draw the keypoints on the image
#     orb_image = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)

#     return orb_image

# image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# if image is not None:
#     image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
#     height, width = image.shape[:2]

#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Apply ORB feature mapping
#     orb_image = apply_orb(image)
#     st.image(orb_image, caption="ORB Feature Mapping", use_column_width=True)
