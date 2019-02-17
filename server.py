from flask import Flask, jsonify, send_from_directory
app = Flask(__name__, static_url_path='')


PING_COUNT = 1

@app.route('/')
def index():
    return send_from_directory('', 'index.html')


@app.route('/api/todos', methods=['GET'])
def todosController():
    todos = [
        {
            'task': 'Clean room',
            'done': False,
        },
        {
            'task': 'Cook food',
            'done': False,
        }
    ]

    res = jsonify(todos)
    res.status_code = 200

    return res


@app.route('/api/ping', methods=['POST'])
def pingController():
    global PING_COUNT
    PING_COUNT += 1
    print 'Button clicked {0} times'.format(PING_COUNT)
    res = jsonify(success=True)
    return res


if __name__ == '__main__':
    app.run()