from django.core.exceptions import ValidationError

def validate_symbol(value):
    if ("@" in value)or ("#" in value) or("&" in value) :
        raise ValidationError("'@'와 '#'과 '&'은 사용 불가합니다.",code='symbol-error')