import ptt_mac_shop
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get():
    product_list = ptt_mac_shop.get_product()
    return render_template('page.html', product_list=product_list)


app.run()
