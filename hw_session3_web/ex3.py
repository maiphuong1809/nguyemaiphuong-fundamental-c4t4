from mongoengine import *

import mlab

class Customers(Document):
    name = StringField()
    age = IntField()
    address = StringField()
    ref = StringField()
    meta = {'collection':'customers'}
mlab.connect()
ads_count=len(Customers.objects(ref__icontains="ads"))
event_count=len(Customers.objects(ref__icontains="event"))
word_of_mouth_count=len(Customers.objects(ref__icontains="word of mouth"))

