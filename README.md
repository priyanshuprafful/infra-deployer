## 🚀 InfraDeployer – A DevOps CI/CD Project

### 🔧 Project Overview

**InfraDeployer** is a motivational quote web app built using Python Flask, containerized using Docker, and deployed via a Jenkins CI/CD pipeline on an AWS EC2 instance.

This project demonstrates basic CI/CD principles using modern DevOps tools and cloud infrastructure.

---

### 🛠 Tech Stack Used

| Layer            | Tools Used               |
| ---------------- | ------------------------ |
| App Layer        | Python, Flask, HTML, CSS |
| Containerization | Docker                   |
| CI/CD            | Jenkins (Pipeline)       |
| Cloud Hosting    | AWS EC2                  |
| Version Control  | Git, GitHub              |

---

### 📷 Project Preview


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6d7a0bbc-ed43-48f9-9dcb-4710aed07f03" />


---

### 🧱 Project Architecture

```
GitHub Repo (Code) 
     ↓
Dockerfile builds image
     ↓
Image pushed to Docker Hub
     ↓
Jenkins Pipeline triggered
     ↓
EC2 instance pulls image
     ↓
Docker runs container
     ↓
Flask App served at <Public_IP>:5000
```

---

### 📦 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/infradeployer.git
cd infradeployer

# Create virtual environment (optional)
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Access the app in your browser at:

```
http://localhost:5000
```

---

### 🐳 Docker Usage (Manual Steps)

```bash
# Build Docker Image
docker build -t yourusername/infra-deployer .

# Run Container
docker run -d -p 5000:5000 yourusername/infra-deployer

# Push to Docker Hub
docker push yourusername/infra-deployer
```

---

### ⚙️ Jenkins Pipeline Setup

1. **Install Jenkins on EC2**
2. Install required plugins (Git, Docker, Pipeline)
3. Add Jenkins user to Docker group:

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

4. Create a **Pipeline Job** with this script:

```groovy
pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                sh 'docker pull yourusername/infra-deployer:latest'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 yourusername/infra-deployer'
            }
        }
    }
}
```

---

### 🌱 Future Improvements

* Automate infrastructure with **Terraform**
* Use **Ansible** for config management
* Add **GitHub Webhook** for automatic build trigger
* Deploy multiple services with **Kubernetes**
* Add **NGINX Load Balancer**
* Add monitoring with **Prometheus + Grafana**

---

### 🙌 Acknowledgements

This project is self-built and inspired by real-world DevOps practices. Special thanks to the DevOps community and learning resources.

---

### 📫 Contact

**Priyanshu Prafful**
📧 [priyanshuprafful@gmail.com](mailto:priyanshuprafful@gmail.com)
📦 [Docker Hub](https://hub.docker.com/u/priyanshuprafful)
🔗 [LinkedIn](https://linkedin.com/in/priyanshu8787)

---

 `⭐ Star` Me Please . 

---

