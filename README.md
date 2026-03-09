# Multi-Crop Leaf Disease Detection with Explainable AI and AI-Based Advisory System

This repository contains all code, data preprocessing scripts, models, and a Streamlit application for a deep learning system that automatically detects plant diseases from leaf images and provides crop-specific advisory information. The system supports multiple crops and uses explainable AI techniques (Grad-CAM).

## Project Structure

- `dataset/` - dataset organization and preprocessing scripts
- `src/` - training, evaluation, and utility code
- `streamlit_app/` - Streamlit web interface code
- `notebooks/` - exploratory notebooks and visualizations

## Getting Started

1. Create a Python virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Prepare the PlantVillage dataset following the scripts in `dataset/`:
   ```bash
   python dataset/prepare.py
   ```
4. Train the model using the provided task or script:
   ```bash
   # via VS Code task
   # - Run "Train Model" from the command palette
   # via command line
   python src/train.py
   ```
   The model file `model.h5` and `class_indices.json` will be saved to the project root.
5. Evaluate the model using `src/evaluate.py` (modify as needed).
6. Run the Streamlit app:
   ```bash
   # via VS Code task: "Run Streamlit App"
   streamlit run streamlit_app/app.py
   ```
   
   **Features of the web interface:**
   - Upload your own leaf image or select a sample from the prepared test set (use the sidebar checkbox).
   - View the predicted crop and disease along with confidence score.
   - See Grad-CAM heatmap highlighting the image regions influencing the decision.
   - Get agricultural advice including description, symptoms, treatment and prevention for the detected disease.
   - Download the trained model file from the sidebar.
   - Navigate between the Home and About pages for project information.

## Requirements

See `requirements.txt` for all Python packages used.

## License

(Provide license information here)
