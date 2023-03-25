import pymongo

# initial connection
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# database creation
db = client['Employee']

# collection creation
information = db.employeeinformation

record = [
    {
    'firstname':'Ashley',
    'lastname':'Jacob',
    'department':'Analytics',
},
{
    'firstname':'Raja',
    'lastname':'Ahmed',
    'department':'Cloud',
},
{
    'firstname':'Syed',
    'lastname':'Mohsin',
    'department':'Testing',
},

]

information.insert_many(record)

