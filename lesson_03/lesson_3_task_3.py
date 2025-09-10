from address import Address
from mailing import Mailing

# Создаем адреса с правильным форматированием
to_address = Address(
    "123456",
    "Москва",
    "Ленина",
    "15",
    "25"
)

from_address = Address(
    "654321",
    "Санкт-Петербург",
    "Невский проспект",
    "42",
    "10"
)

mailing = Mailing(to_address, from_address, 250, "TR123456789")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
