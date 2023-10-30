from dream import grab_image
from flask import Flask, abort, request, send_file
from flask_cors import CORS
import os


app = Flask(__name__)


# Configure CORS to allow access from frontned
CORS(
  app, 
  resources={
    r"/dream/*":{
      "origins":"https://sliqfrontend.frankcheng7.repl.co"
    }
  }
)

@app.route('/')
def index():
  return 'Sliq'

@app.route('/dream')
def dream():
  print('got here')
  # Get the values from query parameters
  prompt = request.args.get('prompt')
  pwd = request.args.get('pwd')
  imgWidth = request.args.get('imgWidth')
  imgHeight = request.args.get('imgHeight')
  print(prompt, pwd, imgWidth,imgHeight)

  # A very very naive authentication
  # Return a 404 error response if incorrect pwd
  if pwd != os.environ['MY_PWD']:
    print('wrong pwd', pwd, os.environ['MY_PWD'])  
    abort(404)

  # A very very naive cache
  # Also acts as a naive logging system
  # Return a saved image if we already have one for the prompt
  if os.path.exists(f"img/{prompt}{imgWidth}x{imgHeight}.png"):
      print('default --')
      return send_file(
        f"img/{prompt}{imgWidth}x{imgHeight}.png", 
        mimetype='image/png'
      )

  # Request the image from dream studio and then return it
  print('grab_image --')
  grab_image(prompt, int(imgWidth), int(imgHeight))
  return send_file(
    f"img/{prompt}{imgWidth}x{imgHeight}.png", 
    mimetype='image/png'
  )


app.run(host='0.0.0.0', port=81)
