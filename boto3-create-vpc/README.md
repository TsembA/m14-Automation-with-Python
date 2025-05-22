# 🌐 AWS VPC Provisioning with Python & Boto3

This project demonstrates how to automate the creation and inspection of AWS VPC (Virtual Private Cloud) infrastructure using the **Boto3** Python SDK.

---

## 🚀 What the Script Does

### ✅ 1. Create a VPC
- Provisions a new VPC with the CIDR block `10.0.0.0/16`.

### ✅ 2. Create Two Subnets in the VPC
- One subnet with CIDR block `10.0.0.0/24`
- Another with CIDR block `10.0.2.0/24`

### ✅ 3. Tag the VPC
- Adds a `Name` tag with the value `my-vpc`.

### ✅ 4. List All VPCs
- Retrieves all VPCs in the account and prints their IDs.

### ✅ 5. Inspect CIDR Block Associations
- Displays CIDR block association state for each VPC.

---

## 🧰 Requirements

- Python 3.6+
- Boto3 installed
- AWS credentials configured (`aws configure` or env variables)

### Install Boto3:
```bash
pip install boto3
```

---

## 🧪 Example Output

```
vpc-0abc1234567def89
{'State': 'associated'}
vpc-0fgh9876543zyx10
{'State': 'associated'}
```

---

## ✅ Usage

1. Ensure AWS credentials are configured.
2. Run the script:

```bash
python create_vpc.py
```

---

## 📌 Notes

- The default region is determined by your AWS config unless specified in `boto3.client()` or `boto3.resource()`.
- Make sure the CIDR blocks used don’t overlap with existing VPCs or subnets in the region.