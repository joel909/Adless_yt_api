from flask import Flask,render_template
from flask_cors import CORS, cross_origin
from youtubesearchpython.__future__ import VideosSearch
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/app/test",methods=["GET"])
def test_reply():
    return {"messgage":"Suscess"}

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/watch')
def watch():
    return render_template('hello.html')

@app.route('/search/<query>')
async def Search(query):
    print("USER Queryied for:",query)
    videosSearch = VideosSearch(query, limit = 20)
    videosResult =  await videosSearch.next()
    #print(videosResult["result"])
    complete_data = []
    print(len(videosResult["result"]))
    for i in range(0,len(videosResult["result"])):
        title = videosResult["result"][i]["accessibility"]["title"]
        video_id = videosResult["result"][i]["id"]
        preview = f"https://www.youtube.com/embed/{video_id}"
        data = {"title":title,"preview":preview,"video_id":video_id}
        complete_data.append(data)

    
    
    #print(video_search_results["result"])
    return {"data":complete_data,"total_results":len(videosResult["result"])}

if __name__ == "__main__":
    app.run(port=8000,debug=True)   