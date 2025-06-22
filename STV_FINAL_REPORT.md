# 🧠🤖🗑Smart Trash Vision (STV)	

**Date:** 2025-06-02

**Author:** SEOYOUNGWOO, HANSUSEONG

**Github:** repository link

**Demo Video:** Youtube link

------



## 1. Introduction

Proper waste sorting is essential for resource circulation and environmental protection. However, incorrect or careless recycling practices often reduce the efficiency of waste management systems. In particular, **contaminated items** (e.g., food-stained containers) are often disqua	lified from recycling.

This project aims to develop an **AI-based image classification system** that can automatically detect both the **type of waste** and whether it is **clean or contaminated**, thereby enhancing the accuracy and efficiency of waste sorting.

---

## 2. Problem Statement

- ## Project Objectives

  - To improve recycling efficiency through automated image-based waste classification.
  - To reduce reliance on human labor in waste sorting on campus.

- ## Expected Outcome and Evaluation

  - **Improved Sorting Accuracy**: Demonstrated classification of delivery containers and recyclables into at least 3 categories (e.g., clean plastic, contaminated, general waste) with over 85% accuracy.
  - **Labor Reduction**: Reduced manual intervention during sorting by at least 50% during test runs.
  - **Scalability**: Prototype can be deployed in dormitories, cafeterias, and student lounges with minimal supervision.

---

## 3. System Architecture

### 3.1 Hardware Components

| Component    | Role                                            |
| ------------ | ----------------------------------------------- |
| Web-Cam      | Detecting the Trash                             |
| LED Lighting | Ensures consistent image quality during capture |
| LCD Display  | Visualizes classification results               |

### 3.2 Software Stack

| Component        |          |
| ---------------- | -------- |
| Programming      | Python   |
| Image Processing | OpenCV   |
| Labeling Tools   | Roboflow |

---

## 4. Waste Categories & Classification Strategy

### 4.1 Target Waste Items

- Plastic containers
- Food trays
- Chopsticks
- Disposable plates
- Spoons
- Paper cups
- Plastic wraps (Vinyl)
- Receipts
- Beverage bottles (PET/Can)

### 4.2 Two-Stage Classification

| Stage       | Description                                        |
| ----------- | -------------------------------------------------- |
| **Stage 1** | Classify the waste item (9 categories)             |
| **Stage 2** | Determine if the item is *clean* or *contaminated* |

> 🔁 Total classes: up to 18 or use two separate models in sequence.

---

## 5. Dataset

### 5.1 Public Datasets

| Dataset       | Description                          | Link                                                     |
| ------------- | ------------------------------------ | -------------------------------------------------------- |
| TACO          | Real-world annotated trash           | [tacodataset.org](https://tacodataset.org)               |
| TrashNet      | 6-class trash classification dataset | [TrashNet GitHub](https://github.com/garythung/trashnet) |
| OpenLitterMap | Crowdsourced litter images           | [openlittermap.com](https://openlittermap.com)           |

### 5.2 Custom Data Collection Needed each 150 pictures

- Plastic containers
- Food trays
- Chopsticks
- Disposable plates
- Spoons
- Paper cups
- Plastic wraps (Vinyl)
- Receipts
- Beverage bottles (PET/Can)



---

## 6. Project Evaluation Table

| Evaluation Item         | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| Classification Accuracy | 70% accuracy at least                                        |
| Real-Time Response      | Whether results are shown quickly (ideally within 1–2 seconds) |
| Data Quality            | Ensure the model can correctly detect all 9 trained classes  |
| System Stability        | If the system runs 10+ times in a row without crashing       |

---



---

## 7. Roles & Contributions

| Name        | Responsibilities                                     |
| ----------- | ---------------------------------------------------- |
| HANSUSEONG  | - Hardware setup (web-cam, lighting, display)        |
|             | - Custom dataset collection for 9 waste categories   |
|             | - Model deployment and testing on real hardware      |
| SEOYOUNGWOO | - Model training using YOLOv8 and performance tuning |
|             | - Implementation of two-stage classification logic   |
|             | - Demo video production and documentation            |

