import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

#create table 
cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
            video_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )              
''')

# add video
def add_video(name,time):
    cursor.execute('INSERT INTO videos (name,time) VALUES(?, ?)',(name, time))
    conn.commit()
    
# show all video
def show_all_videos():
    cursor.execute('SELECT * FROM videos')
    print("*" * 50)
    for row in cursor.fetchall():
        print(row)
    print("*" * 50)
    
# update a video
def update_video(new_name,new_time,video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE video_id = {video_id}", (new_name, new_time, video_id))
    conn.commit()
    
# delete a video
def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE video_id = ?', (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager by sqlite3")
        print("1. Create a video.")
        print("2. See all videos lists.")
        print("3. Update a video.")
        print("4. Delete a video.")
        print("5. Exit the app.")
        
        choice = input("chose an option to action. ")
        
        match choice:
            case '1':
                 name = input("Type video name. ")
                 time = input("Type video time. ")
                 
                 add_video(name,time)
                 
                 print("Data added successful.")
                 
            case '2':
                show_all_videos()
            case '3':
                 show_all_videos()
                 
                 video_id = int(input("Type video id to update. "))
                 name = input("Type a video name. ")
                 time = input("Type video time. ")
                
                 update_video(video_id,name,time)
                 print("Data update successful.")
                
            case '4':
                 show_all_videos()
                 
                 video_id = int(input("Type video id to delete. "))
                
                 delete_video(video_id)
                 print("Data delete successful.")
                
            case '5':
                break
            case _:
                print("Invalid Selection.")
                
                
        #conn.close()      

if __name__ == "__main__":
    main()