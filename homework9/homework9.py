import re

def split_email(email):
  """
  Разделяет email на имя пользователя и доменное имя.

  Args:
    email: Строка, содержащая email адрес.

  Returns:
    Словарь с ключами "username" и "domain", содержащий имя пользователя и доменное имя.
  """
  match = re.match(r"^(.+?)@(.+)$", email)
  if match:
    return {"username": match.group(1), "domain": match.group(2)}
  else:
    return {"username": None, "domain": None}

if __name__ == "__main__":
  email = input("Введите email адрес: ")
  result = split_email(email)
  if result["username"]:
    print(f"Имя пользователя: {result['username']}")
    print(f"Доменное имя: {result['domain']}")
  else:
    print("Некорректный формат email адреса.")
