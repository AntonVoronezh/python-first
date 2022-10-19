import os

tree = os.walk('folder')
# print(tree)

for file in tree:
    # print(file)
    pass


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, files)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        sub_indent = ' ' * 4 * (level+1)
        # print(level)
        print(f'{indent} [{os.path.basename(root)}]')
        for file in files:
            print(f'{sub_indent} {file}')


read_dir('folder')