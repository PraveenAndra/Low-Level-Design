// PaymentProcessor interface for general payment processing
interface PaymentProcessor {
    void processPayment();
}

// CreditCardProcessor class implementing PaymentProcessor
class CreditCardProcessor implements PaymentProcessor {
    public void processPayment() {
        // Logic to process credit card payment
    }
}

// PayPalProcessor class implementing PaymentProcessor
class PayPalProcessor implements PaymentProcessor {
    public void processPayment() {
        // Logic to process PayPal payment
    }
}

// PaymentProcessing class now depends on abstraction
class PaymentProcessing {
    private PaymentProcessor paymentProcessor;

    // Constructor injection for dependency
    public PaymentProcessing(PaymentProcessor paymentProcessor) {
        this.paymentProcessor = paymentProcessor;
    }

    public void processPayment() {
        paymentProcessor.processPayment();
    }
}