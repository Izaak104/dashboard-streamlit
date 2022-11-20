# dashboard-streamlit



Create a virtual machine on Azure
SSH into the virtual machine via powershell (on windows 11)
Run sudo apt-get update to update the vm
Run sudo apt install python3-pip to enable you install streamlit
Run pip3 install streamlit (note: ensure the required version of python is installed on the vm to facilitate the seamless installation of streamlit
Modify bashrc file using nano ~/.bashrc and helping the software locate streamlit
Pip install pandas
Update jinja2 package by running pip3 install jinja2 –upgrade
Run “touch covid_data.py” to create new python file
un nano covid_data.py to move into the .py file
Load various python packages (import streamlit as st; import pandas as pd; import numpy as np)
Write code to create a title for the dashboard
Save file and exit file editor (nano)
Run the code in the python file by (streamlit run covid_data.py –server.port80 to ensure the 80 is open
