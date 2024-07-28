const $admin_top_li = $("#admin_top_li");
const $site_data_li = $("#site_data_li");
const $buy_data_li = $("#buy_data_li");
const $inquiry_page_li = $("#inquiry_page_li");
const $user_data_li = $("#user_data_li");
const $product_li = $("#product_li");
const $feature_li = $("#feature_li");
const $admin_top = $("#admin_top");
const $site_data = $("#site_data");
const $buy_data = $("#buy_data");
const $inquiry_page = $("#inquiry_page");
const $user_data = $("#user_data");
const $product = $("#product");
const $feature = $("#feature");


const $site_data_li_button = $(".site_data_li");
const $buy_data_li_button = $(".buy_data_li");
const $inquiry_page_li_button = $(".inquiry_page_li");






$admin_top_li.on("click", function() {
    $admin_top.css({
        "display":"block"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#1e3333"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$site_data_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"block"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#1e3333"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$buy_data_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"block"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#1e3333"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$inquiry_page_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"block"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#1e3333"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$user_data_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"block"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#1e3333"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$product_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"block"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#1e3333"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$feature_li.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"flex"
    });

    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#1e3333"
    });
});












$site_data_li_button.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"block"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#1e3333"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$buy_data_li_button.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"block"
    });
    $inquiry_page.css({
        "display":"none"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#1e3333"
    });
    $inquiry_page_li.css({
        "background-color" : "#2f4f4f"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});

$inquiry_page_li_button.on("click", function() {
    $admin_top.css({
        "display":"none"
    });
    $site_data.css({
        "display":"none"
    });
    $buy_data.css({
        "display":"none"
    });
    $inquiry_page.css({
        "display":"block"
    });
    $user_data.css({
        "display":"none"
    });
    $product.css({
        "display":"none"
    });
    $feature.css({
        "display":"none"
    });


    $admin_top_li.css({
        "background-color" : "#2f4f4f"
    });
    $site_data_li.css({
            "background-color" : "#2f4f4f"
    });
    $buy_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $inquiry_page_li.css({
        "background-color" : "#1e3333"
    });
    $user_data_li.css({
        "background-color" : "#2f4f4f"
    });
    $product_li.css({
        "background-color" : "#2f4f4f"
    });
    $feature_li.css({
        "background-color" : "#2f4f4f"
    });
});