import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "8206404")

API_HASH = os.environ.get("API_HASH", "e935d9b56e3fd2c05c743093efb761c9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6244445444:nhs6sgvhh6776gfnhsb4asas1aNbb") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001659284209") 

DB_NAME = os.environ.get("DB_NAME","Aman")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Aman:<Aman>@cluster0.md9wv.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/1f615f51ae3aa7dcdb7dc.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '858588280').split()]

