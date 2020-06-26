import pytest
from .api import app
import requests
import warnings
import re
import time

from requests.packages.urllib3.util.retry import Retry

# with warnings.catch_warnings():
#     warnings.filterwarnings("ignore",category=DeprecationWarning)
#     from flask_testing import TestCase

class Test_API:
	client  = app.test_client()
		
	@pytest.fixture(autouse=True, scope='session')
	def setUp(self):
		app.config['TESTING'] = True
	
	def test_app_from_first_port(self):
		response = requests.get('http://localhost:8001/hello')
		assert response.status_code == 200
		assert "Hello from the process" in response.text
		
	def test_app_from_second_port(self):
		response = requests.get('http://localhost:8002/hello')
		assert response.status_code == 200
		assert "Hello from the process" in response.text
				
	
	def test_nginx_response(self):
		response = requests.get('http://localhost:8001/hello')
		assert response.status_code == 200
		assert "Hello from the process" in response.text
		message_from_first_app = response.text

		response = requests.get('http://localhost:8002/hello')
		assert response.status_code == 200
		assert "Hello from the process" in response.text
		message_from_second_app = response.text

		response = requests.get('http://localhost:8000/hello')
		assert response.text == message_from_first_app or message_from_second_app
		
	def test_conf_file_contents(self):
		with open('python.conf', 'r') as f:
			content = f.read()
			assert "location /hello" in content
			assert "server localhost:8001" in content
			assert "server localhost:8002" in content
			assert "listen 8000" in content
			
		
	
