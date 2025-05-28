## 14 - Automation with Python

### AWS Integration with boto3

This module showcases how to automate AWS tasks using Python's official SDK, **boto3**. While tools like Terraform are ideal for provisioning new infrastructure, boto3 is particularly effective for managing and automating operations on existing AWS resources.

Use cases include:

- Creating and managing EC2 snapshots for backup automation
- Applying bulk tags to instances across regions
- Monitoring EC2 health and sending alerts via email if usage thresholds are exceeded

### Client vs Resource Interfaces in boto3

Boto3 provides two types of interfaces:

- **Client**: A low-level interface offering direct access to AWS APIs, returning responses in raw JSON-like dictionaries.
- **Resource**: A high-level, object-oriented wrapper that simplifies interactions with AWS services.

While the client interface offers full control, the resource interface is generally easier to work with for common use cases.

### Python vs Terraform for Automation

- **Terraform**: Designed for declarative Infrastructure as Code (IaC). Ideal for provisioning infrastructure with simple, repeatable commands.
- **Python (with boto3)**: Offers more flexibility and control. Useful for dynamic automation, scripting complex tasks, and integrating monitoring or backup operations.

Terraform is concise and purpose-built for infrastructure provisioning. Python, on the other hand, excels when automation needs go beyond IaC—especially in scenarios involving logic, data processing, or web interfaces.

For example, Python frameworks like **Flask** or **Django** can be used to build web apps or dashboards that interact with AWS resources via boto3, enabling user-friendly cloud management tools.

---

📁 This module includes sample scripts that demonstrate EC2 monitoring, snapshot automation, and Linode server management with Paramiko and the Linode API.
