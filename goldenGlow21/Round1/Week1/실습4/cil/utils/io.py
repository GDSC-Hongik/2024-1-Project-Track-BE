# 이미지를 파일에서 읽어오는 함수
def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img


# 이미지를 파일에 저장해 주는 함수
def save_image(img, filepath):
    with open(filepath, 'w') as f:
        for row in img:
            line = ''
            for bit in row:
                line += str(bit)
            line += '\\\\\\\\n'
            f.write(line)
