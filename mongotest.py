import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://mohnal:Swapnil123@cluster0.d0jajzj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']   #collections=coll
coll.insert_one(d )