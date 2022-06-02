import {
    delineateWatershedURL,
    downloadElevationURL,
    getDataImageURL,
    getElevationImageURL,
    getTimeSeriesURL
} from "./urls.js";
import {
    getGeojson
} from "./mapPackage.js";

let downloadElevation;
let delineateWatershed;
let getDataImageAjax;
let getElevationImageAjax;
let getTimeSeriesAjax;

downloadElevation = async function (bounds) {
    const result = await $.ajax({
        data: {
            bounds: JSON.stringify(bounds),
            product: "elevation",
            dataset: document.getElementById("elevation-select").value
        },
        dataType: 'json',
        type: 'GET',
        url: downloadElevationURL,
    });
    return result.data;
};

delineateWatershed = async function (coords) {
    const result = await $.ajax({
        data: {coords: JSON.stringify(coords)},
        dataType: 'json',
        type: 'POST',
        url: delineateWatershedURL,
    });
    return result.data;
};

getDataImageAjax = async function () {
    const value = document.getElementById("data-select").value;
    const product = value.split(":")[0];
    const dataset = value.split(":")[1];
    const data = {
        product: product,
        dataset: dataset
    }
    const result = await $.ajax({
        data: data,
        dataType: 'json',
        type: 'GET',
        url: getDataImageURL,
    });
    return result.data;
};

getElevationImageAjax = async function () {
    const data = {
        product: "elevation",
        dataset: document.getElementById("elevation-select").value
    }
    const result = await $.ajax({
        data: data,
        dataType: 'json',
        type: 'GET',
        url: getElevationImageURL,
    });
    return result.data;
};

getTimeSeriesAjax = async function () {
    const value = document.getElementById("data-select").value;
    const product = value.split(":")[0];
    const dataset = value.split(":")[1];
    const firstDate = document.getElementById("first-date").value;
    const secondDate = document.getElementById("second-date").value;
    const geojson = JSON.stringify(getGeojson());
    let daily;
    let allProducts;

    if (document.getElementById("daily-checkbox").checked) {
        daily = true;
    } else {
        daily = false;
    }

    if (value === "none") {
        allProducts = true;
    } else {
        allProducts = false;
    }

    const data = {
        product: product,
        dataset: dataset,
        firstDate: firstDate,
        secondDate: secondDate,
        geojson: geojson,
        daily: daily,
        allProducts: allProducts
    }
    const result = await $.ajax({
        data: data,
        dataType: 'json',
        type: 'POST',
        url: getTimeSeriesURL,
    });
    return JSON.parse(result.data);
};

export {
    downloadElevation,
    delineateWatershed,
    getDataImageAjax,
    getElevationImageAjax,
    getTimeSeriesAjax
}