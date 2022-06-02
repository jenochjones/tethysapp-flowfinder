import {getDataImageAjax, getElevationImageAjax} from "./ajax.js";

let addTileToElevationLayer;
let addTileToDataLayer;
let addSearchBar;
let clearDataLayer;
let clearMap;
let createDrawingLayers;
let createDataLayer;
let createElevationLayer;
let createGeojosnMarker;
let createMapMarker;
let dataLayer;
let elevationLayer;
let getMapMarker;
let getRectangleBounds;
let getGeojson;
let mapMarkerLayer;
let mapRectangleLayer;
let geojsonMarkerLayer;
let drawMenu;
let initBaseMaps;
let initMap;
let mapObj;
let mapDrawingMenu;
let setDataOpacity;
let setElevationOpacity;
let setUpMap;

addTileToDataLayer = async function () {
    const dataURL = await getDataImageAjax();
    console.log(dataURL)
    clearDataLayer();
    L.tileLayer(dataURL, {
        attribution: "Google Earth Engine",
        pane:"dataLayer",
    }).addTo(dataLayer);
};

addTileToElevationLayer = async function () {
    const elevationURL = await getElevationImageAjax();
    elevationLayer.clearLayers();
    L.tileLayer(elevationURL, {
        attribution: "Google Earth Engine",
        pane:"elevationLayer",
    }).addTo(elevationLayer);
}

addSearchBar = function () {
    L.Control.geocoder({defaultMarkGeocode: false}).on('markgeocode', function(e) {
        const bbox = e.geocode.bbox;
        const poly = L.polygon([
            bbox.getSouthEast(),
            bbox.getNorthEast(),
            bbox.getNorthWest(),
            bbox.getSouthWest()
        ])
        mapObj.flyToBounds(poly.getBounds());
    }).addTo(mapObj);
}

clearDataLayer = function () {
    dataLayer.clearLayers();
};

clearMap = function () {
    mapMarkerLayer.clearLayers();
    mapRectangleLayer.clearLayers();
    geojsonMarkerLayer.clearLayers();
};

createDrawingLayers = function () {
    if (mapObj !== undefined) {
        mapMarkerLayer = L.featureGroup().addTo(mapObj);
        mapRectangleLayer = L.featureGroup().addTo(mapObj);
        geojsonMarkerLayer = L.geoJSON().addTo(mapObj);
    }
};

createDataLayer = function () {
    dataLayer = L.layerGroup().addTo(mapObj);
};

createElevationLayer = function () {
    elevationLayer = L.layerGroup().addTo(mapObj);
};

createGeojosnMarker = function (geojsonFeature) {
    if (geojsonFeature !== undefined) {
        geojsonMarkerLayer.clearLayers();
        geojsonMarkerLayer.addData(geojsonFeature);
    }
};

createMapMarker = function (drawEvent) {
    if (drawEvent.layer !== undefined) {
        if (drawEvent.layerType === "marker") {
            mapMarkerLayer.clearLayers();
            mapMarkerLayer.addLayer(drawEvent.layer);
        } else if (drawEvent.layerType === "rectangle") {
            mapRectangleLayer.clearLayers();
            mapRectangleLayer.addLayer(drawEvent.layer);
        }
    }
};

getRectangleBounds = function () {
    if (mapRectangleLayer.toGeoJSON().features.length > 0) {
        return mapRectangleLayer.getBounds();
    } else {
        console.log("No Features On Map");
    }
};

getMapMarker = function () {
    let markerLatLng;
    mapMarkerLayer.eachLayer((layer) => {
        markerLatLng = layer.getLatLng();
    });
    return markerLatLng;
};

getGeojson = function () {
    if (geojsonMarkerLayer.toGeoJSON().features.length > 0) {
        return geojsonMarkerLayer.toGeoJSON();
    } else {
        alert("No features on the map.");
    }
};

initBaseMaps = function () {
    const basemapLayers = {
        "Esri Arial Imagery": L.tileLayer(
            "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
            {attribution: "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"}),
        "USGS Arial Imagery": L.tileLayer(
            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}",
            {attribution: "Tiles courtesy of the <a href='https://usgs.gov/'>U.S. Geological Survey</a>"}),
        "USGS Imagery With Labels": L.tileLayer(
            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}",
            {attribution: "Tiles courtesy of the <a href='https://usgs.gov/'>U.S. Geological Survey</a>"}),
        "USGS Topographical": L.tileLayer(
            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
            {attribution: "Tiles courtesy of the <a href='https://usgs.gov/'>U.S. Geological Survey</a>"}).addTo(mapObj)
    };
    L.control.layers(basemapLayers, null, {collapsed: true}).addTo(mapObj);
};

initMap = function () {
    mapObj = L.map("map", {
        boxZoom: true,
        center: [45, -110],
        fullscreenControl: true,
        minZoom: 2,
        zoom: 3,
        zoomSnap: 0.5
    });
    mapObj.createPane("elevationLayer");
    mapObj.getPane("elevationLayer").style.zIndex = 250;
    mapObj.createPane("dataLayer");
    mapObj.getPane("dataLayer").style.zIndex = 260;
    return mapObj;
};

mapDrawingMenu = function () {
    let drawControl = new L.Control.Draw({
        draw: {
            circle: false,
            polyline: false,
            polygon: false
        },
        edit: {
            edit: true,
            featureGroup: mapMarkerLayer
        }
    });
    drawControl.addTo(mapObj);
};

setDataOpacity = function () {
    const opacityValue = document.getElementById("data-layer-opacity").value;
    if (mapObj.hasLayer(dataLayer)) {
        dataLayer.getLayers().forEach((layer) => {
            layer.setOpacity(opacityValue);
        });
    } else {
        console.log("Can't set opacity");
    }
};

setElevationOpacity = function () {
    const opacityValue = document.getElementById("elevation-layer-opacity").value;
    if (mapObj.hasLayer(elevationLayer)) {
        elevationLayer.getLayers().forEach((layer) => {
            layer.setOpacity(opacityValue);
        });
    } else {
        console.log("Can't set opacity");
    }
};

setUpMap = function (callback) {
    initMap();
    initBaseMaps();
    createDrawingLayers();
    addSearchBar();
    createElevationLayer();
    createDataLayer();
    addTileToElevationLayer();
    drawMenu = mapDrawingMenu();
    mapObj.on(L.Draw.Event.CREATED, function (drawEvent) {
        createMapMarker(drawEvent);
    });

    if (typeof callback === "function") {
        callback();
    }
};

export {
    addTileToDataLayer,
    addTileToElevationLayer,
    clearDataLayer,
    clearMap,
    createGeojosnMarker,
    createMapMarker,
    getMapMarker,
    getRectangleBounds,
    getGeojson,
    setDataOpacity,
    setElevationOpacity,
    setUpMap
};

