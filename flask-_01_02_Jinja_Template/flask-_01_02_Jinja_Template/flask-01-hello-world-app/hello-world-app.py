
#   mport Flask module.
from flask import Flask 

#   Create an object named `app` from imported Flask module.
app = Flask(__name__)

#   Assign a URL route to the `hello` function with decorator `@app.route('/')`.
@app.route('/')

#   Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')`. 
def hello():
     return "Hello World"

@app.route('/second')
def second():
      return "This is second page"

'''
Create a function `third` which returns a string `This is the subpage of third page` and assign a URL 
route the `third` function with decorator `@app.route('/third/subthird')`.
''' 
@app.route('/forth/<string:my_id>')
def forte(my_id):
      return f"The page id is {my_id}"







if __name__ == '__main__':

       app.run(debug=True)
       #app.run(debug=True, port=3000)
       # app.run(host= '0.0.0.0', port=8081)