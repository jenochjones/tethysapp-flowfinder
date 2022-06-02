import { createGraph } from "./graphPackage.js";
import { setUpMap } from "./mapPackage.js" ;
import {addDefaultBehaviorToAjax, sizeWindows} from "./auxilary.js";
import {eventListeners} from "./eventListeners.js";

function ready(readyListener) {
    if (document.readyState !== "loading") {
        readyListener();
    } else {
        document.addEventListener("DOMContentLoaded", readyListener);
    }
}

ready(function () {
    addDefaultBehaviorToAjax();
    setUpMap(() => {
        console.log("Map Created");
    });
    createGraph();
    eventListeners();
    $("#slider-bar").draggable({
        axis : "x",
        containment : "#graph-map-btn",
        stop: sizeWindows
     });
});
