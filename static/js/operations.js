document.addEventListener('DOMContentLoaded', function() {
    const farmSelect = document.getElementById("farm");
    console.log("farm select element:", farmSelect);
    const plotSelect = document.getElementById("plot");
    console.log("plot select element:", document.getElementById("plot"));

    farmSelect.addEventListener("change", function () {
        const farmId = farmSelect.value;
        fetch(`/farms/plots-for-farm/${farmId}/`)
        // Clear plots
        plotSelect.innerHTML = '';
        plotSelect.disabled = true;

        if (farmId) {
            // Fetch plots for the selected farm
            fetch(`/farms/plots-for-farm/${farmId}/`)
                .then(response => response.json())
                .then(plots => {
                    plots.forEach(plot => {
                        const option = document.createElement('option');
                        option.value = plot.id;
                        option.textContent = plot.name;
                        plotSelect.appendChild(option);
                    });
                    plotSelect.disabled = false;
                });
        }
    });

    // const recordTypeSelect = document.getElementById('recordType');
    // const allRecordFields = document.querySelectorAll('.record-fields');
    
    // // Hide all record-specific fields initially
    // allRecordFields.forEach(field => {
    //     field.style.display = 'none';
    // });
    
    // // Add event listener for record type selection
    // recordTypeSelect.addEventListener('change', function() {
    //     // Hide all record-specific fields
    //     allRecordFields.forEach(field => {
    //         field.style.display = 'none';
    //     });
        
    //     // Show the selected record type's fields
    //     const selectedRecordType = this.value;
    //     if (selectedRecordType) {
    //         const fieldsToShow = document.getElementById(selectedRecordType + 'Fields');
    //         if (fieldsToShow) {
    //             fieldsToShow.style.display = 'grid';
    //         }
    //     }
    // });
    
    // // Form submission
    // document.getElementById('agricultureForm').addEventListener('submit', function(e) {
    //     e.preventDefault();
        
    //     const formData = new FormData(this);
    //     const data = {};
    //     formData.forEach((value, key) => {
    //         data[key] = value;
    //     });
        
    //     // Here you would typically send the data to a server
    //     console.log('Form data:', data);
    //     alert('Record saved successfully!');
    //     this.reset();
        
    //     // Hide all record-specific fields after submission
    //     allRecordFields.forEach(field => {
    //         field.style.display = 'none';
    //     });
    // });
    

    // const farmSelect = document.getElementById("farm");
    // const blockSelect = document.getElementById("block");

    // farmSelect.addEventListener("change", function () {
    //     const farmId = farmSelect.value;
    //     // Clear blocks
    //     blockSelect.innerHTML = '<option value="">-- Select Block --</option>';
    //     blockSelect.disabled = true;

    //     if (farmId) {
    //         // Fetch blocks for the selected farm
    //         fetch(`block/create/${farmId}/`) 
    //             .then(response => response.json())
    //             .then(blocks => {
    //                 blocks.forEach(block => {
    //                     const option = document.createElement('option');
    //                     option.value = block.id;
    //                     option.textContent = block.name;
    //                     blockSelect.appendChild(option);
    //                 });
    //                 blockSelect.disabled = false;
    //             });
    //     }
    // });
});
