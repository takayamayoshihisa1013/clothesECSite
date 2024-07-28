// レビューの評価値
const $review_num = $(".reviewNumText").text();

// 星の数
const $star1 = $(".star1 .change");
const $star2 = $(".star2 .change");
const $star3 = $(".star3 .change");
const $star4 = $(".star4 .change");
const $star5 = $(".star5 .change");

const $color_img_parent = $(".color_img");

let $color_img = $(".color_img img");

const $clothes_img = $(".clothes_img img");




// $review_num.text()
// console.log($review_num.text())

if ($review_num == 5.0) {
    
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "100%"
        });
        $star4.css({
            "width" : "100%"
        });
        $star5.css({
            "width" : `100%`
        });
        console.log("5");
    
} 
else if($review_num >= 4.0) {
    if($review_num - 4.0 == 0) {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "100%"
        });
        $star4.css({
            "width" : "100%"
        });
        $star5.css({
            "width" : "0%"
        });
    } else {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "100%"
        });
        $star4.css({
            "width" : "100%"
        });
        $star5.css({
            "width" : `${(($review_num - 4 ) * 100)}%`
        });
    }
    console.log("4");
} 
else if($review_num >= 3.0) {
    if($review_num - 3.0 == 0) {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "100%"
        });
        $star4.css({
            "width" : "0%"
        });
        $star5.css({
            "width" : "0%"
        });
    }
    else {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "100%"
        });
        $star4.css({
            "width" : `${(($review_num - 3 ) * 100)}%`
        });
        $star5.css({
            "width" : `0%`
        });
    }
    console.log("3");
}
else if($review_num >= 2.0) {
    if($review_num - 2.0 == 0) {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : "0%"
        });
        $star4.css({
            "width" : "0%"
        });
        $star5.css({
            "width" : "0%"
        });
    }
    else {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "100%"
        });
        $star3.css({
            "width" : `${(($review_num - 2 ) * 100)}%`
        });
        $star4.css({
            "width" : `0%`
        });
        $star5.css({
            "width" : `0%`
        });
    }
    console.log("2");
}
else if($review_num >= 1.0) {
    if($review_num - 1.0 == 0) {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : "0%"
        });
        $star3.css({
            "width" : "0%"
        });
        $star4.css({
            "width" : "0%"
        });
        $star5.css({
            "width" : "0%"
        });
    }
    else {
        $star1.css({
            "width" : "100%"
        });
        $star2.css({
            "width" : `${(($review_num - 1 ) * 100)}%`
        });
        $star3.css({
            "width" : `0%`
        });
        $star4.css({
            "width" : `0%`
        });
        $star5.css({
            "width" : `0%`
        });
    }
    console.log("1");
}
else if($review_num >= 0) {
    if($review_num - 1.0 == 0) {
        $star1.css({
            "width" : "0%"
        });
        $star2.css({
            "width" : "0%"
        });
        $star3.css({
            "width" : "0%"
        });
        $star4.css({
            "width" : "0%"
        });
        $star5.css({
            "width" : "0%"
        });
    }
    else {
        $star1.css({
            "width" : `${(($review_num) * 100)}%`
        });
        $star2.css({
            "width" : `0%`
        });
        $star3.css({
            "width" : `0%`
        });
        $star4.css({
            "width" : `0%`
        });
        $star5.css({
            "width" : `0%`
        });
    }
    console.log("0");
}



$color_img.on("click", function() {
    let this_img = $(this).attr("src");
    console.log(this_img);
    $clothes_img.attr("src", this_img);
    $color_img_parent.css({
        "border":"#000 1px solid"
    })
    $(this).parent().parent().css({
        "border":"orange 1px solid"
    })
})


const $star_label1 = $(".star-label1");
const $star_label2 = $(".star-label2");
const $star_label3 = $(".star-label3");
const $star_label4 = $(".star-label4");
const $star_label5 = $(".star-label5");


$star_label1.on("click", function() {
    $star_label1.css({
        "color":"gold"
    })
    $star_label2.css({
        "color":"gray"
    })
    $star_label3.css({
        "color":"gray"
    })
    $star_label4.css({
        "color":"gray"
    })
    $star_label5.css({
        "color":"gray"
    })
})

$star_label2.on("click", function() {
    $star_label1.css({
        "color":"gold"
    })
    $star_label2.css({
        "color":"gold"
    })
    $star_label3.css({
        "color":"gray"
    })
    $star_label4.css({
        "color":"gray"
    })
    $star_label5.css({
        "color":"gray"
    })
})

$star_label3.on("click", function() {
    $star_label1.css({
        "color":"gold"
    })
    $star_label2.css({
        "color":"gold"
    })
    $star_label3.css({
        "color":"gold"
    })
    $star_label4.css({
        "color":"gray"
    })
    $star_label5.css({
        "color":"gray"
    })
})

$star_label4.on("click", function() {
    $star_label1.css({
        "color":"gold"
    })
    $star_label2.css({
        "color":"gold"
    })
    $star_label3.css({
        "color":"gold"
    })
    $star_label4.css({
        "color":"gold"
    })
    $star_label5.css({
        "color":"gray"
    })
})

$star_label5.on("click", function() {
    $star_label1.css({
        "color":"gold"
    })
    $star_label2.css({
        "color":"gold"
    })
    $star_label3.css({
        "color":"gold"
    })
    $star_label4.css({
        "color":"gold"
    })
    $star_label5.css({
        "color":"gold"
    })
})


const $buy_process = $(".buy_process");
const $first = $(".first");
const $address = $(".address");
const $product_return = $("#clothes_return");

console.log($product_return)

$buy_process.on("click", function() {
    $address.css({
        "display":"block"
    })
    $first.css({
        "display":"none"
    })
})

$product_return.on("click", function() {
    $address.css({
        "display":"none"
    })
    $first.css({
        "display":"block"
    })
})




const $size_check = $(".size_check");

$("input[type=radio][name=clothesSize]").change(function() {
    var select_size = $(this).val();

    $size_check.text("サイズ：" + select_size);
})

$("input[type=radio][name=clothesImage]").change(function() {
    // 選択された画像の URL を取得
    var select_img = $(this).val();
    console.log(select_img);
    
    // 画像要素のsrc属性を変更する
    document.querySelector(".last_check_img").setAttribute("src", select_img);
});

const $count_check = $(".count_check");

$("#count").change(function() {
    var select_count = $(this).val();

    $count_check.text("個数：" + select_count);
})

const h_adr = $(".address .h-adr");
$("input[type=radio][name=address_check]").change(function() {
    var address_check = $(this).val()
    console.log(address_check)

    if(address_check == "on") {
        h_adr.css({
            "display":"block"
        })
    }
    else {
        h_adr.css({
            "display":"none"
        })
    }
})





// let showForm = $(this).attr("class");

