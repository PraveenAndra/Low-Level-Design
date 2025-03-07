// Hotel class is violating SRP as it has multiple responsibilities.
class Hotel {

    // Stores room details
    public void storeRoomDetails() {
        // Logic to store room details in a database
    }

    // Handles bookings
    public void handleBooking() {
        // Logic to handle the booking process
    }

    // Displays room information
    public void displayRoomInfo() {
        // Logic to display room information
    }
}