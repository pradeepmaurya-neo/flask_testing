from flask import Flask, jsonify

app=Flask(__name__)


@app.route('/api/name', methods=['GET'])
def hello():
    try:
        data=['hello', 'pradeep']

        return jsonify({
        'status':'sucess',
        'data':str(data),
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
        })




if __name__=='__main__':
    app.run(debug=True)