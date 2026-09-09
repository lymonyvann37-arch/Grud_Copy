from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def index_product():
    return render_template('Products/index.html')

if __name__ == "__main__":
    app.run(debug=True)