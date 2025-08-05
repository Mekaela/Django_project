
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrf_token = getCookie("csrftoken");

document.addEventListener("DOMContentLoaded", function(){
    var map = L.map('map').setView([lat_centre, lng_centre], 15); // Set to default farm location
    // google isn't always up to date, so could update this later
    L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
    }).addTo(map);

    // Feature Group to store drawn layers
    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);

    if (farmId) {
        // Fetch plots for the selected farm
        fetch(`/farms/plots-for-farm/${farmId}/`)
            .then(response => response.json())
            .then(plots => {
                plots.forEach(plot => {
                var layer = L.geoJSON(plot.area).getLayers()[0]; // Get the polygon layer from GeoJSON
                if(plot.name) {
                  layer.bindPopup(plot.name);
                }
                drawnItems.addLayer(layer);
              });
            })
            .catch(err => console.error('Failed to load blocks:', err));
    }


    // Add drawing controls
    var drawControl = new L.Control.Draw({
        draw: {
            polyline: false,
            circle: false,
            rectangle: false,
            marker: false,
            circlemarker: false,
            polygon: {
                allowIntersection: false,
                showArea: true
            }
        },
        edit: {
            featureGroup: drawnItems
        }
    });
    map.addControl(drawControl);

    

    // On drawing complete, prompt for block name and send to backend
    map.on(L.Draw.Event.CREATED, function (event) {
        var layer = event.layer;
        var coords = layer.getLatLngs();
        var name = prompt("Enter block name:");

        // Optionally show popup with name
        layer.bindPopup(name).openPopup();
        drawnItems.addLayer(layer);

        // Prepare GeoJSON for submission
        var geojson = layer.toGeoJSON();

        // Send to Django via AJAX (POST)
        fetch(blockCreateUrl, {
             method: "POST",
             headers: {
               "Content-Type": "application/json",
               "X-CSRFToken": csrf_token,
             },
             body: JSON.stringify({
                "name": name,
                "area": geojson.geometry
             })
        })
        .then(response => response.json())
        .then(data => {
            alert("Block saved!");
        }).catch(e => console.error("Error saving block:", e));
    });
});
