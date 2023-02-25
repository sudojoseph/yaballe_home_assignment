VALID_SOURCES = ('amazon', 'walmart')


def has_min_length(name, value, length):
    if len(value) < length:
        raise ValueError(f'{name} must be at least {length} characters long')
    return value


def validate_source(source):
    if source not in VALID_SOURCES:
        raise ValueError('source must be amazon or walmart')
    return source