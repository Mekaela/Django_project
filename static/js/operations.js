document.addEventListener('DOMContentLoaded', function() {
    const farmSelect = document.getElementById("farm");
    console.log("farm select element:", farmSelect);
    const blockSelect = document.getElementById("block");
    console.log("block select element:", document.getElementById("block"));

    farmSelect.addEventListener("change", function () {
        const farmId = farmSelect.value;
        fetch(`/farms/blocks-for-farm/${farmId}/`)
        // Clear blocks
        blockSelect.innerHTML = '';
        blockSelect.disabled = true;

        if (farmId) {
            // Fetch blocks for the selected farm
            fetch(`/farms/blocks-for-farm/${farmId}/`)
                .then(response => response.json())
                .then(blocks => {
                    blocks.forEach(block => {
                        const option = document.createElement('option');
                        option.value = block.id;
                        option.textContent = block.name;
                        blockSelect.appendChild(option);
                    });
                    blockSelect.disabled = false;
                });
        }
    });
    

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
