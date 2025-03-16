state = "West Bengal"
city = "kolkata"

api_key = "01935a87d8ebcb7f5154b662dea73747"
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
 data = response.json()
 print(json.dumps(data, indent=4))
 print(f"Current Weather Condition: {data['weather'][0]['main']}")
 print(f"Current Temperature: {data['main']['temp']}°C.")
 print(f"Temperature Feels Like: {data['main']['feels_like']}°C.")
 print(f"Humidity: {data['main']['humidity']}%.")

else:
  print("Error Occured")
