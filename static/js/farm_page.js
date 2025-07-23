
console.log("Farm page script loaded");

LAT_CENTRE = 38.844733; 
LNG_CENTRE = -9.394690; 

document.addEventListener("DOMContentLoaded", function(){
    console.log("inside");
    var map = L.map('map').setView([LAT_CENTRE, LNG_CENTRE], 15); // Set to default farm location
    // google isn't always up to date, so could update this later
    L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    }).addTo(map);

   

    // Feature Group to store drawn layers
    // var drawnItems = new L.FeatureGroup();
    // map.addLayer(drawnItems);

    // // Add drawing controls
    // var drawControl = new L.Control.Draw({
    //     draw: {
    //         polyline: false,
    //         circle: false,
    //         rectangle: false,
    //         marker: false,
    //         circlemarker: false,
    //         polygon: {
    //             allowIntersection: false,
    //             showArea: true
    //         }
    //     },
    //     edit: {
    //         featureGroup: drawnItems
    //     }
    // });
    // console.log("inside 2");
    // map.addControl(drawControl);

    

    // // On drawing complete, prompt for block name and send to backend
    // map.on(L.Draw.Event.CREATED, function (event) {
    //     var layer = event.layer;
    //     var coords = layer.getLatLngs();
    //     var name = prompt("Enter block name:");

    //     // Optionally show popup with name
    //     layer.bindPopup(name).openPopup();
    //     drawnItems.addLayer(layer);

    //     // Prepare GeoJSON for submission
    //     var geojson = layer.toGeoJSON();

    //     // Send to Django via AJAX (POST)
    //     fetch("{% url 'block_create' %}", {
    //          method: "POST",
    //          headers: {
    //            "Content-Type": "application/json",
    //            "X-CSRFToken": "{{ csrf_token }}",
    //          },
    //          body: JSON.stringify({
    //             "name": name,
    //             "geometry": geojson.geometry
    //          })
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         alert("Block saved!");
    //     });
    // });
});
