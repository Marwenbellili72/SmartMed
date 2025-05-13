# 🩺 SmartMed: AI-Powered Cardiac Care Platform

## 🧭 Overview

**SmartMed** est un projet développé à l’**École Supérieure des Communications de Tunis (SUP’COM)** durant l’année universitaire **2025–2026**. Il combine l’**intelligence artificielle**, l’**IoT**, et les **technologies web** pour offrir une plateforme avancée d’aide au diagnostic et à la prévention des maladies cardiaques.

Le système propose :

* L’**amélioration d’images médicales** (CT),
* La **segmentation du cœur** en 3D,
* La **prédiction des risques d’infarctus**,
* Des **consultations médicales en ligne** en temps réel.

---

## ⚙️ Technologies Utilisées

### 🌐 Frontend

* **HTML5** : Structure du contenu web
* **CSS3** : Mise en forme pour une interface ergonomique
* **JavaScript** : Fonctionnalités interactives (zoom sur les images, etc.)
* **jQuery** : Simplifie la manipulation du DOM et la gestion des événements

### 🖥️ Backend

* **Django** : Framework Python pour la logique serveur et la gestion des données

### 🧠 Machine Learning & AI

* **TotalSegmentator** : Segmentation 3D des structures cardiaques
* **Logistic Regression** : Prédiction du risque d’infarctus
* **LoRA + Unsloth** : Fine-tuning de LLMs
* **Hugging Face** : Hébergement et partage des modèles

### 📡 IoT

* **Arduino** : Acquisition de signes vitaux (température, fréquence cardiaque)
* **ThingSpeak** : Visualisation des données IoT en temps réel
* **ZEGOCLOUD API** : Consultations médicales en ligne en direct

### 🛠️ DevOps

* **Jenkins** : Intégration et déploiement continu (CI/CD)
* **NGINX** : Reverse proxy & gestion des fichiers statiques
* **Docker** : Conteneurisation des services
* **Trivy** : Analyse des vulnérabilités
* **SonarQube** : Analyse de qualité du code
* **Prometheus & Grafana** : Surveillance des performances

### 🔐 Sécurité

* **Nmap & Wireshark** : Tests de sécurité réseau

---

## 🏥 Principales Fonctionnalités

### 📈 Medical Image Enhancement

Nous avons appliqué deux techniques principales pour **améliorer la qualité des images CT** :

* **Égalisation d’histogramme** : améliore la **luminosité et le contraste** globaux.
* **CLAHE (Contrast Limited Adaptive Histogram Equalization)** : améliore le **contraste local** tout en **préservant les détails** sans créer d'artefacts.

> Bien que l’amélioration soit notable, elle n’est pas parfaite. Des artefacts peuvent apparaître selon les paramètres, mais la lisibilité globale est significativement améliorée.

* 🖼️ **Figure 1.6** : montre l’amélioration du contraste après égalisation d’histogramme.
* 🖼️ **Figure 1.7** : illustre les résultats de la transformation CLAHE avec un histogramme mieux réparti dans les zones sombres.

Ces méthodes offrent un **bon compromis** entre amélioration du contraste et conservation des détails.

---

### 🫀 Heart Segmentation

Nous avons utilisé l’**API de TotalSegmentator** pour réaliser la **segmentation 3D** des images CT du cœur. Pour **accélérer le traitement**, nous avons choisi le **mode `fast`**, qui sacrifie légèrement la précision au profit du temps d’exécution.

> ✅ Les résultats sont satisfaisants pour la visualisation et l’analyse des **structures internes** du cœur malgré une **précision moindre**.

Les sorties sont visualisées avec **3D Slicer**, facilitant ainsi l’étude anatomique du cœur.

---

### ❤️‍🔥 Heart Attack Prediction

Nous avons testé plusieurs algorithmes de machine learning. Le **modèle de régression logistique** a été retenu pour sa **meilleure performance**.

* 📊 Les résultats incluent : **matrices de confusion** et **courbes ROC**.
* 🎯 Le modèle classe les patients selon leur **risque d’infarctus** à partir de leurs données cliniques.

---

### 🔴 Online Consultations via IoT

* 🩺 Les signes vitaux sont capturés via **Arduino** (fréquence cardiaque, température).
* 📡 Les données sont envoyées à **ThingSpeak** pour visualisation en temps réel.
* 👨‍⚕️ Grâce à l’**API ZEGOCLOUD**, nous permettons des **consultations en ligne interactives** avec visualisation des mesures.

---

### 🧠 LLM for CT Image Analysis

Nous avons fine-tuné un **LLM (Large Language Model)** avec **LoRA** via **Unsloth**, pour l’analyse sémantique des images CT.

* 📁 Le modèle est hébergé sur **Hugging Face**.
* 💻 Il est accessible depuis un **notebook Google Colab**.
* ❗ Déploiement complet non réalisé à cause de la complexité des ressources nécessaires.

---

### 🔁 CI/CD Pipeline

Mise en place d’un pipeline DevOps automatisé :

* **Jenkins** : automatisation des tests et déploiements
* **SonarQube + Trivy** : contrôle qualité et sécurité du code
* **Docker + NGINX** : déploiement conteneurisé
* **Grafana + Prometheus** : surveillance des performances

---

### 🔒 Security Testing

Nous avons effectué des **tests de sécurité réseau** avec :

* **Nmap** : scan des ports et services exposés
* **Wireshark** : analyse du trafic réseau pour détecter des vulnérabilités

---

## 📊 Visualisation des Résultats

| Résultat                           | Outil utilisé                 | Détails                       |
| ---------------------------------- | ----------------------------- | ----------------------------- |
| **CT Image Enhancement**           | Web UI                        | Résultats CLAHE + égalisation |
| **Segmentation 3D du cœur**        | 3D Slicer                     | Affichage interactif          |
| **Prédiction d’infarctus**         | Django + Matplotlib           | ROC, confusion matrix         |
| **Données IoT (température, BPM)** | ThingSpeak + Web dashboard    | Graphes temps réel            |
| **Analyse LLM**                    | Google Colab + Hugging Face   | Résumés textuels              |
| **Monitoring & Sécurité**          | Grafana, Trivy, Jenkins, Nmap | Dashboards + rapports         |

---

## 🧰 Setup Instructions

### ✅ Prérequis

* Python 3.8+
* Docker
* Arduino IDE
* Comptes ThingSpeak, Hugging Face, ZEGOCLOUD

### 🚀 Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/marwenbellili/smartmed.git
cd smartmed

# 2. Installer les dépendances
pip install -r requirements.txt
python manage.py migrate

# 3. Lancer l’application
gunicorn --bind 0.0.0.0:8000 smartmed.wsgi
```

Configurer **NGINX** pour les fichiers statiques et le reverse proxy.

---

### 🔌 Mise en place IoT

1. Connecter les capteurs (fréquence cardiaque, température) à l’Arduino.
2. Uploader le code via **Arduino IDE**.
3. Configurer les clés API ThingSpeak.

---

### 🤖 Accès au LLM

* Le **notebook Colab** est disponible pour tester le modèle fine-tuné.
* Le modèle est hébergé sur **Hugging Face** : [lien dans le dépôt](https://huggingface.co).

---

## 📄 License

Projet sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.

---

## 📬 Contact

Développé par **Marwen Bellili**
📧 [marwen.bellili@supcom.tn](mailto:marwen.bellili@supcom.tn)
🔗 GitHub : [marwenbellili](https://github.com/marwenbellili)

---
