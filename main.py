import os

""" we need compare by content each files! """


def slave_version_control(directory_2, master_file, master_file_path):
    for root, dirs, files in os.walk(directory_2):
        for file in files:
            if master_file == file:
                print(f'We have find the file: {file}')
                slave_file_path = os.path.join(root, file)
                print(os.path.getsize(master_file_path))
                print(os.path.getsize(slave_file_path))
            else:
                print(f'We can not find the file')


def master_version_control(directory_1, directory_2):
    for root, dirs, files in os.walk(directory_1):
        for file in files:
            file_path = os.path.join(root, file)
            slave_version_control(directory_2, file, file_path)







directory_to_walk_1 = 'test_tree_1'
directory_to_walk_2 = 'test_tree_2'
master_version_control(directory_to_walk_1, directory_to_walk_2)
