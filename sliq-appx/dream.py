import os
import requests
import base64


# grab image from dream studio
def grab_image(text_prompt: str, width: int, height: int):
  print('generating')
  url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

  body = {
    "steps": 20,
    "width": width,
    "height": height,
    "seed": 0,
    "cfg_scale": 10,
    "samples": 1,
    "text_prompts": [{
        "text": text_prompt,
        "weight": 1
    }],
  }

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": os.environ['DREAM_STUDIO'],
  }

  response = requests.post(
    url,
    headers=headers,
    json=body,
  )

  if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

  data = response.json()

  # Make sure the 'out' directory exists
  if not os.path.exists("img/"):
    os.makedirs("img/")

  for _, image in enumerate(data["artifacts"]):
    with open(f"img/{text_prompt}{width}x{height}.png", "wb") as f:
      f.write(base64.b64decode(image["base64"]))

  return
