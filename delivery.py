# delivery.py
import datetime


class Delivery:
    def __init__(self, order):
        self.order = order
        self.status = "Em preparo"
        self.status_history = []  # Histórico de status com horário

    def update_status(self, new_status):
        """Atualiza o status da entrega."""
        valid_statuses = ["Em preparo", "Saiu para entrega", "Entregue", "Cancelado"]
        if new_status in valid_statuses:
            self.status = new_status
            self.status_history.append((new_status, datetime.datetime.now()))
        else:
            raise ValueError(f"Status '{new_status}' inválido.")

    def display_status(self):
        """Exibe o status da entrega com horário."""
        status_details = "\n".join([f"{status} às {time.strftime('%H:%M:%S')}" for status, time in self.status_history])
        return f"Status do pedido:\n{status_details}"
