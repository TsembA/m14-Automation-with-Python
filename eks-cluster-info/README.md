# ☸️ AWS EKS Cluster Info Fetcher (Python + Boto3)

## 📌 Description

This Python script uses the **Boto3 SDK** to connect to **Amazon EKS (Elastic Kubernetes Service)** in a specified region and retrieves essential information about all available EKS clusters. It's useful for DevOps engineers, for quick visibility into EKS environments.

---

## 🔧 Features

- 📍 Connects to a specified AWS region (e.g., `us-west-1`)
- 🔍 Lists all EKS clusters in that region
- 📊 Fetches and displays for each cluster:
  - Status (`ACTIVE`, `CREATING`, etc.)
  - API endpoint (used to connect via `kubectl`)
  - Kubernetes version

---

## 🧠 How It Works

1. Uses Boto3 to connect to the AWS EKS service.
2. Retrieves a list of cluster names via `list_clusters()`.
3. For each cluster, calls `describe_cluster()` to extract:
   - `status`: lifecycle state of the cluster
   - `endpoint`: API server endpoint for Kubernetes
   - `version`: current Kubernetes version

---

## 💻 Example Output

```
Cluster my-eks-prod status is ACTIVE
Cluster endpoint: https://ABCDEFG1234567.gr7.us-west-1.eks.amazonaws.com
Cluster version: 1.29

Cluster dev-cluster status is CREATING
Cluster endpoint: https://XYZ9876543210.gr7.us-west-1.eks.amazonaws.com
Cluster version: 1.28
```

---

## 📁 Python Script

```python
import boto3

client = boto3.client('eks', region_name="us-west-1")
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(name=cluster)
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version: {cluster_version}")
```

---

## ✅ Requirements

- Python 3.x
- `boto3` (`pip install boto3`)
- AWS credentials configured (`~/.aws/credentials`, environment variables, or IAM role)

---

## 🚀 Use Cases

- Cluster inventory and environment audit
- Automated infrastructure status checks
- Input for monitoring dashboards
