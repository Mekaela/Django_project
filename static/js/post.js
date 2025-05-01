document.addEventListener('DOMContentLoaded', function() {
    const recordTypeSelect = document.getElementById('recordType');
    const allRecordFields = document.querySelectorAll('.record-fields');
    
    // Hide all record-specific fields initially
    allRecordFields.forEach(field => {
        field.style.display = 'none';
    });
    
    // Add event listener for record type selection
    recordTypeSelect.addEventListener('change', function() {
        // Hide all record-specific fields
        allRecordFields.forEach(field => {
            field.style.display = 'none';
        });
        
        // Show the selected record type's fields
        const selectedRecordType = this.value;
        if (selectedRecordType) {
            const fieldsToShow = document.getElementById(selectedRecordType + 'Fields');
            if (fieldsToShow) {
                fieldsToShow.style.display = 'grid';
            }
        }
    });
    
    // Form submission
    document.getElementById('agricultureForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        
        // Here you would typically send the data to a server
        console.log('Form data:', data);
        alert('Record saved successfully!');
        this.reset();
        
        // Hide all record-specific fields after submission
        allRecordFields.forEach(field => {
            field.style.display = 'none';
        });
    });
});