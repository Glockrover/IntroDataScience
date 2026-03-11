# Training Tools & Concepts Overview

This document provides a high-level summary of the tools and core concepts we will be using throughout this data science training in DataThink. 

---

## 🛠️ Core Tools

### **Python**
Our primary programming language. It is designed to be readable and clean, making it the most widely used language in data science, machine learning, and scientific research. You can be able to prototype with it in every program that you want to do.

### **Marimo Notebooks**
A reactive Python notebook. Unlike traditional notebooks, Marimo runs as pure `.py` files. When you change one cell, all dependent cells update automatically, ensuring your outputs are never "stale". It is also perfect for version control in GitHub/GitLab and etc. It always runs from top to bottom. 

### **Git Version Control**
A system for tracking changes to your code. It allows you to save "checkpoints" of your work, revert to previous versions, and collaborate safely without overwriting other's progress. It was built by Linux to be able to manage open source repositories.

### **uv Package Management**
It is the new standard package manger that is extremely fast written in Rust. It is 10-100x faster than traditional tools like `pip`, allowing for near-instant package installation and environment setup.  

### **VS Code**
Our primary code editor. It is a powerful, free tool that supports syntax highlighting, error catching, and integrated Git support, making it the industry standard for development and it is wildly used by all types of developers.

### **Polars Data Wrangling**
A blazing fast DataFrame library for Python. Written in Rust, it uses parallel execution to process data 5-10x faster than the older Pandas library while being more memory-efficient. It is used for data manipulation and analytics. 

### **Plotly Visualization**
A library for creating beautiful, interactive charts. Users can hover to see values, zoom into specific areas, and filter data directly within the browser or notebook.

---

## 📊 Data Science Fundamentals

Data science is the practice of turning raw data into actionable insights using statistics, programming, and domain expertise. And using that data to come up with a conclusion. 

**Key Activities:**
- **Cleaning:** Preparing messy real world data for analysis.
- **Exploration:** Finding patterns and trends through visualization.
- **Modeling:** Building algorithms to make predictions.
- **Communication:** Translating technical findings into clear stories for decision making.

---

## ✍️ Markdown Writing

We use Markdown to write all our documentation. It is a simple way to format plain text using symbols you type directly:

- **# Heading** for titles
- **\*\*bold\*\*** for emphasis
- **\*italics\*** for subtle emphasis
- **- lists** for bullet points
- **`inline code`** and **```code blocks```** for technical snippets
- It is not ~~ThinkData~~ it is **DataThink**
- **To learn more about markdown read: [markdown](https://www.markdownguide.org/)** 
- **To import images use:** \![description of your image](url of the image in the browser or on your own local machine) 
- **![Images](https://blog.ronin.cloud/content/images/2022/02/markdown.png)**

Markdown files (`.md`) are future-proof, professional, and work across almost every modern platform.
