# Serverless Server

### **Summary**

Repository contains source codes to get started with AWS Lambda and RESTful API web services. Files in the repo should be used as an example to get one started with 'servleress server' set up, and create first API calls from IoT device.

Please refer to Part 1 & Part 2 of the article to find out more about this repo.

Let's assume we have IoT device that is connected to WiFi.

- Folder `python_api_requests/` contains all the API requests you can make from remote 'server', which in our case is AWS Lambda. In other words, this directory will go onto your IoT device that will request information from our 'server'.
- Folder `rest_http_functions/` contains example HTTP methods that you can upload to AWS Lambda. In other words, this directory will go into Lambda and we will call these functions from IoT device.

**In sum**, here is what this repo covers:

- Flask functions with HTTP methods (GET, POST, PUT, DELETE)
- Examples & source code to test API requests visually without coding via web browser
- Examples & source code to make API requests using [Python HTTP Request library](https://realpython.com/python-requests/)
- Resources to read about AWS Lambda and 'serverless'

### Repo Organization

- `rest_http_functions/`
- `python_api_requests/`
  - Source code to make API requests using Python
- `restlet_api_requests/`
  - Folder contains `.json` file with pre-filled values, which you can upload to [Restlet Google Chrome Extension](https://restlet.com/modules/client/). You can test your API requests in the browser for sanity check.
- `app.py`
  - Main file - source code runner

### How to run code

- Create virtual environment & install `requirements.txt`
- To run locally
  ```bash
  python app.py
  ```
- To upload source code to AWS Lambda
  ```bash
  # if uploading for the first time
  zappa upload dev
  # if updating code
  zappa update dev
  ```
  Note: you don't have use `dev` argument provided above

## Resources

### IOPipe Articles

- [Serveless Python 1 - Serverless Library + HTTP Methods](https://read.iopipe.com/the-right-way-to-do-serverless-in-python-e99535574454)
- [Serveless Python 2 - Flask](https://read.iopipe.com/the-right-way-to-do-serverless-in-python-part-2-63430131239)

## Articles

- [Serverless Web Scraping using AWS and Python](https://medium.com/@jcalabrese16/serverless-web-scrap-using-aws-lambda-and-s3-python-12bf1d27ea3f)
- [Hitchhiker's Guide to Serverless](https://hackernoon.com/the-hitchhikers-guide-to-serverless-ec5efb8075d6)
- [Custom Domain Name](https://github.com/amplify-education/serverless-domain-manager)
- [Should you use server or AWS lambda?](https://servers.lol/)
- [Beautiful Soup - Python library to parse HTML and XML data](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
