import streamlit as st
from PIL import Image
import numpy as np
import os, sys
import json

# add src folder to path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'src')))

# caching utilities
@st.cache_resource
def load_model(path='model.h5'):
    import tensorflow as tf
    return tf.keras.models.load_model(path)

@st.cache_data
def load_class_map(path='class_indices.json'):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception:
        return {}

# helper for prediction
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from src.advisory import get_advice
from src.grad_cam import make_gradcam_heatmap, overlay_heatmap


def predict(image:
    Image.Image):
    img = image.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    model = load_model()
    preds = model.predict(img_array)
    class_idx = np.argmax(preds[0])
    confidence = preds[0][class_idx]
    cmap = load_class_map()
    inv_map = {v: k for k, v in cmap.items()}
    pred_class = inv_map.get(class_idx, str(class_idx))
    return pred_class, confidence, model, img_array


def display_results(image, pred_class, confidence, model, img_array):
    st.write(f"**Prediction:** {pred_class}")
    st.write(f"**Confidence:** {confidence:.2f}")
    advice = get_advice(pred_class)
    if advice:
        st.markdown("**Recommended action:**")
        for key, val in advice.items():
            st.write(f"- **{key.capitalize()}:** {val}")
    # grad-cam
    last_conv = 'conv5_block3_out'
    heatmap = make_gradcam_heatmap(img_array, model, last_conv)
    img_orig = np.array(image.resize((224,224)))
    overlayed = overlay_heatmap(img_orig, heatmap)
    st.image(heatmap, caption='Grad-CAM heatmap', use_column_width=True)
    st.image(overlayed, caption='Overlay', use_column_width=True)


def run_home():
    st.title("Multi-Crop Leaf Disease Detection")
    st.write("Upload a leaf image and the model will predict the disease and provide advice.")
    # option to pick sample from prepared dataset
    image = None
    if st.sidebar.checkbox('Use sample image'):
        sample_dir = os.path.join('dataset', 'processed', 'test')
        samples = []
        if os.path.isdir(sample_dir):
            for cls in os.listdir(sample_dir):
                cls_dir = os.path.join(sample_dir, cls)
                if os.path.isdir(cls_dir):
                    imgs = os.listdir(cls_dir)
                    if imgs:
                        samples.append(os.path.join(cls_dir, imgs[0]))
        choice = st.sidebar.selectbox('Sample images', samples)
        if choice:
            image = Image.open(choice)
    if image is None:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
    if image is not None:
        st.image(image, caption='Selected Image', use_column_width=True)
        try:
            pred_class, confidence, model, img_array = predict(image)
            display_results(image, pred_class, confidence, model, img_array)
        except Exception as e:
            st.error(f"Prediction failed: {e}")

    # model download
    if os.path.exists('model.h5'):
        with open('model.h5', 'rb') as f:
            st.sidebar.download_button('Download trained model', f, file_name='model.h5')


def run_about():
    st.title("About the Project")
    st.markdown(
        "This application detects diseases on potato, corn, and grape leaves using a ResNet50 model trained on the PlantVillage dataset. "
        "It also provides Grad-CAM visualizations and agricultural advice for the predicted disease."
    )
    st.markdown("#### Dataset classes:")
    classes = [
        'Potato Early blight', 'Potato Late blight', 'Potato healthy',
        'Corn Gray leaf spot', 'Corn Common rust', 'Corn Northern Leaf Blight', 'Corn healthy',
        'Grape Black rot', 'Grape Esca', 'Grape Leaf blight', 'Grape healthy'
    ]
    for c in classes:
        st.write(f"- {c}")
    st.markdown("#### Instructions")
    st.write("1. Prepare dataset with dataset/prepare.py")
    st.write("2. Train model using src/train.py or VS Code task")
    st.write("3. Use this interface to upload images and see predictions.")


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "About"])
    if page == "Home":
        run_home()
    elif page == "About":
        run_about()

if __name__ == '__main__':
    main()
