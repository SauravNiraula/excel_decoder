def validate_max_min(max, min):
    def wrapper(value):
        print(max, min, value)
        if value < min or value > max:
            return 1
        else:
            return 0
    return wrapper


wrap = validate_max_min(100, 12)
print(wrap(40))