# menu.py
class Menu:
    def __init__(self, restaurant):
        self._dishes = {}  # Atributo privado
        self._restaurant = restaurant  # Referência ao restaurante

    def _check_owner_permission(self, user):
        """Verifica se o usuário é o proprietário do restaurante."""
        if user.id != self._restaurant.owner.id:
            raise PermissionError("Apenas o proprietário do restaurante pode modificar o menu.")

    def add_dish(self, user, dish_name, price):
        """Adiciona um prato ao menu."""
        self._check_owner_permission(user)
        self._dishes[dish_name] = price

    def update_dish_price(self, user, dish_name, new_price):
        """Atualiza o preço de um prato."""
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            self._dishes[dish_name] = new_price
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def remove_dish(self, user, dish_name):
        """Remove um prato do menu."""
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            del self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def display_menu(self):
        """Exibe o menu."""
        return "\n".join([f"{dish}: R${price:.2f}" for dish, price in self._dishes.items()])
