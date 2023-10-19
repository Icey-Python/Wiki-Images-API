import requests
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def welcome():
  return 'hello world'


@app.get('/me')
def call(me: str):
  return f'hello {me}'


@app.get('/api/v1/<string:query>')
def get_image(query: str) -> dict:
  url = f"https://en.wikipedia.org/w/rest.php/v1/search/title?q={query}"

  response = requests.get(url)
  response.raise_for_status()
  data = response.json()

  # error handling
  try:
    key = data['pages'][0]['key']
    title = data['pages'][0]['title']
  except IndexError:
    key = None
    title = None
  except TypeError:
    key = None
    title = ''

  if key is not None:
    image_link = f"https://en.wikipedia.org/api/rest_v1/page/summary/{key}"
    image_url = requests.get(image_link).json()['thumbnail']['source']
  else:
    image_url = None

  return {"title": title, "image": image_url}


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)
