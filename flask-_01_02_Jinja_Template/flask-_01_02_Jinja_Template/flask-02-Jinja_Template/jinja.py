from flask import Flask, render_template

app = Flask(__name__)

'''
Create a function named `head` which sends number `number1`
and `number2` variables to the `index.html`. 
Use these variables into the `index.html` file. 
Assign a URL route the `head` function with decorator `@app.route('/')`.
'''






if __name__== "__main__":
    app.run(debug=True) #This app run by defaul on port=5000
    #app.run(debug=True, port=3000)
    # app.run(host= '0.0.0.0', port=8081)