from flask import Flask, render_template,request,jsonify,json

app=Flask(__name__)
@app.route('/api-name', methods=['POST'])
def func_name():
    if request.headers['Content-Type'] == 'application/json':
        response=request.json
        print response
        value1=response["array"]
        value1=value1+value1
        final={'array':value1}
        
        return jsonify(final)
        
    
    
        
    return ("Something when server fails")

@app.route('/test', methods=['GET'])
def test():
    value=[1,2,3,2]
    value={'array':value}

    return jsonify(value)



if __name__ == '__main__':
	app.run(debug=True)
