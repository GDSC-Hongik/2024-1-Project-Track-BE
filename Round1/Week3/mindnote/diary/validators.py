from django.core.exceptions import ValidationError


def validate_no_hash(value):
    if '#' in value:
        raise ValidationError('# 은 포함될 수 없습니다.')


def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('숫자는 들어갈 수 없습니다.')


def validate_score(value):
    if 0 > value or 10 < value:
        raise ValidationError('0부터 10사이의 숫자만 입력 가능합니다.')
