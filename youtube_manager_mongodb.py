# # import pymongo
# # client = pymongo.MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@youtube-test.6legm.mongodb.net/ytmanager")
# from pymongo import MongoClient
# # client = MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@youtube-test.6legm.mongodb.net/ytmanager")
# #Not good idea to include id and password in the code file
# client = MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@youtube-test.6legm.mongodb.net/", tlsAllowInvalidCertificates=True)
# db = client["ytmanager"]
# #tlsAllowInvalididCertificates=True --->  not a good idea to handle ssl
# video_collection = db["videos"]
# print(client)
# print('*'*20)
# print(video_collection)

# def add_video(name,time):
#     video_collection.insert_one({"name":name, "time":time})


# def list_videos():
#     for video in video_collection.find():
#         print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

# def update_video(id,name,time):
#     video_collection.update_one({'_id':id},{"$set": {"name":name,"time":time}})

# def delete_video(id):
#     video_collection.delete_one({'_id':id})



# def main():
#     while True:
#         print("n Youtube manager app ")
#         print("1. list all videos")
#         print("2. Add new videos")
#         print("3. Update videos")
#         print("4. Delete a videos")
#         print("5. exit the app")

#         choice = input("Enter the choice: ")
#         if choice =='1':
#             list_videos()
        
#         elif choice == '2':
#             name = input("Enter video name: ")
#             time  = input("Enter time of video: ")
#             add_video(name,time)

#         elif choice == '3':
#             id = int(input("Enter the vidoe id which you want to update: "))
#             name = input("Enter the updated video name: ")
#             time  = input("Enter the updated time of video: ")
#             update_video(id,name,time)

#         elif choice == '4':
#             id = int(input("Enter the vidoe id which you want to delete: "))
#             delete_video(id)

#         elif choice == '5':
#             break
        
#         else:
#             raise Exception("Enter the corrrect Choice")








# if __name__ == "__main__":
#     main()




# from pymongo import MongoClient
# from bson import ObjectId
# # Replace `<username>` and `<password>` with your MongoDB credentials
# USERNAME = "your_username"
# PASSWORD = "your_password"

# # Construct the connection URI
# connection_uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@youtube-test.6legm.mongodb.net/ytmanager"

# # Initialize MongoDB client
# try:
#     client = MongoClient(connection_uri, tlsAllowInvalidCertificates=True)
#     db = client["ytmanager"]
#     video_collection = db["videos"]
#     print("Connected to MongoDB successfully!")
# except Exception as e:
#     print(f"Failed to connect to MongoDB: {str(e)}")
#     exit()

# # CRUD operations
# def add_video(name, time):
#     try:
#         video_collection.insert_one({"name": name, "time": time})
#         print("Video added successfully!")
#     except Exception as e:
#         print(f"Failed to add video: {str(e)}")

# def list_videos():
#     try:
#         videos = video_collection.find()
#         if videos.count() == 0:
#             print("No videos found.")
#         for video in videos:
#             print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
#     except Exception as e:
#         print(f"Failed to list videos: {str(e)}")

# def update_video(id, name, time):
#     try:
#         result = video_collection.update_one({'_id': ObjectId(id)}, {"$set": {"name": name, "time": time}})
#         if result.modified_count > 0:
#             print("Video updated successfully!")
#         else:
#             print("No video found with the provided ID.")
#     except Exception as e:
#         print(f"Failed to update video: {str(e)}")

# def delete_video(id):
#     try:
#         result = video_collection.delete_one({'_id': ObjectId(id)})
#         if result.deleted_count > 0:
#             print("Video deleted successfully!")
#         else:
#             print("No video found with the provided ID.")
#     except Exception as e:
#         print(f"Failed to delete video: {str(e)}")

# # Main menu logic
# def main():
#     while True:
#         print("\nYoutube Manager App")
#         print("1. List all videos")
#         print("2. Add new video")
#         print("3. Update video")
#         print("4. Delete video")
#         print("5. Exit the app")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             list_videos()
#         elif choice == '2':
#             name = input("Enter video name: ")
#             time = input("Enter time of video: ")
#             add_video(name, time)
#         elif choice == '3':
#             id = input("Enter the video ID you want to update: ")
#             name = input("Enter the updated video name: ")
#             time = input("Enter the updated time of video: ")
#             update_video(id, name, time)
#         elif choice == '4':
#             id = input("Enter the video ID you want to delete: ")
#             delete_video(id)
#         elif choice == '5':
#             print("Exiting the app. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()




from pymongo import MongoClient

# Replace `<username>` and `<password>` with your MongoDB credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Construct the connection URI
connection_uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@youtube-test.6legm.mongodb.net/ytmanager"

# Initialize MongoDB client
try:
    client = MongoClient(connection_uri, tlsAllowInvalidCertificates=True)
    db = client["ytmanager"]
    video_collection = db["videos"]
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")
    exit()

# CRUD operations
def add_video(name, time):
    try:
        video_collection.insert_one({"name": name, "time": time})
        print("Video added successfully!")
    except Exception as e:
        print(f"Failed to add video: {str(e)}")

def list_videos():
    try:
        if video_collection.count_documents({}) == 0:
            print("No videos found.")
            return
        videos = video_collection.find()
        for video in videos:
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    except Exception as e:
        print(f"Failed to list videos: {str(e)}")

def update_video(id, name, time):
    try:
        result = video_collection.update_one({'_id': id}, {"$set": {"name": name, "time": time}})
        if result.modified_count > 0:
            print("Video updated successfully!")
        else:
            print("No video found with the provided ID.")
    except Exception as e:
        print(f"Failed to update video: {str(e)}")

def delete_video(id):
    try:
        result = video_collection.delete_one({'_id': id})
        if result.deleted_count > 0:
            print("Video deleted successfully!")
        else:
            print("No video found with the provided ID.")
    except Exception as e:
        print(f"Failed to delete video: {str(e)}")

# Main menu logic
def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter time of video: ")
            add_video(name, time)
        elif choice == '3':
            id = input("Enter the video ID you want to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated time of video: ")
            update_video(id, name, time)
        elif choice == '4':
            id = input("Enter the video ID you want to delete: ")
            delete_video(id)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
