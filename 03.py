import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "38050 111&& 22$$ 11   ",
    "38050 111&& 22$$ 11~!@#$%^&*()_'   ",
]


def normalize_phone(phone_number: str) -> str:
    clean_pattern = re.compile(r"[^0-9+]")
    normalized_phone = re.sub(clean_pattern, "", phone_number)

    check_prefix_pattern = re.compile(r"\+?38\d+")

    if not re.search(check_prefix_pattern, normalized_phone):
        normalized_phone = "+38" + normalized_phone

    if not normalized_phone.startswith("+"):
        normalized_phone = "+" + normalized_phone

    return normalized_phone


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
