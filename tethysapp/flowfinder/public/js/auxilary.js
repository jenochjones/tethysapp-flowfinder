import {createGraph} from "./graphPackage.js";

let checkCsrfSafe;
let getCookie;
let addDefaultBehaviorToAjax;
let sizeWindows;

checkCsrfSafe = function (method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

getCookie = function (name) {
    let cookie;
    let cookies;
    let cookieValue = null;
    let i;

    if (document.cookie && document.cookie !== "") {
          cookies = document.cookie.split(";");
          for (i = 0; i < cookies.length; i += 1) {
                cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + "=") {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break
                }
          }
    }
    return cookieValue;
}

addDefaultBehaviorToAjax = function () {
    // Add CSRF token to appropriate ajax requests
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!checkCsrfSafe(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            }
        }
    });
};

sizeWindows = function () {
    const position = ($("#slider-bar").position().left * ($("#graph-map-btn").width() /
        ($("#graph-map-btn").width() - $("#slider-bar").width()))) /
        $("#graph-map-btn").width() * 100;
    $("#map").animate({height: `${position}%`}, {
        duration: 200,
        easing: "swing",
    });
    $("#graphs").animate({height: `${100 - position}%`}, {
        duration: 200,
        easing: "swing",
        complete: function () {
            createGraph();
        }
    });
};

export {
    addDefaultBehaviorToAjax,
    sizeWindows
};
