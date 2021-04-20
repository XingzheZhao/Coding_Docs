# dealing with small files

# f = open('test.txt', 'r')

# print(f.read())
# f.close()

"""
with open('test.txt', 'r') as f:
    # file_content = f.read()
    # file_content = f.readlines()  # ? list
    # file_content = f.readline()  # ? one line at a time
    # print(file_content, end='')

    # ! to solve memory issue
    # for line in f:
    #     print(line, end='')

    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f.tell()) # ? check current position
    print(f_content)
    f.seek(0)
    f_content = f.read(size_to_read)
    print(f_content)
    # while len(f_content) > 0:
    #     print(f_content, end='')
    #     f_content = f.read(size_to_read)

with open('test2.txt', 'w') as f:
    f.write('testing123')
    f.seek(0)
    f.write('NewTest')
"""

with open('test.txt', 'r') as rf:
    with open('testcopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# ! in order to read and write a image, use 'rb' instead of 'r'

with open('beatles.jpg', 'rb') as rf:
    with open('beatlescopy.jpg', 'wb') as wf:
        size_of_write = 2048
        image_content = rf.read(size_of_write)
        while len(image_content) > 0:
            wf.write(image_content)
            image_content = rf.read(size_of_write)