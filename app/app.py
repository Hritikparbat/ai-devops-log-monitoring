from flask import Flask
import logging
import random
import time

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():

    value = random.randint(1,10)

    if value > 8:
        logging.error("Application error occurred")
    else:
        logging.info("Application running normally")

    return "AI DevOps Monitoring App Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)