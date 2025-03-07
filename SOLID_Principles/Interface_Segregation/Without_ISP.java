// A single User interface with methods that all classes must implement
interface User {
    void view_data();   // View data
    void edit_data();   // Edit data
    void delete_data(); // Delete data
}

// AdminUser needs all three methods
class AdminUser implements User {

    @Override
    public void view_data() {
        // Logic to view data
    }

    @Override
    public void edit_data() {
        // Logic to edit data
    }

    @Override
    public void delete_data() {
        // Logic to delete data
    }
}

// ReadOnlyUser only needs view_data() but must implement all methods
class ReadOnlyUser implements User {

    @Override
    public void view_data() {
        // Logic to view data
    }

    @Override
    public void edit_data() {
        // ReadOnlyUser doesn't edit data, but forced to implement
    }

    @Override
    public void delete_data() {
        // ReadOnlyUser doesn't delete data, but forced to implement
    }
}