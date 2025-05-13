# SmartMed: AI-Powered Cardiac Health Platform ❤️🧠💻
SmartMed is an ambitious academic project aimed at revolutionizing cardiac healthcare through the integration of advanced web technologies, Artificial Intelligence (AI), Machine Learning (ML), Internet of Things (IoT), and robust DevOps practices. The platform focuses on enhancing medical image analysis, predicting cardiac events, optimizing CT imaging protocols, providing secure online consultations, and leveraging Large Language Models (LLMs) for medical diagnosis.

---

## 📚 Table of Contents

*   [Project Vision](#project-vision)
*   [Key Features](#key-features)
*   [Modules / Reports Overview](#modules--reports-overview)
*   [Core Technologies Used](#core-technologies-used)
*   [System Architecture Highlights](#system-architecture-highlights)
*   [Screenshots & Visualizations](#screenshots--visualizations)

---

## 🎯 Project Vision

The core vision of SmartMed is to create an integrated, intelligent, and secure platform that:
1.  Improves the accuracy and efficiency of cardiac diagnostics.
2.  Facilitates remote patient monitoring and online consultations.
3.  Optimizes medical imaging procedures to enhance quality while minimizing patient risks.
4.  Provides robust security for sensitive medical data and platform interactions.
5.  Leverages cutting-edge AI, including LLMs and deep learning, for predictive analytics and diagnostic support.

---

## ✨ Key Features

*   **Comprehensive Web Platform:** User-friendly interface for medical professionals and patients.
*   **AI-Powered Image Analysis:**
    *   CT Image Enhancement & Segmentation (heart, vessels).
    *   LLM-driven analysis of CT images for anomalies.
*   **Predictive Modeling:** Machine learning models for predicting cardiac crises.
*   **CT Protocol Optimization:** Techniques to optimize CT image quality while minimizing X-ray radiation dose (e.g., using NSGA-II).
*   **IoT for Remote Monitoring:** Real-time monitoring of vital signs (heart rate, temperature) via Arduino-based IoT devices, with data visualization on ThingSpeak and the web platform.
*   **Secure Online Consultation:** ZEGOCLOUD API integration for real-time video consultations alongside live vital signs display.
*   **Robust Security Framework:**
    *   Security testing using Nmap and Wireshark.
    *   Implementation of SSL/TLS, Web Application Firewalls (WAF), and Reinforcement Learning for cybersecurity.
*   **Efficient CI/CD Pipeline:** Automated build, test, and deployment using Docker, Jenkins, SonarQube, Trivy, and Kubernetes.
*   **Detailed Cardiac Anatomy & Function Module:** Educational resource integrated into the platform.

---

## 📄 Modules / Reports Overview

This project is composed of several detailed reports, each focusing on a critical aspect of the SmartMed platform:

1.  **Technologies Web Utilisées et Objectifs de Projet:**
    *   Outlines the web technologies (HTML5, CSS, JS, jQuery, Django) employed.
    *   Defines overarching project goals: medical image improvement, heart segmentation, cardiac event prediction, online consultation, and CT quality optimization.

2.  **Optimisation des Protocoles d’Imagerie CT:**
    *   Explains CT scanner principles and Radon Transform.
    *   Details mathematical and metaheuristic optimization techniques (Gradient Descent, Genetic Algorithms, PSO, NSGA-II).
    *   Applies NSGA-II to optimize CT image quality vs. radiation dose using equations for dose and quality based on mA, time, and rpm.

3.  **Test de Sécurité et Solutions pour l’Améliorer:**
    *   Covers security testing with Nmap (port scanning, OS detection) and Wireshark (packet analysis).
    *   Proposes security solutions: SSL/TLS certificates, Web Application Firewalls (WAF), and Reinforcement Learning for intrusion detection and DDoS protection.

4.  **Fonction et Anatomie du Cœur:**
    *   Provides a detailed description of the heart's function, anatomy (walls, chambers, valves, blood vessels, coronary arteries), and electrical conduction system.
    *   Discusses common cardiac conditions, symptoms, diagnostic tests, and care.

5.  **Modèle de Prédiction des Crises Cardiaques à l’Aide de l’Apprentissage Automatique:**
    *   Explores supervised learning (regression, classification).
    *   Details various classification algorithms (Logistic Regression, SVM, KNN, Decision Trees, Random Forest, AdaBoost, Gradient Boosting, Naive Bayes, LDA).
    *   Covers model evaluation metrics (Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC AUC).
    *   Applies these models to a Kaggle heart attack dataset, including data description, EDA, and classifier performance comparison.

6.  **Solution IoT pour la Consultation en Ligne en Santé:**
    *   Describes the IoT approach for real-time vital signs monitoring (heart rate, temperature).
    *   Details components: Arduino, ESP8266, heartbeat sensor, LM35 temperature sensor.
    *   Covers Arduino IDE, virtual serial port creation, data visualization, and sending data to ThingSpeak.
    *   Integration with the web platform for online consultation (potentially using ZEGOCLOUD).

7.  **Mise en Place d’un Pipeline CI/CD:**
    *   Introduces DevOps principles and tools: Docker, Jenkins, SonarQube, Trivy, Grafana, Prometheus, Kubernetes, Ansible, Terraform.
    *   Explains web server technologies: NGINX (load balancing, reverse proxy, caching) and WSGI servers (uWSGI, Gunicorn).
    *   Details the project's CI/CD architecture: GitHub -> Jenkins (SonarQube, Trivy, Docker build/push) -> Docker Hub, with monitoring via Prometheus & Grafana.

8.  **LLM pour le Diagnostic Médical:**
    *   Traces the evolution of NLP models from RNNs/LSTMs to Transformers (BERT, GPT, T5).
    *   Discusses the application of LLAMA models, PEFT (LoRA, QLoRA), Unsloth, and Hugging Face.
    *   Details a training pipeline: loading the "Radiology Mini" dataset, Llama-3.2-11B-Vision-Instruct model, LoRA adaptation, dataset transformation, training, and uploading to Hugging Face for testing with CT images.

9.  **Amélioration et Segmentation des Images CT:**
    *   Covers digital image processing basics: intensity transformations (negation, log, power-law) and histogram equalization (including CLAHE).
    *   Explores image segmentation: importance, types (semantic, instance, panoptic), key concepts.
    *   Details traditional methods (thresholding, edge-based, region-based, clustering) and deep learning models (U-Net, SegNet, Mask R-CNN, DeepLab, Vision Transformers).
    *   Discusses evaluation metrics (IoU, Dice).
    *   Applies Totalsegmentator (based on nnUNET) for 3D heart segmentation from CT/MRI scans, visualized with 3D Slicer.

---

## 🛠️ Core Technologies Used

*   **Frontend:** HTML5, CSS3, JavaScript, jQuery
*   **Backend:** Python, Django
*   **Database:** SQLite (as per Django default, could be others)
*   **AI/ML:** Scikit-learn, TensorFlow/Keras/PyTorch (implied for deep learning models)
    *   *Algorithms:* Logistic Regression, SVM, KNN, Decision Trees, Random Forest, AdaBoost, Gradient Boosting, Naive Bayes, LDA, NSGA-II.
*   **IoT:**
    *   *Hardware:* Arduino, ESP8266, Pulse Sensor, LM35 Temperature Sensor.
    *   *Software/Platform:* Arduino IDE, ThingSpeak.
*   **DevOps & CI/CD:**
    *   *Containerization:* Docker, Docker Compose.
    *   *Orchestration:* Kubernetes (mentioned as a DevOps tool).
    *   *CI/CD Server:* Jenkins.
    *   *Code Quality & Security:* SonarQube, Trivy.
    *   *Monitoring:* Prometheus, Grafana.
    *   *IaC:* Ansible, Terraform (mentioned as DevOps tools).
    *   *Web Server/Gateway:* NGINX, uWSGI, Gunicorn.
*   **LLM & NLP:**
    *   *Models:* LLAMA, BERT, GPT, T5, Vision Transformers.
    *   *Frameworks/Libraries:* Hugging Face Transformers, PEFT (LoRA, QLoRA), Unsloth.
*   **Image Processing & Segmentation:**
    *   *Libraries:* OpenCV, Scikit-image (likely), ITK/SimpleITK (for medical images).
    *   *Tools:* Totalsegmentator, nnUNET, 3D Slicer.
*   **Security:** Nmap, Wireshark, OpenSSL (for SSL/TLS).
*   **Cloud & APIs:** ZEGOCLOUD (for video consultation), Docker Hub.

---

## 🏗️ System Architecture Highlights

The SmartMed platform integrates several key architectural components:

1.  **Web Application:** A Django-based backend serves a dynamic frontend. NGINX acts as a reverse proxy, load balancer, and serves static files. uWSGI/Gunicorn handles application serving.
2.  **IoT Subsystem:** Arduino devices collect sensor data, which is transmitted (likely via ESP8266 Wi-Fi module) to ThingSpeak for cloud storage/visualization and also directly to the web platform for real-time display during consultations.
3.  **AI/ML Services:**
    *   **Prediction Models:** Trained models (e.g., for heart attack risk) are integrated into the backend to provide predictions based on patient data.
    *   **Image Analysis:** Segmentation and enhancement algorithms (traditional and deep learning-based like nnUNET/Totalsegmentator) process uploaded medical images.
    *   **LLM Diagnostics:** Fine-tuned LLAMA models analyze medical reports and images, providing diagnostic insights.
4.  **CI/CD Pipeline:**
    *   **Source Control:** Code hosted on GitHub.
    *   **Automation Server:** Jenkins orchestrates the pipeline.
    *   **Build & Test:** Jenkins pulls code, runs SonarQube for static analysis, builds Docker images.
    *   **Security Scan:** Trivy scans Docker images for vulnerabilities.
    *   **Deployment:** Images are pushed to Docker Hub. Deployment to staging/production environments (potentially managed by Kubernetes).
    *   **Monitoring:** Prometheus collects metrics from Jenkins and other services, visualized in Grafana dashboards.
5.  **Security Layer:** SSL/TLS for encrypted communication, WAF for application-level threat protection, and proactive security monitoring.

*(Refer to the "Mise en Place d’un Pipeline CI/CD" report for a visual representation of the CI/CD architecture).*

---

## 🖼️ Screenshots & Visualizations

The project reports contain numerous figures and visualizations, including:
*   Logos of technologies (HTML5, CSS, JS, jQuery, Django).
*   Diagrams of optimization algorithms (Gradient Descent, GA, PSO).
*   NSGA-II optimization results for CT protocols.
*   Nmap and Wireshark security test outputs.
*   SSL/TLS workflow, WAF architecture.
*   Heart anatomy diagrams.
*   ML model concepts, dataset visualizations, ROC curves, and classifier performance tables.
*   IoT device schematics, Arduino IDE, ThingSpeak charts.
*   CI/CD pipeline diagrams, Jenkins, SonarQube, Trivy, Grafana dashboards.
*   LLM architectures (RNN, LSTM, Transformer, BERT, GPT, Llama), Unsloth and Hugging Face UI.
*   Image processing examples (negation, CLAHE), segmentation results from Totalsegmentator/3D Slicer.

These visuals are crucial for understanding the implementation and results of each module.

---
