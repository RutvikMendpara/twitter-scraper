from flask import Flask, render_template , request
import snscrape.modules.twitter as sntwitter
app = Flask(__name__)

# result page
@app.route('/result', methods=['GET', 'POST'])
def result():
    try:
        if request.method == 'POST':
            def get_user_id(username: str):
                user = next(sntwitter.TwitterSearchScraper(f'from:{username}').get_items())
                return user.user.id
            username = request.form["username"]
            user_id = get_user_id(username)
    except:
        return render_template('error.html')
    return render_template('result.html' , username = username, user_id = user_id )

# index page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)