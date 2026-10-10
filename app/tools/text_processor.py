def process_text(text: str, operation: str) -> str | int:

    if operation == "uppercase":
        return text.upper()

    elif operation == "lowercase":
        return text.lower()

    elif operation == "word_count":
        return len(text.split())

    else:
        raise ValueError("Invalid text operation")