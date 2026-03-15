# AI-Powered DevOps Log Monitoring System

## Project Overview

This project demonstrates a **cloud-native DevOps monitoring pipeline** that collects application logs, analyzes them for anomalies, and sends automated alerts.

The system uses containerization, centralized logging, serverless computing, and event-driven automation to simulate real production monitoring environments used by modern DevOps teams.

---

# Architecture

Application logs are collected and processed through the following pipeline:

Application → Docker → EC2 → CloudWatch Logs → Lambda → SNS → Email Alerts

---

# Features

• Containerized Python application
• Centralized log collection
• Automated log monitoring
• Event-driven alert system
• Serverless log processing
• Cloud-based deployment
• AWS Free Tier compatible infrastructure

---

# Technology Stack

## Cloud Platform

* AWS EC2
* AWS CloudWatch
* AWS Lambda
* AWS SNS
* AWS IAM

## DevOps Tools

* Docker
* Git
* GitHub

## Programming Language

* Python

---

# Project Structure

```
ai-devops-log-monitoring
│
├── app
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.log
│
├── lambda
│   └── lambda_function.py
│
└── README.md
```

---

# Deployment Steps

## Clone Repository

```
git clone https://github.com/<yourusername>/ai-devops-log-monitoring.git
```

---

## Build Docker Image

```
docker build -t ai-log-app .
```

---

## Run Container

```
docker run -d -p 5000:5000 ai-log-app
```

---

# AWS Infrastructure Setup

1. Launch EC2 instance
2. Install Docker
3. Deploy containerized application
4. Configure CloudWatch agent
5. Stream logs to CloudWatch
6. Create Lambda log analyzer
7. Configure SNS alerts
8. Connect CloudWatch subscription filter

---

# Monitoring Workflow

User Request
↓
Application generates logs
↓
CloudWatch collects logs
↓
Lambda analyzes log events
↓
SNS sends alert notification

---

# Future Improvements

• AI log anomaly detection using machine learning
• CI/CD pipeline with GitHub Actions
• Infrastructure as Code using Terraform
• Kubernetes deployment
• Grafana monitoring dashboard

---

# Author

DevOps Project Portfolio
