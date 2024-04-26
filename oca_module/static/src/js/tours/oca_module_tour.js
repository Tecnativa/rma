odoo.define("oca_module.tour_frontend", function (require) {
    "use strict";
    var tour = require("web_tour.tour");
    tour.register(
        "oca_module_tour",
        {
            test: true,
            url: "/my",
        },
        [
            {
                content: "Go /my/orders url",
                trigger: 'a[href*="/my/orders"]',
            },
            {
                content: "Go to first order item",
                trigger: "td:eq(0) a",
            },
        ]
    );
});
