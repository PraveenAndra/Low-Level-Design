class PaymentProcessing {
    private CreditCardProcessor creditCardProcessor;

    public PaymentProcessing() {
        this.creditCardProcessor = new CreditCardProcessor(); // Direct dependency
    }

    public void processPayment() {
        creditCardProcessor.processPayment();
    }
}

class CreditCardProcessor {
    public void processPayment() {
        // Logic to process credit card payment
    }
}