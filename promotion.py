# promotion.py
class Promotion:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self._promotions = {}

    def _check_owner_permission(self, user):
        from users import Owner
        if not isinstance(user, Owner):
            raise PermissionError("Apenas proprietários podem adicionar, atualizar ou remover promoções.")

    def add_promotion(self, user, code, value):
        self._check_owner_permission(user)
        if code in self._promotions:
            raise ValueError(f"Promoção com código '{code}' já existe.")
        self._promotions[code] = value

    def update_promotion(self, user, code, new_value):
        self._check_owner_permission(user)
        if code in self._promotions:
            self._promotions[code] = new_value
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def remove_promotion(self, user, code):
        self._check_owner_permission(user)
        if code in self._promotions:
            del self._promotions[code]
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def apply_promotion(self, code, total_amount):
        if code in self._promotions:
            return total_amount - (total_amount * self._promotions[code])
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def display_promotions(self):
        return "\n".join([f"{code}: {value * 100}% de desconto" for code, value in self._promotions.items()])
