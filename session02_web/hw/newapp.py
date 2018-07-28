from flask import Flask,redirect

newapp = Flask(__name__)
Users = {
        'huy' :         {
                'name' : 'Nguyen Quang Huy',
                'age' : 29
        },
        'don' : {
                "name" : 'Don zoombie',
                'age' : 23
        },
        'phuong' : {
                'name' : "Nguyen Mai Phuong",
                'age' : 16
        }
    }
def user_profile(username,Users):
    return_informations= ""
    if username in Users:
        for profile in Users[username]:
            return_informations += str(profile)
            return_informations += ":"
            return_informations += str(Users[username][profile])
            return_informations += "<br/>"
        return return_informations    
    else:
        return None    

print()
@newapp.route("/")
def index():
    return "Hello C4T4, this is homepage"

@newapp.route("/about-me/")
def about_me():
    return """
    A bit about me(the developer):
    Hello, my name is Nguyen Mai Phuong or some people call me MP.
    I am 15 years old when i develop this website.
    I am studying at grade 11 at HN-Amsterdam high school for the gifted.
    I like sports and watching films"""
@newapp.route("/school")
def school():
    return redirect("http://techkids.vn")
 
@newapp.route("/user/<username>")
def profile(username):
    printing=user_profile(username,Users)
    if printing is not None:
        return printing
    else:
        return "User not found"    


if __name__ == "__main__":
    newapp.run(debug=True)

