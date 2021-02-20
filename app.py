from flask import Flask, render_template, request #import the library
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__) #create flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


#creating real database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)

#data
# all_posts = [
#     {
#         'title': 'post 1',
#         'content': 'content 1. oohoooo',
#         'Author' : 'madiha'
#     },
#     {
#         'title': 'post 2',
#         'content': 'content 2. wohoooo',
#     }
# ]

#@app.route('/home/users/<string:name>/posts/<int:id>') [DYNANMIC URL]
#localhost:5000/home/users/madiha/posts/20
#def hello(name, id):
#    return "hello," + name + ", your id is: " + str(id) ---> hello,madiha, your id is: 20

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST']) #POST method for the new post you add
def posts():
    #if request.method == 'POST': #this will add the added post to existing database
      #  post_title = request.form['title'] #storing the input of title in post_title
      #  post_content = request.form['content'] ##storing the input of content in post_content
      #  new_post = BlogPost(title= post_title, content= post_content, Author= 'madiha') 
      #  db.session.add(new_post) #add new_post to database in the current session
      #  db.session.commit() #now only the database will be saved permanantely
      #  return redirect('/posts') #redirect back to same page 
    #else:
        #all_posts= BlogPost.query.order_by(BlogPost.date_posted).all() #getting all the blog posts and arranging them acc to date posted
    return render_template('posts.html', posts= all_posts) #just return the already present database

if __name__ == "__main__":
    app.run(debug=True)
