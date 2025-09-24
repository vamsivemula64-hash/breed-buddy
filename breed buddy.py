import streamlit as st
from PIL import Image
import torch
import os

# --------------------------
# LOGIN SECTION
# --------------------------
def login():
    st.title("🔐 Login - Breed Recognition")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "breed" and password == "25004":
            st.session_state["logged_in"] = True
            st.success("✅ Login successful!")
        else:
            st.error("❌ Incorrect username or password.")

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Show login page
if not st.session_state["logged_in"]:
    login()
    st.stop()

# --------------------------
# MODEL LOADING
# --------------------------
@st.cache_resource
def load_model():
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", trust_repo=True)  # use yolov5s
    return model

model = load_model()

# --------------------------
# MAIN APP UI
# --------------------------
st.title("🐄 Breed Recognition of Cattles and Buffaloes")
st.markdown("Upload an image and select dataset to detect cattle or buffalo breeds.")

# Dataset option
dataset_options = ["Select Dataset", "Cattle Breeds", "Buffalo Breeds", "Mixed"]
selected_dataset = st.selectbox("📂 Choose Dataset", dataset_options)

# File uploader
uploaded_file = st.file_uploader("📁 Upload an Image...", type=["jpg", "jpeg", "png", "mp4"])

if selected_dataset == "Select Dataset":
    st.warning("⚠️ Please select a dataset to continue.")
    st.
