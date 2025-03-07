// PaymentProcessor is violating OCP as it needs to be modified for each new payment method
class PaymentProcessor {

    // Processes payment depending on the payment method
    public void processPayment(String paymentMethod) {
        if (paymentMethod.equals("CreditCard")) {
            // Logic to process credit card payment
        } else if (paymentMethod.equals("PayPal")) {
            // Logic to process PayPal payment
        }
    }
}