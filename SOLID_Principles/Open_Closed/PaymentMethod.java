// PaymentMethod interface represents a generic payment method
interface PaymentMethod {

    // Processes the payment
    void processPayment();
}

// CreditCard payment method class
class CreditCardPayment implements PaymentMethod {

    @Override
    public void processPayment() {
        // Logic to process credit card payment
    }
}

// PayPal payment method class
class PayPalPayment implements PaymentMethod {

    @Override
    public void processPayment() {
        // Logic to process PayPal payment
    }
}

// PaymentProcessor now works with any PaymentMethod (open for extension)
class PaymentProcessor {

    // Processes the payment using a PaymentMethod
    public void processPayment(PaymentMethod paymentMethod) {
        paymentMethod.processPayment();
    }
}