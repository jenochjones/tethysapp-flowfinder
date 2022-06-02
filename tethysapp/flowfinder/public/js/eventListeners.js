import {
    addTileToDataLayer,
    addTileToElevationLayer, clearDataLayer,
    clearMap,
    createGeojosnMarker,
    getGeojson,
    getMapMarker,
    getRectangleBounds,
    setDataOpacity,
    setElevationOpacity
} from "./mapPackage.js";
import {
    delineateWatershed,
    downloadElevation,
    getTimeSeriesAjax
} from "./ajax.js";
import {
    createGraph,
    makeTrace
} from "./graphPackage.js";
import {
    sizeWindows
} from "./auxilary.js";

let eventListeners;

eventListeners = function () {

    document.getElementById("down-wat-btn").addEventListener("click", () => {
        const fileToDownload = JSON.stringify(getGeojson());
        if (fileToDownload !== undefined) {
            const blob = new Blob([fileToDownload], {type: `text/geojson;charset=utf-8;`});
            const link = document.createElement("a");
            const url = URL.createObjectURL(blob);
            const currentdate = new Date();
            const datetime = `${currentdate.getDate()}-${(currentdate.getMonth() + 1)}-${currentdate.getFullYear()}-${currentdate.getHours()}:${currentdate.getMinutes()}:${currentdate.getSeconds()}`;
            link.setAttribute("href", url);
            link.setAttribute("download", `${datetime}.geojson`);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    });

    document.getElementById("clear-map-btn").addEventListener("click", (event) => {
        clearMap();
    });

    document.getElementById("get-dem-btn").addEventListener("click", async (event) => {
        const bounds = getRectangleBounds();
        if (bounds !== undefined) {
            const streams = await downloadElevation(bounds);
            console.log(streams);
            createGeojosnMarker(streams.streams)
        } else {
            alert("Please define a region.");
        }
    });

    document.getElementById("del-wat-btn").addEventListener("click", async (event) => {
        const coords = getMapMarker();
        if (coords !== undefined) {
            const watershed = await delineateWatershed(coords);
            createGeojosnMarker(watershed.watershed)
        } else {
            alert("Please define a region.");
        }
    });

    document.getElementById("elevation-select").addEventListener("change", async (event) => {
        addTileToElevationLayer();
    });

    document.getElementById("data-select").addEventListener("change", async (event) => {
        if (document.getElementById("data-select").value === "none") {
            clearDataLayer();
        } else {
            let firstDate = "2000-01-01";
            let secondDate = "2022-05-11";
            if (document.getElementById("data-select").value === "ECMWF_ERA5_DAILY:total_precipitation") {
                firstDate = "1979-01-02";
                secondDate = "2020-07-09";
            }
            $("#first-date").attr("min", firstDate);
            $("#first-date").attr("max", secondDate);
            $("#first-date").val(firstDate);
            $("#second-date").attr("min", firstDate);
            $("#second-date").attr("max", secondDate);
            $("#second-date").val(secondDate);
            addTileToDataLayer();
        }
    });

    document.getElementById("elevation-layer-opacity").addEventListener("change", (event) => {
        setElevationOpacity();
    });

    document.getElementById("data-layer-opacity").addEventListener("change", (event) => {
        setDataOpacity();
    });

    document.getElementById("plot-data-btn").addEventListener("click", async (event) => {
        const timeSeries = await getTimeSeriesAjax();
        console.log(timeSeries)
        Object.keys(timeSeries).forEach((key) => {
            if (key !== "datetime") {
                makeTrace(timeSeries[key], timeSeries["datetime"], key, key);
            }
        })
        $("#slider-bar").css("left", "50%");
        sizeWindows();
    });
}

export {
    eventListeners
}