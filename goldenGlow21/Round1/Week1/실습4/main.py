import cil

logo = cil.read_image('codeit_logo')
text = cil.read_image('codeit_text')

# logo를 상하 반전해서 upside_down_logo에 저장해 주세요 
upside_down_logo = cil.vertical_flip(logo)
# text를 좌우 반전해서 reversed_text에 저장해 주세요
reversed_text = cil.horizontal_flip(text)

print('코드잇 로고:')
cil.display(logo)
print('\n상하 반전된 로고:')
cil.display(upside_down_logo)

print('\n코드잇 텍스트:')
cil.display(text)
print('\n좌우 반전된 텍스트:')
cil.display(reversed_text)

# 테스트 코드
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge', 'horizontal_flip', 'vertical_flip']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(cil) for x in key_functions))
print(not any(x in dir(cil) for x in non_key_functions))