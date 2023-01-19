# weather-rig
 
### Currently only tested for Windows

### Installation instructions:
Clone the repository to a folder of your choice and install required modules  
```
cd \\weather-rig

python -m venv venv

.\venv\scripts\activate

pip install -r requirments.txt
```

Configure your config.yaml (remove .default extension)  
  - You will need your own weatherapi.com API key (free for up to 1,000,000 requests per month).  
  - To enable discord notifications, you will need to enter your own webhook URL.  

Run the app:  
```
python .\src\manager.py
```

### Known issues:  
You will need to run python as admin if you want to start your script as admin.  
