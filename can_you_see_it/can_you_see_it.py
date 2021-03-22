import re
import cv2


def read_frames(filename):
    cap = cv2.VideoCapture(filename)
    frame_list = []
    ret, frame = cap.read()
    i = 0
    while ret:
        i += 1
        if i % 2:
            frame_list.append(frame.mean())
        ret, frame = cap.read()
    return frame_list


def to_string(frame_list):
    string = [x != 0 for x in frame_list]
    string = ['T' if x else 'A' for x in string]
    return ''.join(string)


if __name__ == '__main__':
    filename = 'Can_You_See_It.mp4'
    frame_list = read_frames(filename)
    string = to_string(frame_list)

    line_len = 719
    # delimiter = 'TTTAT'
    # print(re.sub(delimiter, '\n', string))
    for i, letter in enumerate(string):
        print(letter, end='')
        if not i % line_len:
            print('')
