import requests

class adopt:
  def __init__(self):
    self.url = "https://www.adoptapet.com/public/apis/pet_list.html"

  def adopt_pets(self):
    r = requests.get(self.url)
    response = r.json()
    print(response)