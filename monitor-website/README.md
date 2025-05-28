# 🔍 Website Uptime Monitor & Auto-Recovery Tool

This Python script monitors the availability of a web application deployed on a Linode server and performs automated recovery actions in case of failure.

## 📌 Features

- ✅ Periodic health checks via HTTP requests
- 📧 Email alerts when the app is down
- 🐳 Automatic restart of the Docker container
- 🔁 Reboot Linode instance if it's unresponsive
- 🔒 Secure SSH access using private key

## 📁 Project Structure

```
monitor-website/
├── monitor-website.py       # Main monitoring script
├── .env                     # Environment variables (not committed)
├── requirements.txt         # Python dependencies
```

## 🔧 Requirements

- Python 3.8+
- A running Docker container on a remote server
- Linode API Token
- SSH private key access to your server

## 🛠 Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/TsembA/monitor-website.git
   cd monitor-website
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**  
   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASS=your_email_password_or_app_password
   LINODE_TOKEN=your_linode_api_token
   ```

4. **Update the script**  
   - Replace IP address and instance ID with your own
   - Set correct path to your private SSH key

5. **Run the script**  
   ```bash
   python import_requests.py
   ```

## 🧠 How It Works

1. Every 5 minutes, the script pings your app.
2. If it fails, it sends an email and attempts to restart the Docker container.
3. If that fails, it reboots the server and restarts the app after the server is back online.
