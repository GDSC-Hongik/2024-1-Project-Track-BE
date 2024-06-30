from django.core.exceptions import ValidationError


def validate_symbols(value):
    if('@' in value) or ('#' in value) or ('&' in value):
        raise ValidationError('"@", "#, "&"는 포함될 수 없습니다.')
