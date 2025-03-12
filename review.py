class Review:
    def __init__(self):
        self._reviews = {}  # Dicionário para armazenar avaliações

    def _check_customer_permission(self, user):
        """Verifica se o usuário é um Customer."""
        from users import Customer  # Importação local para evitar circularidade
        if not isinstance(user, Customer):
            raise PermissionError("Apenas clientes podem adicionar, atualizar ou deletar avaliações.")

    def add_review(self, user, review_text, rating):
        """Adiciona uma avaliação."""
        self._check_customer_permission(user)
        if user.id in self._reviews:
            raise ValueError("Usuário já avaliou este restaurante.")
        self._reviews[user.id] = {"review": review_text, "rating": rating}

    def update_review(self, user, new_review_text, new_rating):
        """Atualiza uma avaliação existente."""
        self._check_customer_permission(user)
        if user.id in self._reviews:
            self._reviews[user.id] = {"review": new_review_text, "rating": new_rating}
        else:
            raise ValueError("Avaliação não encontrada.")

    def delete_review(self, user):
        """Remove uma avaliação."""
        self._check_customer_permission(user)
        if user.id in self._reviews:
            del self._reviews[user.id]
        else:
            raise ValueError("Avaliação não encontrada.")

    def get_average_rating(self):
        """Calcula a média das avaliações."""
        if not self._reviews:
            return 0
        total_ratings = sum(review["rating"] for review in self._reviews.values())
        return total_ratings / len(self._reviews)

    def display_reviews(self):
        """Exibe as avaliações."""
        return "\n".join([f"Usuário {user_id}: {review['review']} (Nota: {review['rating']})"
                          for user_id, review in self._reviews.items()])
