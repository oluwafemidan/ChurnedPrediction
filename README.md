# Prediction of Churned Customers

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Docker](#deployement-on-docker)
  * [Directory Tree](#directory-tree)
  * [License](#license)
  * [Credits](#credits)

## Demo
Demo Screenshot: ![Screenshot](https://private-user-images.githubusercontent.com/146761013/311536571-ff17d456-f8e7-4ae8-8df2-9905f2e501c9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTAwOTY1NTIsIm5iZiI6MTcxMDA5NjI1MiwicGF0aCI6Ii8xNDY3NjEwMTMvMzExNTM2NTcxLWZmMTdkNDU2LWY4ZTctNGFlOC04ZGYyLTk5MDVmMmU1MDFjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMxMFQxODQ0MTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OTMyOTgyMzdmMTVhNjc3MDRmYTc0Y2FhZWRhZDBkZTIzOTM2YTc3NDQ5MThlNGI1YmZiNTA3OWVjYWQ2NzAyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.8OSN95crJeElJ2XWP7FtH7j5wp7PLnxKG6I623ivL3A)

## Overview
My objective revolves around the development of a sophisticated customer churn prediction system. Through the strategic application of advanced analytics and machine learning methodologies, I aim to harness the insights latent within our extensive customer dataset. My approach includes deploying the predictive model on Docker using Flask web application framework. By doing so, I endeavor to furnish the company with a reliable mechanism for accurately anticipating customer churn. This, in turn, will empower the organization to execute targeted retention strategies, thereby fostering sustained customer engagement and enhancing overall business performance.

## Installation
The Code is written in Python 3.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r req.txt
```
## Run
### STEPS:

Clone the repository

```bash
https://github.com/oluwafemidan/ChurnedPrediction.git
```
### STEP 01- Launch Anaconda Prompt Command after opening the repository
Copy the directory from the resipository and paste it on the Anaconda prompt

```bash
C:\Users\HP 2022\OneDrive\projects\Telecomm deployment with Docker
```
Input `cd` and `flask` in the prompt command
```bash
cd flask
```


### STEP 02- install the requirements
```bash
pip install -r req.txt
```

```bash
# Finally run the following command
python app.py
```
## Deployement on Docker
 ### Pre-requisites      
 1. System should have [docker engine](https://docs.docker.com/install/) installed.      
     
 ### Hosting the web service      
 1. Build the docker image       
```bash
docker build -t churned_predimg:v1 .  
```   
2. Check the image       
```bash 
docker images 
``` 
<p align="center">          
  <img src="/docs/images/mpws-01.png" alt="Docker Images">          
</p>          
    
3. Run the container      
```bash
docker run -dp 8080:5000 -ti --name mlContainer churned_predimg:v1
```    
    
4. Check whether the container is up       
```bash 
docker ps 
``` 
<p align="center">          
  <img src="/docs/images/mpws-02.png" alt="Running Containers">          
</p>          
      
      
>When we run the container two scripts are initiated:  
>1. `app.py` which hosts the model as a web service.      
 ---      

Now,
```bash
open up you local host and port
```
