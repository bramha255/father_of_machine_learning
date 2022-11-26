import shutil
import os


path = os.path.join('.')
pdf_fol = os.path.join(path, 'pdf_fol')
img_fol = os.path.join(path, 'img_fol')
zip_fol = os.path.join(path, 'zip_fol')
video_fol = os.path.join(path, 'video_fol')
py_fol = os.path.join(path, 'py_fol')
gif_fol = os.path.join(path, 'gif_fol')
docs_fol = os.path.join(path, 'docs_fol')
exe_fol = os.path.join(path, 'exe_fol')
mis_fol = os.path.join(path, 'miscellaneous_fol')

diff_type = [('.jpg', img_fol), ('.pdf', pdf_fol), ('.zip', zip_fol),
             ('.mp4', video_fol),
             ('.gif', gif_fol), ('.py', py_fol), ('.exe', exe_fol),
             ('.docx', docs_fol), ('.png', img_fol), ('.rar', zip_fol), ('.mkv', video_fol)]

f = [i for i in os.listdir() if 'c_drive_' in i]


for i in range(len(f)):
    different_folder = os.path.join(path, f[i])
    # print('FOLDER:{}'.format(different_folder))
    for file_type, folder in diff_type:

        files = [f for f in os.listdir(different_folder) if file_type in f.lower()]

        # print(files)

        folder = os.path.join(different_folder, folder)

        if not os.path.exists(folder):
            os.mkdir(folder)

        for file in files:
            # print(file)
            file = os.path.join(different_folder, file)
            new_path = os.path.join(folder)
            shutil.move(file, new_path)
            # print(
            #     f"'FOLDER: {different_folder}, SRC: {file}, DEST: {new_path}")
