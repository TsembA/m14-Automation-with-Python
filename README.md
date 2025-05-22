# 🩺 EC2 Instance Status Checker with Boto3

This Python script uses the AWS SDK for Python (**Boto3**) to automatically retrieve and display both the **state** and **health status** of your EC2 instances in a specified AWS region.

---

## 🚀 What This Script Does

### 1️⃣ List EC2 Instance States

- Uses `describe_instances()` to retrieve all EC2 instances.
- Loops through each instance to print its:
  - Instance ID
  - Current lifecycle state (e.g., `running`, `stopped`, `terminated`)

### 2️⃣ Check EC2 Health Status

- Uses `describe_instance_status(IncludeAllInstances=True)` to check:
  - **Instance state** — EC2 lifecycle status
  - **Instance status** — Software-level health
  - **System status** — Hardware and infrastructure health

---

## 📋 Sample Output

```
EC2 Instance States:
Instance i-0123456789abcdef0 is currently running
Instance i-0abcdef1234567890 is currently stopped

🔧 EC2 Instance Health Checks:
Instance i-0123456789abcdef0 state: running | Instance status: ok | System status: ok
Instance i-0abcdef1234567890 state: stopped | Instance status: insufficient-data | System status: insufficient-data
```

---

## 🧰 Requirements

- Python 3.6+
- Boto3 library
- AWS credentials configured (`aws configure` or environment variables)

Install dependencies:

```bash
pip install boto3
```

---

## 🧠 Why Use This Script?

This script is useful for:

- Daily auditing of EC2 instances
- Quickly checking for degraded or impaired instances
- Automating health checks across multiple regions or environments
- Integrating with alerting tools (email, SNS, Slack, etc.)

---

## ✅ How to Run

```bash
python ec2_health_check.py
```
