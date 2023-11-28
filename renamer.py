import os


def target_files(path):
    files = os.listdir(path)  # put everything in a folder in a list
    videos_files = []
    subtitle_files = []
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension == '.mp4' or extension == '.mkv':  # checking videos
            videos_files.append(file)
        elif extension == '.srt' or extension == '.ass':  # checking subtitles
            subtitle_files.append(file)
    videos_files.sort()
    subtitle_files.sort()
    return videos_files, subtitle_files    # return both lists


v_files, title_files = target_files(os.getcwd())

if len(v_files) != len(title_files):
    print("check your videos and subtitles!")
    quit()

for i in range(len(v_files)):
    video_name, video_extension = os.path.splitext(v_files[i])
    subtitle_name, subtitle_extension = os.path.splitext(title_files[i])
    target_name = video_name + subtitle_extension

    os.rename(title_files[i], target_name)
