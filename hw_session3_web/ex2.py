from mongoengine import*

class Post(Document):
    title=StringField()
    author=StringField()
    content=StringField()
    meta = {'collection':'posts'}

import mlab
mlab.connect()
music_list = Post(title = 'Let Myself Try',author = 'Jasmine Thompson,post by mai phuong',
content = """It's alright cause in time i'll be fine
I'm gonna let myseft,let myself
Fall once or twice, I won't mind
i'm gonna let myself, let myself
Fail and discover cause one what or another
I'll be fine, it's alright in this life
I'm gonna let myself, let myself try""")

music_list.save()