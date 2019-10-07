# Laboratoire 3 / Voyez votre horoscope

### Requirements:

* python3  
* python3-venv on linux  
* nginx  

### Getting started:

1. Open a terminal (Linux/MacOS) or a PowerShell command prompt (Windows)  
1. Clone the project  
1. Go to the directory : `cd travail-3-AlexisCode101/code/`  
1. Create a virtual `environnement using: python -m venv venv`  
1. Activate the virtual environnement using: `source venv/bin/activate` on Linux/MacOS  
or `.\venv\Scripts\activate` on Windows  
1. Install requirement: `pip install -r requirement.txt`  
1. Run the app : `python app.py`  
1. Change all the paths for the one of the project on your computer
1. Copy the config file `horoscope` into the folder `sites-available` of NGINX folder  
1. Now create a symbolic link of horoscope to the folder `sites-enabled` of NGINX folder  
1. Restart NGINX
1. Enter the following address in your favorite browser :  https://127.0.0.1/  
