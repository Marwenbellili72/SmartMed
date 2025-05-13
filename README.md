# **SmartMed: AI-Powered Cardiac Care Platform**

## 🩺 Overview

**SmartMed** is an innovative platform developed at **École Supérieure des Communications de Tunis (SUP’COM)** during the academic year **2025–2026**. It combines **Artificial Intelligence (AI)**, **Internet of Things (IoT)**, and **web technologies** to improve cardiac care through:

* Medical image enhancement and segmentation
* Heart attack risk prediction
* Real-time online consultations

---

## 🧰 Technologies Used

### 🌐 Frontend

* **HTML5** – Web content structure
* **CSS3** – Styling for clean and ergonomic design
* **JavaScript** – Interactive functionalities (e.g., image zooming)
* **jQuery** – Simplified DOM manipulation and event handling

### 🛠️ Backend

* **Django** – Python framework for backend logic and database management

### 🤖 Machine Learning & AI

* **Totalsegmentator** – 3D heart structure segmentation from CT scans
* **Logistic Regression** – Heart attack risk prediction model
* **LoRA + Unsloth** – Fine-tuning large language models (LLMs)
* **Hugging Face** – Model hosting and access

### 📡 IoT

* **Arduino** – Acquisition of heart rate and body temperature
* **ThingSpeak** – IoT data storage and real-time visualization
* **ZEGOCLOUD API** – Real-time video consultation integration

### ⚙️ DevOps

* **Jenkins** – CI/CD automation
* **NGINX** – Web server and reverse proxy
* **Trivy** – Vulnerability scanning
* **SonarQube** – Static code analysis
* **Docker** – Application containerization
* **Prometheus & Grafana** – Performance monitoring and visualization

### 🔐 Security

* **Nmap & Wireshark** – Security assessment and network traffic analysis

---

## 🚀 Key Features

### 🔬 Medical Image Enhancement

* Enhanced CT scan contrast using **Histogram Equalization** and **CLAHE** (Contrast Limited Adaptive Histogram Equalization)

### 🫀 Heart Segmentation

* Automated segmentation of cardiac structures in 3D CT images via **Totalsegmentator**

### ❤️ Heart Attack Prediction

* Developed and evaluated multiple models
* **Logistic Regression** selected for its superior performance

### 🧑‍⚕️ Real-Time Online Consultations

* IoT-based health monitoring with **Arduino sensors**
* Data sent to **ThingSpeak** and integrated with **ZEGOCLOUD API** for live consultations

### 📊 CT Image Analysis with LLM

* Fine-tuned a **Large Language Model** (LLM) using **LoRA** and **Unsloth**
* Model hosted on **Hugging Face** and accessible through **Google Colab**
* Full deployment not completed due to resource complexity

### 🔁 CI/CD & Monitoring Pipeline

* Implemented automated CI/CD with:

  * **Jenkins**, **Docker**, **NGINX**, **SonarQube**, **Trivy**
  * Monitoring using **Prometheus** and **Grafana**

### 🔒 Security Testing

* Performed vulnerability scans and traffic analysis with **Nmap** and **Wireshark**

---

## 📈 Visualization Highlights

| Feature                 | Visualization Tool            | Description                                                  |
| ----------------------- | ----------------------------- | ------------------------------------------------------------ |
| CT Image Enhancement    | Web Interface                 | Contrast improvement using Histogram Equalization and CLAHE  |
| Heart Segmentation      | 3D Slicer                     | Visualization of segmented 3D heart structures               |
| Heart Attack Prediction | ROC Curves & Confusion Matrix | Model performance metrics                                    |
| IoT Data Monitoring     | ThingSpeak + Web Dashboard    | Live graphs of heart rate and temperature                    |
| LLM CT Analysis         | Google Colab                  | Textual medical insights generated from CT scans             |
| Pipeline & Metrics      | Jenkins + Grafana             | CI/CD status, performance metrics, and vulnerability reports |

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.8+
* Docker
* Arduino IDE
* ThingSpeak & ZEGOCLOUD accounts
* Hugging Face account

### 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/marwenbellili/smartmed.git
   cd smartmed
   ```

2. **Install backend dependencies**

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

3. **Set up IoT**

   * Connect the Arduino with heart rate and temperature sensors
   * Upload firmware via the Arduino IDE
   * Configure ThingSpeak API credentials

4. **Run the application**

   ```bash
   gunicorn --bind 0.0.0.0:8000 smartmed.wsgi
   ```

5. **Configure NGINX**

   * Serve static files
   * Reverse proxy for Gunicorn

---

## 🤖 Accessing the LLM

Use the **Google Colab notebook** provided in the repository to interact with the fine-tuned LLM hosted on **Hugging Face**.

---

## 📄 License

SmartMed is released under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact

For any inquiries or collaboration requests, contact:
**[marwen.bellili@supcom.tn](mailto:marwen.bellili@supcom.tn)**

---
