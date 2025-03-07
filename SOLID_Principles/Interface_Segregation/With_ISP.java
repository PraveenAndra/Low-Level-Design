// Breaking the User interface into smaller, focused interfaces

// Interface for viewing data
interface Viewable {
    void view_data();  // View data
}

// Interface for editing data
interface Editable {
    void edit_data();  // Edit data
}

// Interface for deleting data
interface Deletable {
    void delete_data();  // Delete data
}

// AdminUser implements all three interfaces
class AdminUser implements Viewable, Editable, Deletable {

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

// ReadOnlyUser only implements Viewable interface
class ReadOnlyUser implements Viewable {

    @Override
    public void view_data() {
        // Logic to view data
    }
}