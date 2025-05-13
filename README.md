SmartMed: AI-Powered Cardiac Care Platform
Overview
SmartMed is a project developed at École Supérieure des Communications de Tunis (SUP’COM) in 2025-2026. It leverages AI, IoT, and web technologies to enhance cardiac care through medical image analysis, heart attack prediction, and online consultations.
Technologies Used
Frontend

HTML5: Structures web content.
CSS3: Styles the interface for clarity and ergonomics.
JavaScript: Enables interactive features like image zooming.
jQuery: Simplifies DOM manipulation and event handling.

Backend

Django: Python framework for secure server-side logic and data management.

Machine Learning and AI

Totalsegmentator: For heart segmentation.
Logistic Regression: For heart attack prediction.
LoRA and Unsloth: For fine-tuning LLMs.
Hugging Face: For model storage and access.

IoT

Arduino: Captures vital signs.
ThingSpeak: Stores and visualizes IoT data.
ZEGOCLOUD API: Enables real-time consultations.

DevOps

Jenkins: Automates CI/CD pipelines.
NGINX: Serves static files and acts as a reverse proxy.
Trivy: Scans for vulnerabilities.
SonarQube: Analyzes code quality.
Docker: Containerizes applications.
Prometheus and Grafana: Monitor performance.

Security

Nmap and Wireshark: For security testing.

Main Features

Medical Image EnhancementWe used histogram equalization and CLAHE to enhance CT image contrast and visibility.

Heart SegmentationWe employed Totalsegmentator to automatically segment heart structures in 3D CT images.

Heart Attack PredictionWe trained multiple models and selected Logistic Regression as the most performant for predicting heart attack risks.

Online ConsultationsWe developed an IoT solution using Arduino to capture heart rate and temperature, sent data to ThingSpeak, and integrated the ZEGOCLOUD API for real-time consultations.

LLM for CT Image AnalysisWe fine-tuned a Large Language Model (LLM) with LoRA using Unsloth to analyze CT images. The model was uploaded to Hugging Face and can be accessed via a Google Colab notebook. Full deployment was not completed due to complexity.

CI/CD PipelineWe implemented a CI/CD pipeline using Jenkins, NGINX, Trivy, SonarQube, Docker, Prometheus, and Grafana for automated code analysis, security scanning, and deployment.

Security TestingWe conducted tests using Nmap and Wireshark to identify and mitigate vulnerabilities.


Visualization of Results

CT Image Enhancement: Visualized improved contrast using histogram equalization and CLAHE, displayed on the web interface.
Heart Segmentation: 3D heart structures segmented by Totalsegmentator, visualized using 3D Slicer.
Heart Attack Prediction: Logistic Regression model performance shown via ROC curves and confusion matrices.
IoT Data: Heart rate and temperature data plotted in real-time on ThingSpeak and integrated into the web platform.
LLM Outputs: CT image analysis results displayed as textual descriptions in the Colab notebook.
Pipeline Monitoring: Jenkins pipeline status and code quality metrics visualized on Grafana dashboards, with vulnerability reports from Trivy.

Setup Instructions
Prerequisites

Python 3.8+
Docker
Arduino IDE
ThingSpeak and ZEGOCLOUD accounts
Hugging Face account

Installation

Clone the repository:git clone https://github.com/marwenbellili/smartmed.git
cd smartmed


Install backend dependencies:pip install -r requirements.txt
python manage.py migrate


Set up IoT:
Connect Arduino with heartbeat and temperature sensors.
Upload code via Arduino IDE.
Configure ThingSpeak API.


Run the application:gunicorn --bind 0.0.0.0:8000 smartmed.wsgi

Configure NGINX for static files and proxy.

Accessing the LLM

Use the Google Colab notebook to interact with the fine-tuned LLM on Hugging Face.

License
MIT License. See LICENSE file.
Contact
marwen.bellili@supcom.tn
