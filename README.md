

# Heart Disease Dashboard

## **Overview**

The Heart Disease Dashboard is an **interactive Streamlit application** that allows users to explore heart disease data across countries and states. It provides insights through **KPIs, charts, and maps**, and is designed to be **modular, maintainable, and easy to extend**.

---

## **Features**

* Explore heart disease prevalence by **country, state, age, and gender**.
* Interactive **bar charts, line charts, and maps**.
* Dynamic **KPIs and column layouts** for quick insights.
* Modular structure for **easy updates and scalability**.
* Works **locally and on Streamlit Cloud** with relative paths.

---

## **Project Structure**

```
HeartDiseaseDashboard/
│
├─ Modules/                             <- all Python scripts
│   ├─ __init__.py                      <- makes Modules a package
│   ├─ app.py                           <- main Streamlit app
│   ├─ utils.py                         <- shared functions, data loading
│   ├─ sidebar.py                        <- sidebar elements
│   ├─ queries.py                        <- query/filter functions
│   ├─ columns.py                        <- KPI/column layout functions
│   ├─ plots.py                          <- charting functions
│   ├─ map.py                            <- map plotting functions
│   └─ kpi.py                            <- KPI calculation functions
│
├─ data preprocessing and exploration/   <- datasets + notebook
│   ├─ raw_merged_heart_dataset.csv
│   ├─ heart_dataset_with_countries_states.csv
│   └─ preprocessing.ipynb
│
├─ images/                              <- dashboard images
│   ├─ page_image.png
│   └─ sidebar_image.png
│
├─ .gitignore                           <- ignore venv, pycache, etc.
├─ requirements.txt                      <- Python dependencies
└─ README.md                             <- this file
```

---

## **Installation & Setup (Local)**

1. **Clone the repository**

```bash
git clone https://github.com/Aphrodite1818/HEART_DISEASE_DASHBOARD---PRACTICE.git
cd Folder_Name
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run Modules/app.py
```

---

## **Quick Deploy on Streamlit Cloud**

1. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in.
2. Click **“New App” → Select GitHub repository**.
3. Choose the branch (usually `main`) and **start file:** `Modules/app.py`.
4. Click **Deploy**. Streamlit Cloud installs dependencies from `requirements.txt` and launches the app.

> All CSV and image paths use **relative paths** from the repo root, ensuring compatibility locally and on Streamlit Cloud.

---

## **Data**

* **Raw Dataset:** `data preprocessing and exploration/raw_merged_heart_dataset.csv`
* **Cleaned Dataset:** `data preprocessing and exploration/heart_dataset_with_countries_states.csv`
* Preprocessing steps are in `preprocessing.ipynb`.

---

## **Images**

* `images/page_image.png` → main dashboard banner
* `images/sidebar_image.png` → sidebar visual

**Example in Streamlit:**

```python
import streamlit as st
import os

st.image(os.path.join("images", "page_image.png"))
st.sidebar.image(os.path.join("images", "sidebar_image.png"))
```

---

## **Code Organization**

* **Modules/utils.py:** Data loading and shared functions
* **Modules/sidebar.py:** Sidebar filters and widgets
* **Modules/queries.py:** Query/filter functions
* **Modules/columns.py:** KPI and column layouts
* **Modules/plots.py:** Charting functions
* **Modules/map.py:** Map visualizations
* **Modules/kpi.py:** KPI calculations
* **Modules/app.py:** Main Streamlit app connecting all modules

**CSV loading example (`utils.py`)**:

```python
import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    csv_path = os.path.join("data preprocessing and exploration", "heart_dataset_with_countries_states.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {os.path.abspath(csv_path)}")
    return pd.read_csv(csv_path)

heart_df = load_data()
```

---

## **Usage**

* Use the **sidebar filters** to select country, state, gender, or age range.
* Charts, maps, and KPIs update dynamically.
* Explore the dataset and preprocessing notebook for deeper analysis.
---

## **License**

This project is licensed under the **MIT License**
