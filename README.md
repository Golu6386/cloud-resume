# Cloud Resume Challenge - Serverless Visitor Counter

This project is a fully functional, serverless web application built on AWS. It serves as my digital resume and features a real-time visitor counter that tracks and displays the total number of visits to this site.

## 🚀 Live Demo
[Click here to view my live resume](https://golu-cloud-resume-2026.s3.ap-south-2.amazonaws.com/index.html)

## 🛠️ Tech Used
* **Frontend:** Static website hosted on Amazon S3.
* **Backend:** Python-based AWS Lambda function.
* **Database:** DynamoDB for storing the visit counts.
* **API:** Amazon API Gateway to handle HTTP requests and bridge the frontend/backend.
* **Security:** IAM Roles for least-privilege access and CORS for secure frontend communication.

## 💡 Key Learnings
- **Infrastructure as Code:** Gained hands-on experience in configuring AWS services to work in harmony.
- **Debugging:** Successfully navigated challenges with CORS policies, API-to-Lambda permissions, and browser caching.
- **Serverless Paradigm:** Built an event-driven system without managing a single server.

## 📂 Project Structure
- `/frontend`: Contains the `index.html` file and frontend logic.
- `/backend`: Contains the Python code for the Lambda function.

## ⚙️ How it works
1. **Frontend:** A user visits the static site hosted on S3.
2. **API Trigger:** The browser performs a GET request to the API Gateway.
3. **Compute:** API Gateway triggers the Lambda function.
4. **Data:** Lambda updates the visitor count in DynamoDB using the Boto3 library and returns the new value.
5. **Display:** The JavaScript on the frontend updates the page content dynamically.