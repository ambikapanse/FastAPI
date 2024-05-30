

from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb+srv://ambikapanse:admin123456@cluster0.stf0qpm.mongodb.net/")
print("connected")



