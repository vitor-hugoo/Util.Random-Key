import random
import string

def generate_secret_key(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=False):
    """
    Generate a secret key/password based on the given parameters.

    Parameters:
        length (int): Length of the key/password (default is 16).
        use_uppercase (bool): Whether to include uppercase letters (default is True).
        use_lowercase (bool): Whether to include lowercase letters (default is True).
        use_digits (bool): Whether to include digits (default is True).
        use_symbols (bool): Whether to include symbols (default is False).

    Returns:
        str: Generated secret key/password.
    """
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character set must be selected.")

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a secret key/password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the key/password (default is 16).")
    parser.add_argument("-u", "--use_uppercase", action="store_true", help="Include uppercase letters.")
    parser.add_argument("-w", "--use_lowercase", action="store_true", help="Include lowercase letters.")
    parser.add_argument("-d", "--use_digits", action="store_true", help="Include digits.")
    parser.add_argument("-s", "--use_symbols", action="store_true", help="Include symbols.")

    args = parser.parse_args()

    try:
        secret_key = generate_secret_key(
            length=args.length,
            use_uppercase=args.use_uppercase,
            use_lowercase=args.use_lowercase,
            use_digits=args.use_digits,
            use_symbols=args.use_symbols
        )
        print("Generated Secret Key/Password:", secret_key)
    except ValueError as ve:
        print("Error:", ve)
