# // Adapter is used to connect to a legacy or incompatible class to an existing modern interface
import random
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    @abstractmethod
    def is_paid(self):
        pass
    @abstractmethod
    def get_transaction_id(self):
        pass

import uuid

class PaypalProcessor(PaymentProcessor):
    _transaction_id = None
    _payment_success = False

    def process_payment(self, amount):
        self._transaction_id = str(uuid.uuid4())  # Generate unique transaction ID
        self._payment_success = True

    def is_paid(self):
        return self._payment_success

    def get_transaction_id(self):
        return self._transaction_id


class LegacyPaymentProcessor:
    transaction_id = None
    payment_success = False

    def make_transaction(self, amount):
        self.transaction_id = str(uuid.uuid4())  # Generate unique transaction ID
        self.payment_success = True
class LegacyPaymentAdapter(PaymentProcessor):
    legacy_payment = None
    def __init__(self):
        self.legacy_payment = LegacyPaymentProcessor()
    def process_payment(self, amount):
        self.legacy_payment.make_transaction(amount)

    def is_paid(self):
        return self.legacy_payment.payment_success
    def get_transaction_id(self):
        return self.legacy_payment.transaction_id

def main():
    # Using PayPal processor
    paypal_processor = PaypalProcessor()
    paypal_processor.process_payment(100)
    print(f"Transaction ID: {paypal_processor.get_transaction_id()}, Paid: {paypal_processor.is_paid()}")

    # Using Legacy Payment processor with Adapter
    legacy_adapter = LegacyPaymentAdapter()
    legacy_adapter.process_payment(30)  # Payment amount <= 50, so it should fail
    print(f"Transaction ID: {legacy_adapter.get_transaction_id()}, Paid: {legacy_adapter.is_paid()}")

if __name__ == "__main__":
    main()