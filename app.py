from flask import Flask, render_template
from fetcher import fetch_data
from processor import process_data

app = Flask(__name__)

@app.route('/citations', methods=['GET'])  
def get_citations():
    data = fetch_data()
    processed_data = process_data(data)
    return render_template('citations.html', citations=processed_data)

if __name__ == "__main__":
    app.run(debug=True)
