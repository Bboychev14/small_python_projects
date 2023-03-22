class Validator:
    @staticmethod
    def raise_if_string_is_null_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_age_is_less_than_16(number, message):
        if number < 16:
            raise ValueError(message)

    @staticmethod
    def raise_if_genre_is_invalid(string, message):
        if string not in ["Metal", "Rock", "Jazz"]:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_less_than_one(number, message):
        if number < 1:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_less_than_zero(number, message):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_place_is_invalid(string, message):
        if string.strip() == '' or len(string) < 2:
            raise ValueError(message)