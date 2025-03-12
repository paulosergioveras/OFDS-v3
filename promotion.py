# promotion.py
class Promotion:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self._promotions = {}  # Dicionário para armazenar promoções: {código: valor}

    def _check_owner_permission(self, user):
        """Verifica se o usuário é um Owner."""
        from users import Owner  # Importação local para evitar circularidade
        if not isinstance(user, Owner):
            raise PermissionError("Apenas proprietários podem adicionar, atualizar ou remover promoções.")

    def add_promotion(self, user, code, value):
        """Adiciona uma promoção."""
        self._check_owner_permission(user)
        if code in self._promotions:
            raise ValueError(f"Promoção com código '{code}' já existe.")
        self._promotions[code] = value

    def update_promotion(self, user, code, new_value):
        """Atualiza o valor de uma promoção."""
        self._check_owner_permission(user)
        if code in self._promotions:
            self._promotions[code] = new_value
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def remove_promotion(self, user, code):
        """Remove uma promoção."""
        self._check_owner_permission(user)
        if code in self._promotions:
            del self._promotions[code]
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def apply_promotion(self, code, total_amount):
        """Aplica uma promoção ao valor total."""
        if code in self._promotions:
            return total_amount - (total_amount * self._promotions[code])
        else:
            raise ValueError(f"Promoção com código '{code}' não encontrada.")

    def display_promotions(self):
        """Exibe as promoções."""
        return "\n".join([f"{code}: {value * 100}% de desconto" for code, value in self._promotions.items()])
