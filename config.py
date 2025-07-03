from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# set values
connection_url = os.getenv("CONNECTION_URL")
dbName = os.getenv("DB_NAME")
colName = os.getenv("COL_NAME")