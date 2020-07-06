#this my views comment
from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=7D6AB1DA-AEEB-4A16-BF1E-F62FC0063DBB") 
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7D6AB1DA-AEEB-4A16-BF1E-F62FC0063DBB") 
	

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	if api[0]['Category']['Name'] == "Good":
		category_description = "(0-50) Air quality is good"
		category_color = "good"
	elif api[0]['Category']['Name'] == "Moderate":
		category_description = "(50-100) Air quality is moderate"
		category_color = "moderate"
	else:
		category_description = "(100-150) Air quality is bad"
		category_color = "Bad"

	zipcode =''
	return render(request, 'home.html', {
		'api': api,
		'category_description':category_description,
		'category_color':category_color,
		'zipcode': zipcode
		})


def about(request):
	return render(request, 'about.html', {})



