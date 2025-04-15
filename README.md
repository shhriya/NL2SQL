# Jenkins Docker Setup

This project sets up Jenkins using Docker. It uses the official Jenkins LTS image and exposes necessary ports for running Jenkins locally.

## How to Run

1. Make sure you have Docker installed.
2. Run the following command to build and start the Jenkins container:

   ```bash
   docker build -t my-jenkins .
   docker run --name jenkins -d -p 8080:8080 -p 50000:50000 my-jenkins
