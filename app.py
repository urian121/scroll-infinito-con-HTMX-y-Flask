from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [f"Item {i}" for i in range(1, 51)]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load-items/<int:start>")
def load_items(start):
    limit = 20
    end = start + limit
    items = ITEMS[start:end]
    has_more = end < len(ITEMS)
    return render_template("items.html", items=items, next_start=end, has_more=has_more)

if __name__ == "__main__":
    app.run(debug=True)
