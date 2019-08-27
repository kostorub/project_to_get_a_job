project_to_get_a_job

Using aiohttp + sqlite to get weather for towns with names like London or Moscow 

Clone repo and follow these steps.

```
git clone https://github.com/kostorub/project_to_get_a_job.git
cd project_to_get_a_job
python3 -m venv venv
```

If you use *nix, make
```
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```
If windows
```
.\venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```


For test make
```
curl http://127.0.0.1:7000/weather/get_weather?town_name=Moscow
```
In result check field content
`
Content: {"town": "Moscow", "temp": 13.14, "units": "metric"}
`

To check database with logs use https://sqlitebrowser.org/

The database file is in the root folder and is called **sqlite.db**