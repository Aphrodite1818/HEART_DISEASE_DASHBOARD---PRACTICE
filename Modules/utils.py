import os
import pandas as pd
import streamlit as st

#-------------------THIS MODULE STORES THE DATASET REQUIRED BY THE APP --------------#
# YOU CAN CHANGE THE FILE PATH HERE
# NB WHEN YOU CHANGE THE FILE MAKE SURE IT MATCHES THE STRUCTURE THE WEB APP WAS BUILT WITH


@st.cache_data
def load_data():
    script_dir = os.path.dirname(__file__)  # Modules/
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # WHEN CHANGING THE FILE STORE THE DATASET INTO THE DATA PREPROCESSING AND EXPLORATION FOLDER 
    # AND CHANGE "heart_disease_dataset_with_countries_states.csv" TO YOUR_FILE
    csv_path = os.path.join(project_root, "Data preprocessing and exploration", 
                            "heart_disease_dataset_with_countries_states.csv")
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found! Looked here: {os.path.abspath(csv_path)}")

    df = pd.read_csv(csv_path)
    return df


# Shared dataframe for the app
heart_df = load_data()


def load_page_impage():
    script_dir = os.path.dirname(__file__)  # Modules/
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # WHEN CHANGING THE FILE STORE THE IMAGE INTO THE images/ FOLDER 
    # AND CHANGE "page icon image.jpeg" TO YOUR_IMAGE_FILE
    page_image_path = os.path.join(project_root, "images", "page icon image.jpeg")
    
    if not os.path.exists(page_image_path):
        raise FileNotFoundError(f"PAGE IMAGE NOT FOUND: {os.path.abspath(page_image_path)}")

    page_image = page_image_path
    return page_image


def load_sidebar_image_icon():
    script_dir = os.path.dirname(__file__)  # Modules/
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # WHEN CHANGING THE FILE STORE THE IMAGE INTO THE images/ FOLDER 
    # AND CHANGE "sidebar icon image.png" TO YOUR_IMAGE_FILE
    sidebar_icon_image_path = os.path.join(project_root, "images", "sidebar icon image.png")
    
    if not os.path.exists(sidebar_icon_image_path):
        raise FileNotFoundError(f"SIDEBAR ICON IMAGE NOT FOUND: {os.path.abspath(sidebar_icon_image_path)}")

    sidebar_icon_image = sidebar_icon_image_path
    return sidebar_icon_image


if __name__ == "__main__":
    # TESTING: PRINT FIRST 5 ROWS OF DATA AND PATHS OF IMAGES
    print("First 5 rows of dataset:")
    print(heart_df.head())
    print("Page icon path:", load_page_impage())
    print("Sidebar icon path:", load_sidebar_image_icon())
