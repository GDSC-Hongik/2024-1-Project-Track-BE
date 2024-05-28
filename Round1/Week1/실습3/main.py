import cil

logo = cil.read_image('codeit_logo')
text = cil.read_image('codeit_text')

print('코드잇 로고:')
# logo를 디스플래이해 주세요
cil.display(logo)
print('\n코드잇 텍스트:')
# text를 디스플래이해 주세요
cil.display(text)

# text를 색상 반전해서 inverted_text 변수에 할당해 주세요
inverted_text = cil.invert(text)
# logo와 text를 합성한 이미지를 merged_img 변수에 할당해 주세요
merged_img = cil.merge(logo, text)

print('\n색상 반전 텍스트:')
# inverted_text를 디스플래이해 주세요
cil.display(inverted_text)
print('\n합성 이미지:')
# merged_img를 디스플래이해 주세요
cil.display(merged_img)

# 테스트 코드
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(cil) for x in key_functions))
print(not any(x in dir(cil) for x in non_key_functions))