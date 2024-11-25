from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello, Andrew Falcon!"

# Retrieve video from s3 and extract image
# Write image to lightsail filesystem
@app.route('/s3-retrieval', methods=['POST'])
def s3_retrieval():
   data = request.get_json()
   selected_videos = data.get('videos')
   for video in selected_videos:
      print(video)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)