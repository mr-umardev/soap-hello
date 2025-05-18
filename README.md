# SOAP Client using WSDL (Python + Zeep)

## 🧾 Problem Statement

**Task:**  
Implement a client to consume methods from a WSDL service which is available over the internet. Your client program should access the exposed methods in WSDL and perform necessary operations.

---

## ✅ Solution Overview

This project uses Python and the `zeep` SOAP client library to consume operations from a public WSDL service (Calculator API). It performs the following operations by invoking SOAP methods:

- Add
- Subtract
- Multiply
- Divide

The WSDL service used is publicly accessible:  
**URL:** `http://www.dneonline.com/calculator.asmx?WSDL`

---

## 🛠️ Requirements

- Python 3.7 or higher
- `zeep` library (for consuming WSDL services)
- Virtual environment (recommended)

---

## 📁 Folder Structure

soap_client/
├── client.py # Main client code
├── wsdl/ # Optional folder for saving WSDL locally
│ └── calculator.wsdl
├── venv/ # Virtual environment (created locally)
├── requirements.txt # List of dependencies
└── README.md # Project guide

## Create and activate a virtual environment

🔹 Windows
python -m venv venv
venv\Scripts\activate

## Install required dependencies

pip install zeep

## Run the client code

python client.py

## ✅ How This Meets the Requirements

Requirement Implementation
Consume WSDL from internet The client accesses the WSDL URL http://www.dneonline.com/calculator.asmx?WSDL directly.
Access exposed methods Methods Add, Subtract, Multiply, and Divide are called using the zeep client.
Perform operations Operations are performed using inputs (intA, intB) and printed to the console.
Proper structure Code is modular, organized into a folder structure with optional WSDL storage and a README.
Virtual environment Setup instructions include creation and activation of a virtual environment for best practices.
