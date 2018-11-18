# render_template for displaying the html (rendering the html), request is going to get the information (content by the user)
from flask import Flask, render_template, request
# security to prevent certain things like side line scripting
from flask_cors import CORS
# importing get_posts from models
from models import create_post, get_posts

# creating the server object with the name of app
app = Flask(__name__)

CORS(app)

# decide what data to send back to the frontend for especific functions. Methods are going to be get, post, delet, put(update)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    # user is posting information into an input field
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    # everytime the user updates with a new post it'll be updated
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
