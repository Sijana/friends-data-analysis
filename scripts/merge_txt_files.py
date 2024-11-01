import os

def get_dir_files(dir):
    all_files = os.listdir(dir)
    txt_files = []
    for file in all_files:
        full_path = os.path.join(dir, file)
        if file.find(".txt") != -1:
            txt_files.append(full_path)
        else:
            pass
    txt_files.sort()
    
    return txt_files

def merge_txt(all_files, file_path):
    with open(file_path, "w") as outfile:
        for file in all_files:
            with open(file) as infile:
                outfile.write(infile.read() + "\n")

def main():
    dir_path = "friends_episodes"
    file_path = "output/friends.txt"
    all_files = get_dir_files(dir_path)
    merge_txt(all_files, file_path)


if __name__ == "__main__":
    main()