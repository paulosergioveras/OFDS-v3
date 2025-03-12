# menu.py
class Menu:
    def __init__(self, restaurant):
        self._dishes = {}
        self._restaurant = restaurant

    def _check_owner_permission(self, user):
        if user.id != self._restaurant.owner.id:
            raise PermissionError("Apenas o proprietário do restaurante pode modificar o menu.")

    def add_dish(self, user, dish_name, price):
        self._check_owner_permission(user)
        self._dishes[dish_name] = price

    def update_dish_price(self, user, dish_name, new_price):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            self._dishes[dish_name] = new_price
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def remove_dish(self, user, dish_name):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            del self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def display_menu(self):
        return "\n".join([f"{dish}: R${price:.2f}" for dish, price in self._dishes.items()])
