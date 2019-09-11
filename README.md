# Serverless Server

This repository was created as a part of the article published on [Medium.com](https://medium.com/@almasmyrzatay/how-to-easily-set-up-serverless-server-for-iot-devices-using-amazon-aws-lambda-python-flask-d7e9d79dbe0?source=friends_link&sk=62421aa7adb972a604e6c178499f3fc0)

### **Outline**

### **Summary**

Repository contains source codes to get started with RESTful API web services using Python Flask, Request and Zappa libraries/frameworks. Files in the repo should be used as an example to get one started with API web services, and to create first API calls from _Rest client_: IoT device, web browser, application, etc.

There are 2 components to the repository. First, let's assume we have _server_ that provides an API endpoints with various information. Also, let's assume we have _Rest client_ that is connected to WiFi, and will request various information from the server.

- Folder `rest_http_functions/` contains example HTTP methods, written in Python Flask, that you can upload to server. This directory will be placed in the server and they will be accessible via API calls from _Rest client_.
- Folder `python_api_requests/` contains all the API requests you can make from the remote server. This directory will be placed in any _Rest client_ that will request information from the server using Python.

**In sum**, here is what this repo covers:

- Flask functions with HTTP methods (GET, POST, PUT, DELETE)
- Examples & source code to test API requests visually without coding via web browser using **Restlet Google Chrome Extension**
- Examples & source code to make API requests using [Python HTTP Request library](https://realpython.com/python-requests/)
- Resources to read about AWS Lambda and 'serverless'

### Repo Organization

- `rest_http_functions/`
  - Source code to create API endpoints uing Python Flask micro-framework
- `python_api_requests/`
  - Source code to make API requests using Python Requests lib
- `restlet_api_requests/`
  - Folder contains `.json` file with pre-filled values, which you can upload to [Restlet Google Chrome Extension](https://restlet.com/modules/client/). You can test your API requests in the browser without coding.
- `app.py`
  - Main file to run server-side application

### How to run code

- Create directory:
  ```bash
  mkdir restful_api
  cd restful_api
  ```
- Download repository via HTTP or SSH from GitHub
- Create virtual environment & install `requirements.txt`

There are 2 components that you need to run:

1. Server-side application
2. Rest client side application

#### 1. Server side application

- All the code necessary to generate API endpoints are located in the folder `rest_http_functions/`
- To run locally

  ```bash
  # activate virtual environment
  source <your-virtual-environment>/bin/activate
  cd restful_api
  # run server-side application
  python app.py
  ```

- In your terminal you should see message with the following output:
  ```
  * Serving Flask app "rest_http_functions"
  * Environment: production
  * Debug mode: on
  * Running on http://127.0.0.1:5000/
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 206-758-016
  ```
- If you see the message above it means Python Flask is successfully running API endpoints locally on port 5000
- You can test it via curl in terminal or in web browser, type:

  - In web browser URL, type in:

  ```bash
  http://127.0.0.1:5000/all
  ```

  - In Terminal window:

  ```bash
  curl http://127.0.0.1:5000/all
  ```

  The output should be:

  ```
  {
  "body": {
      "allDevices": [
      "deviceId-1"
      ]
  },
  "statusCode": 200
  }
  ```

- **All API endpoints** are located in the folder: `python_api_requests/helpers/api_endpoints.py`

#### 2. Rest client side application - Restlet

As you have API endpoints that are currently running on your local machine, you can test them by writing Python scripts and/or using Restlet Google Chrome extension.

1. Navigate to Restlet.com and install the extension
2. Navigate to folder: `restlet_http_functions/restlet_api_request.json`
3. Import `.json` file to Restlet
4. Now, you should be able to make API requests via web browser for all the open endpoints through web-browser without writing code

#### 2. Rest client side application - Python

- All the code necessary to make an API calls using Python are located in the folder: `python_api_requests/`
- Navigate to template file: `python_api_requests/.env.sample` and create `.env` file using the template. This file will have URL and Port number to access API endpoints.

  - To test locally, change `URL` variable to `http://127.0.0.1:5000/`

- Then, you can make an API call to server (in local environment). Crete `get_devices_all.py` file and past the following code:

  ```python
  import json
  from python_api_requests.controllers.get_all_devices import get_all_devices

  def main():

      # Get all devices in DB
      response = get_all_devices()
      print("Response: {}".format(response))

  if __name__ == "__main__":
      main()

  ```

- Code will print out in terminal
  ```
  {
  "body": {
      "allDevices": [
      "deviceId-1"
      ]
  },
  "statusCode": 200
  }
  ```

## OPTIONAL: AWS Lambda and Zappa Deployment

In this section we will focus on server side application in the AWS Lambda functions. In other words, we will create 'serverless server' that will host API endpoints.

- Before you proceed, please make sure environment is set up, and Zappa is already installed
- Navigate to main directory `restful_api/`, where `app.py` file is located

- To upload source code to AWS Lambda using Zappa

  ```bash
  # if uploading for the first time
  zappa upload dev
  # if updating code
  zappa update dev
  ```

  Note: you don't have use `dev` argument provided above

- You should have source code deployed to AWS Lambda and have an open API endpoint. You should have URL link that looks like below:

  ```
  https://XXXXXX.execute-api.REGION-XX-X.amazonaws.com/dev
  ```

### On your device

- Now, refer back to [2. Rest client side application - Python]() section to repeat the procedure from client-side.

- Navigate to template file: `python_api_requests/.env.sample` and create `.env` file using the template. This file will have URL and Port number to access API endpoints.

  - In this case it will be:

  ```
  https://XXXXXX.execute-api.REGION-XX-X.amazonaws.com/dev/
  ```

## Resources

- [Serveless Python 1 - Serverless Library + HTTP Methods](https://read.iopipe.com/the-right-way-to-do-serverless-in-python-e99535574454)
- [Serveless Python 2 - Flask](https://read.iopipe.com/the-right-way-to-do-serverless-in-python-part-2-63430131239)
- [Serverless Web Scraping using AWS and Python](https://medium.com/@jcalabrese16/serverless-web-scrap-using-aws-lambda-and-s3-python-12bf1d27ea3f)
- [Hitchhiker's Guide to Serverless](https://hackernoon.com/the-hitchhikers-guide-to-serverless-ec5efb8075d6)
- [Custom Domain Name](https://github.com/amplify-education/serverless-domain-manager)
- [Should you use server or AWS lambda?](https://servers.lol/)
- [Beautiful Soup - Python library to parse HTML and XML data](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
