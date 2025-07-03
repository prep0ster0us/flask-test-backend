from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from config import connection_url, dbName, colName

client = None
db = None
userTable = None

#CALL BEFORE RUNNING ANY OPERATIONS
def init_db():
	global client, db, userTable
	client = MongoClient(connection_url)
	db = client.get_database(dbName)
	print("Connected to db: ", dbName)
	userTable = db.users

def get_all_users():
	users = list(db.users.find())
	return {
		"users": users,
		"message": "users retrieved successfully"
	}

def add_user(user):
	user_id = db.users.insert_one(user).inserted_id
	return {
		"_id": str(user_id),
		"message": "User added successfully"
	}

def delete_user(user_id):
	try:
		result = db.users.find_one_and_delete({
			"_id": ObjectId(user_id)
		})
		if result:
			print("Deleted User: ", result.first_name)
			return {
				"_id": str(result._id),
				"message": "User deleted successfully"
			}
	except Exception as err:
		print("Error deleting user: ", err)
		return {
			"message": f"ERROR deleting user: {err}"
		}
	
def update_user(user_id, field, value):
	try:
		result = db.users.update_one(
			{"_id": ObjectId(user_id)},		# filter the record to update
			{field: value}					# update to be made
		)
		if result.matched_count == 0:
			print("No such user found!")
			return {
				"message": "No such user!"
			}
		elif result.modified_count == 0:
			print(f"Couldn't modify {field}")
			return {
				"message": f"Couldn't modify {field}!"
			}
		else:
			print(f"user {user_id}'s {field} updated to {value}")
			return {
				"message": f"user {user_id}'s {field} updated to {value}"
			}
	except Exception as err:
		print(f"ERROR updating user: {err}")
		return {
			"message": f"Couldn't update user: {err}"
		}

# def insert_user_db(user_dict):
# 	result = db.users.insert_one(user_dict)
# 	return {"id": str(result.inserted_id), "message": "User created successfully"}

def find_user_by_name_db(first_name):
	user = db.users.find_one({"first_name": first_name})
	return {
		"_id": user._id,
		"message": f"user {first_name} found in db"
	}