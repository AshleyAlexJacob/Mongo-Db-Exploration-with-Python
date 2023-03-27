from mongo_connection import information

if __name__ == "__main__":
    print('Employees in Testing or Cloud')
    for record in information.find({'department':{'$in':['Cloud','Testing']}}):
        print(record)
    print('AND Operator')
    for record in information.find({'$and':[{'firstname':'Krish'},{'department':'Testing'}]}):
        print(record)
    
