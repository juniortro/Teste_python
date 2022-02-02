from flask import Flask, request

app = Flask("Exercicio_2")

@app.route('/api/v1/message/', methods=['POST'])
def message():
    body = request.get_json()
    
    return body

app.run()