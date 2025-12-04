from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name='James')

@app.route("/<name>")
def hello(name):
    return render_template("index.html", name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

# Type available
#
# string (default) accepts any text without a slash
# int accepts positive integers
# float accepts positive floating point values
# path like string but also accepts slashes
# uuid accepts UUID strings

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# instead of defining two route like @app.get('/login') and @app.post('/login'),
# we put them under one function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
   return 'Do the login!'

def show_the_login_form():
    return render_template('login.html')

if __name__ == '__main__':
    
    # url_for example
    # Instead of putting the path directly like /hello_admin, we use url_for('<name of the function>')
    #
    # @app.route('/user/<name>')
    # def hello_user(name):
    #     if name =='admin':
    #         return redirect(url_for('hello_admin'))
    #     else:
    #         return redirect(url_for('hello_guest',guest = name))
    
    with app.test_request_context():
        print(url_for('home'))
        print(url_for('login'))
        print(url_for('hello', name='James'))
        print(url_for('login', next='/'))
        print(url_for('show_subpath', subpath='/'))
        print(url_for('show_post', post_id='1'))
        print(url_for('show_user_profile', username='John Doe'))
        
    app.run(debug=True)