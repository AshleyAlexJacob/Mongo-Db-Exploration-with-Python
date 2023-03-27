from mongo_connection import information



if __name__=="__main__":
    # simple querying
    # by default gets the first document top one
    print(information.find_one())
    # getting all the records
    print('All the Records For Loop: ')
    for records in information.find({}):
        print(records)
    print('Specific Record: ')
    for records in information.find({'lastname':'Jacob'}):
        print(records)
    




