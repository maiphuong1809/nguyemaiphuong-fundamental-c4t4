from flask import Flask, render_template
from mongoengine import Document, StringField
class Travel(Document):
    place = StringField()
    image_url = StringField()
    thing_to_do = StringField()
import mlab
app = Flask(__name__)
mlab.connect()
@app.route("/hobby")
def index():
    travel_list = Travel.objects()
    return render_template("travel.html", travels = travel_list)


if __name__ == "__main__":
    app.run(debug = True)