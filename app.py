from flask import Flask, render_template
import threading
import time
from scraper import scrape_right_box, right_box_html

app = Flask(__name__)

def scrape_periodically():
    while True:
        scrape_right_box()
        time.sleep(300)  # 5 minutes

# Start the scraping thread
scrape_thread = threading.Thread(target=scrape_periodically)
scrape_thread.daemon = True
scrape_thread.start()

@app.route('/')
def index():
    return render_template('index.html', right_box_content=right_box_html)

if __name__ == '__main__':
    app.run(debug=True)
