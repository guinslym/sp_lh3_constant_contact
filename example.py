from sp_lh3_constant_contact import check_operator_response
from pprint import pprint as tprint


def main():
    chat_ids = [3423927, 3423928, 3423929]  # List of chat IDs to test
    for chat_id in chat_ids:
        result = check_operator_response(chat_id)
        if result:
            tprint(result)


if __name__ == "__main__":
    main()
