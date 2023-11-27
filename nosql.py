#-----------------------------code 1-------------------------------------
class simplenosqldb:
    def __init__(self):
        self.data={}

    def insert(self,key,value):
        if key in self.data:
            print(f"Key '{key}' already exists. updating value")
        self.data[key]=value
        print (f"Inserted :{key}- {value}")

    def get (self,key):
        return self.data.get(key)

    def delete (self,key):
        if key in self.data:
            del self.data[key]
            print (f"deleted {key}")
        else:
            print(f"Key {key}' not found")

    def display (self):
        print("All key value")
        for key,value in self.data.items():
            print(f"{key}:{value}")

db = simplenosqldb()

db.insert("001",{"name":"gowtham","age":30,"city":"chennai"})
db.insert("002",{"name":"nandhu","age":28,"city":"bangalore"})
db.insert("003",{"name":"saro","age":31,"city":"chennai","salary":5000})

print("Get '001':", db.get("001"))
print("Get '002':", db.get("002"))

db.display()

db.delete("003")
db.display()



#-----------------------------code 2-------------------------------------
parent_dic={}

dict1={"name":"gowtham","age":30,"city":"chennai"}
dict2={"name":"nadhu","age":28,"city":"chennai","salary":3000}

parent_dic['user1']=dict1
parent_dic['user2']=dict2

user_data1=parent_dic['user1']
user_data2=parent_dic['user2']


print("user1:",user_data1)
print("user2:",user_data2.get("salary"))


#                 table_name colum = value
def find_records (collection,key,value):
    matching_record=[]
    for user,user_data in collection.items():
        if key in user_data and user_data[key]==value:
                matching_record.append((user,user_data))
    return matching_record


matching_record = find_records(parent_dic,'age',28)

print ("matching records....")
for user,user_data in matching_record:
    print(f"{user}:{user_data}")
