from django.core.exceptions import ValidationError


def validate_title(title):
    if len(title.split(" ")) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


if __name__ == "__main__":
    validate_title('Duas palavras')
    validate_title("PalavraUnica")
