import os

def list_files(startpath):

    with open("folder_structure.txt", "w") as f_output:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = '\t' * 1 * (level)
            output_string = '{}{}/'.format(indent, os.path.basename(root))
            print(output_string)
            f_output.write(output_string + '\n')
            subindent = '\t' * 1 * (level + 1)
            for f in files:
                output_string = '{}{}'.format(subindent, f)
                print(output_string)
                f_output.write(output_string + '\n')

list_files(".")