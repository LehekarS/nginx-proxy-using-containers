# 🔁 NGINX Reverse Proxy to Python Flask App (Using `--link` and Official NGINX Image)

This project shows how to run a **Python Flask application** in one Docker container and use the **official NGINX image** as a reverse proxy in another container. The containers are connected using Docker's legacy `--link` option, and the NGINX configuration is mounted directly from your project folder.

---

## 📁 Project Structure

nginx-proxy-using-containers/
├── app.py # Python Flask app
├── index.html # HTML content served by Flask
├── style.css # CSS styling
├── requirements.txt # Flask dependencies
├── Dockerfile # Builds the Flask app container
├── default.conf # NGINX reverse proxy config


---

## 🚀 How to Run

### 1. Clone the Repository

git clone https://github.com/LehekarS/nginx-proxy-using-containers.git
cd nginx-proxy-using-containers

### 2. Build and Run the Flask App Container

docker build -t flask-app .
docker run -d --name flask-container flask-app
✅ This runs your Python Flask app container. The app listens on port 5000.

### 3. Run the NGINX Container (Official Image) and Link to Flask App
   
docker run -d \
  --name nginx-container \
  -p 80:80 \
  --link flask-container:flask-app \
  -v $(pwd)/default.conf:/etc/nginx/conf.d/default.conf:ro \
  nginx
✅ This uses the official NGINX image, links to the Flask app container, and mounts your NGINX config.

### 4. Open in Browser
Visit: http://localhost or your instance public ip
You should see your Flask app served via NGINX.

⚙️ NGINX Configuration
default.conf:

server {
    listen 80;

    location / {
        proxy_pass http://flask-app:5000;
    }
}
flask-app is the alias given to flask-container via --link.

NGINX listens on port 80 and forwards all traffic to the Flask app on port 5000.


❗ Notes
--link is a legacy feature. It works, but it's deprecated.

For modern setups, it's recommended to use user-defined Docker networks (--network).
