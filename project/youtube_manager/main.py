import json

def load_videos():
    try:
        with open('database.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_video(videos):
    with open('database.txt','w') as file:
        return json.dump(videos,file)

def add_video(videos):
    name = input("Type video name. ")
    time = input("Type video time. ")
    videos.append({'name':name, 'time':time})
    
    save_video(videos)
    print("Add Video Successful.")
  
def show_all_videos(videos):
    print("*"*50)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video}")
    print("*"*50)
    
def update_video(videos):
    show_all_videos(videos)
    
    index = int(input("Type video index number. To update the index data. "))
    
    if 1 <= index <= len(videos):
        name = input("Type video name. ")
        time = input("Type video time. ")
        videos[index-1] = {'name':name, 'time':time}
        
        save_video(videos)
        print("Update Video Successful.")
    else:
        print("Invalid selection.")

def delete_video(videos):
    show_all_videos(videos)
    
    index = int(input("Select index. To delete the index. "))
    
    if 1 <= index <= len(videos):
        del(videos[index-1])
        
        save_video(videos)
        print("Update Video Successful.")
    else:
        print("Invalid Selection.")

def main():
    videos = load_videos()
    while True:
        print("Youtube Manager || Chose an option")
        print("1. Create a Youtube video. ")
        print("2. List all Youtube videos. ")
        print("3. Update a Youtube video. ")
        print("4. Delete a Youtube video. ")
        print("5. Exit the app. ")
        chose = int(input("Chose your option. "))
        
        match chose:
            case 1:
                add_video(videos)
            case 2:
                show_all_videos(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                exit()
            case _:
                print("Invalid option. Please try a valid number 1-5")
    
if __name__ == "__main__":
    main()