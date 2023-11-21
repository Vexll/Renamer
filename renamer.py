import os


def target_files(path):
    files = os.listdir(path)
    videos_files = []
    subtitle_files = []
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension == '.mp4':
            videos_files.append(file)
        elif extension == '.srt':
            subtitle_files.append(file)
    videos_files.sort()
    subtitle_files.sort()
    return videos_files, subtitle_files


v_files, title_files = target_files(os.getcwd())

if len(v_files) != len(title_files):
    print("check your videos and subtitles!")
    quit()

for i in range(len(v_files)):
    target_name, video_extension = os.path.splitext(v_files[i])
    subtitle_name = target_name + '.srt'
    os.rename(title_files[i], subtitle_name)
