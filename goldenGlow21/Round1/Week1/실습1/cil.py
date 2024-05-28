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
            line += '\n'
            f.write(line)


# 이미지를 디스플레이해 주는 함수
def display(img):
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            print(img[i][j], end=' ')
        print()


# 이미지 색상 반전
def invert(img):
    # img 이미지 크기
    height, width = len(img), len(img[0])

    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = invert_bit(img[i][j])

    return new_img


# -1로 채워진 새로운 이미지 생성
def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([-1] * width)
    return new_img


# 비트 반전
def invert_bit(bit):
    return 1 - bit