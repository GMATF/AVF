from flask import Flask , render_template , request


app = Flask ( __name__ )

@app.route('/' , methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about' , methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/services' , methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/contact' , methods=['GET'])
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=6969, debug=True, threaded = True)
