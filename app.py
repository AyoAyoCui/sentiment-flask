from flask import Flask, request, jsonify, send_from_directory
from wordcloud_gen import generate_wordcloud_image
from trend_chart import generate_trend_chart
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "舆情分析 Flask 服务运行中！"

@app.route("/wordcloud", methods=["POST"])
def wordcloud():
    data = request.get_json()
    text = data.get("text", "")
    generate_wordcloud_image(text)
    return jsonify({"img_url": request.host_url + "static/wordcloud.png"})

@app.route("/trend", methods=["POST"])
def trend():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "请上传CSV文件"}), 400
    file.save("sample.csv")
    generate_trend_chart("sample.csv")
    return jsonify({"img_url": request.host_url + "static/trend.png"})

@app.route("/static/<filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)