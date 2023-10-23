from flask import Flask

app = Flask(__name__)


@app.route('/')
def serve_html():
    with open('mobile_out.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
