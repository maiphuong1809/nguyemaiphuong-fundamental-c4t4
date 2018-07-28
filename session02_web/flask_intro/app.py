# 1 Create a flask app
from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self,t,c,tu):
        self.title = t
        self.cast = c
        self.thumbnail_url = tu

m = Movie("The Avengers 3: Infinity War",
"Robert Downey Jr., Chris Hemsworth, Mark Ruffalo, Chris Evans, Scarlett Johansson, Benedict Cumberbatch, Don Cheadle, Tom Holland, Chadwick Boseman, Paul Bettany, Elizabeth Olsen, Anthony Mackie, Sebastian Stan, Danai Gurira, Letitia Wright, Dave Bautista, Zoe Saldana, Josh Brolin, and Chris Pratt",
"http://t0.gstatic.com/images?q=tbn:ANd9GcRmE2vwxy5KaCu7cRuYYdgNdQKddux5OYgGwsPo0kqP_xzLnsDV")
m2 = Movie("Ant-man and the wasp",
"Paul Rudd, Evangeline Lilly",
"http://t1.gstatic.com/images?q=tbn:ANd9GcQeA9IA-C1GiNpVwEXXm-jcFOFpuYvjd-n30RmAtSs8511N2NMi")
m3 = Movie("Thor:ragnarok ",
"Chris Hemsworth,Tom Hiddleston,Cate Blanchett",
"http://t3.gstatic.com/images?q=tbn:ANd9GcST1uigGrukMvSAVUefFNuQ0NMZAR-FjfFIwSZFCR5ZkyMSgCyj")
movies_list = [m,m2,m3]


class Travel:
    def __init__(self,place,location_url,things_to_do):
        self.place = place
        self.location_url = location_url
        self.things_to_do = things_to_do

p1 = Travel("Bali,Indonesia",
"https://e3.365dm.com/18/04/1096x616/skynews-bali-file-picture_4291521.jpg?20180424141409",
"visit the Uluwatu Temple,the Sanur village,and many more")
p2 = Travel("PhuKet,Thailand",
"http://static.asiawebdirect.com/m/phuket/portals/phuket-com/shared/teasersL/TOP10/10-best-tours/teaserMultiLarge/imageHilight/best-tours-phuket-L.jpg",
"enjoying the beaches,travel on tuk tak,visit Phi Phi island, eat seafood,...")
p3 = Travel("Jeju island,South Korea",
"https://jingtravel.com/wp-content/uploads/2018/01/shutterstock_673524259-e1515141234641.jpg",
"travel through Lava tubes in  Manjang cave,visiting Grandfather stones,eating abundants of food,travel along beach coast and walk trial")
p4 = Travel ("Hanoi,Vietnam",
"http://vietnamopentour.com.vn/timthumb.php?src=http://vietnamopentour.com.vn/images/tour/352/352_7.jpg&w=500&h=320",
"eating amazing street food, visit sightseeing places like Hoan Kiem lake,Quoc Tu Giam,travel through the old street in xich lo cart")
p5 = Travel ("Singapore,Singapore",
"https://cdn1.i-scmp.com/sites/default/files/styles/2000x792/public/images/methode/2017/07/29/78d57198-7373-11e7-9a9a-a7d2083b6658_4000x1584_121355.JPG?itok=LSKFQpyg",
"visit Sentosa amusement park,singapore science museum,the lion head statue,...")
travel_places = [p1,p2,p3,p4,p5]
@app.route("/")
def index():
    return render_template("index.html",
    name=" Alex",
    image_url="https://i.pinimg.com/564x/3f/79/8f/3f798f16f3cd243879c8c9cc708c8cee.jpg") 

@app.route("/about-me")
def about_me():
    return """
    A bit about me(the developer):
    Hello, my name is Nguyen Mai Phuong or some people call me MP.
    I am 15 years old when i develop this website.
    I am studying at grade 11 at HN-Amsterdam high school for the gifted """
@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name
@app.route("/casts")
def casts():
    return render_template("cast.html",casts=["Anne Hathaway","Alexandra Daddario","Anna Kendrick"])
@app.route("/movie")
def movie():
    return render_template("movie.html",movies = movies_list)
@app.route ("/travel")
def travel():
    return render_template("travel.html",travels = travel_places)
# 2 Run app
if __name__ == "__main__":
    app.run(debug=True)