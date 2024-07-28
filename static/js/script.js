const $header = $("header");

const $clothesSite = $(".clothesSite");

const $sub = $(".sub");


const $all = $("#all");
const $mens = $("#men");
const $ladies = $("#woman");
const $kids = $("#kid");
const $buck = $(".back");


const $header_img = $(".header_img");





const article = $("article");

const $mensClothes = $("#mensClothes");

const $ladiesClothes = $("#ladiesClothes");

const $kidsClothes = $("#kidsClothes");

const $allClothes = $("#allClothes");

const $address = $(".address");






const $siteConcept = $(".SiteConcept");

const text1 = $("#text1");
const text2 = $("#text2");
const text3 = $("#text3");
const text4 = $("#text4");
const $SiteConceptImgLeft = $("#SiteConceptImgLeft");
const $SiteConceptImgRight = $("#SiteConceptImgRight");




const $two = $(".two");




$allClothes.show();
$ladiesClothes.hide();
$kidsClothes.hide();
$mensClothes.hide();




$all.on("click", function(){
    $buck.css({
        "left":"0"
    })
    $kidsClothes.hide();
    $ladiesClothes.hide();
    $mensClothes.hide();
    $allClothes.show();
    $two.css({
        "background-color": "rgba(255,204,0,0.1)"
    })
})

$mens.on("click", function(){
    $buck.css({
        "left":"calc((36vw / 4) * 1)"
    })
    $mensClothes.show();
    $kidsClothes.hide();
    $ladiesClothes.hide();
    $allClothes.hide();
    $two.css({
        "background-color": "#f0f8ff"
    })
})

$kids.on("click", function(){
    $buck.css({
        "left":"calc((36vw / 4) * 3)"
    })
    $mensClothes.hide();
    
    $ladiesClothes.hide();
    $kidsClothes.show();
    $allClothes.hide();
    $two.css({
        "background-color": "rgba(255,255,0,0.4)"
    })
})

$ladies.on("click", function() {
    $buck.css({
        "left":"calc((36vw / 4) * 2)"
    })
    $mensClothes.hide();
    $ladiesClothes.show();
    $kidsClothes.hide();
    $allClothes.hide();
    $two.css({
        "background-color": "rgba(255,192,203,0.55)"
    })
})














$(window).on("scroll load", function() {
    var scroll = $(this).scrollTop();
    console.log(scroll);



    if (scroll > 480) {
        $header.css({
            "height":"22vh"
        })
        // $clothesSite.css({
        //     "margin-top":"9vh"
        // })
        $sub.css({
            "margin":"-35vh auto 0",
            "opacity":"0"
        })
        $header_img.css({
            "height":"17vh",
            "margin-top":"2.5vh"
        })
        $address.css({
            "margin":"-35vh auto 0",
            "opacity":"0"
        })
        $clothesSite.css({
            "height":"16vh"
        })
    }
    else {
        $header.css({
            "height":"30vh"
        })
        // $clothesSite.css({
        //     "margin-top":"9vh"
        // })
        $sub.css({
            "margin":"4vh auto 0",
            "opacity":"1"
        })

        $header_img.css({
            "height":"30vh",
            "margin":"0"
        })
        $address.css({
            "margin":"0 auto",
            "opacity":"1"
        })
        $clothesSite.css({
            "height":"24vh"
        })
    }

    
    if (scroll > 1200) {
        $siteConcept.css({
            "opacity":"1",
        })
    }
    else {
        $siteConcept.css({
            "opacity":"0",
        })
    }
    if (scroll >= 1300) {
        text1.css({
            "opacity":"1"
        })
    }
    else {
        text1.css({
            "opacity":"0"
        })
    }    
    if (scroll >= 1900) {
        text2.css({
            "opacity":"1"
        })
    }
    else {
        text2.css({
            "opacity":"0"
        })
    }
    if (scroll == 2500) {
        $SiteConceptImgLeft.css({
            "opacity":"0"
        })
        $SiteConceptImgRight.css({
            "opacity":"0"
        })
        setTimeout(() => {
            $SiteConceptImgLeft.css({
                "opacity":"1"
            })
            $SiteConceptImgRight.css({
                "opacity":"1"
            },500)
        });
    }

    if (scroll >= 2500) {
        text3.css({
            "opacity":"1"
        })
        
        
        $SiteConceptImgLeft.attr("src","./../../static/images/indexTop/74711709b_b_42_500.jpg")
        $SiteConceptImgRight.attr("src","./../../static/images/indexTop/1630999025_500.webp")
        
        
    
    }
    else {
        console.log("d")
        $SiteConceptImgLeft.attr("src","./../../static/images/indexTop/b661740a428ab476b9661579da8fdfad.jpg")
        $SiteConceptImgRight.attr("src","./../../static/images/indexTop/1-1024x683.jpg")
        console.log("")
        text3.css({
            "opacity":"0"
        })
    }
    if (scroll >= 3100) {
        text4.css({
            "opacity":"1"
        })
    }
    else {
        text4.css({
            "opacity":"0"
        })
    }
    if (scroll >= 3900) {
        article.css({
            "background-color":"#ffff"
        })
        text1.css({
            "color":"#000"
        })
        text2.css({
            "color":"#000"
        })
        text3.css({
            "color":"#000"
        })
        text4.css({
            "color":"#000"
        })
    }
    else {
        article.css({
            "background-color":"#000"
        })
        text1.css({
            "color":"#ffff"
        })
        text2.css({
            "color":"#ffff"
        })
        text3.css({
            "color":"#ffff"
        })
        text4.css({
            "color":"#ffff"
        })
    }
})







// ボタン押したら項目増えるやつ
// const $two = $(".two");


// const $top1 = $(".top1");
// const $top2 = $(".top2");
// const $bottom1 = $(".bottom1");
// const $bottom2 = $(".bottom2");

// const $three = $(".three")


// console.log("aaa")










// // アカウント詳細表示
// $account_detail.hide();
// $account.on("click", function(e) {
//     console.log("show")
//     if ($account_detail.hasClass("show")){
//         $account_detail.hide();
//         $account_detail.removeClass("show");
//     }
//     else {
//         e.stopPropagation();
//         $account_detail.show();
//         $account_detail.addClass("show");
//     }


// })

// $(document).on("click", function(e) {
//     if(!$(e.target).closest($account_detail,$account).length) {
//         $account_detail.removeClass("show");
        
//         $account_detail.hide();
        
//         console.log("u")
//     }
// })









// // ボタン押したら項目増えるやつ

// $top2.hide();
// $bottom2.hide();

// $top1.on("click", function() {
//     $three.css({"margin-top": "0"});
//     $two.css({"height":"calc(100vh + 30px)"});
//     $top2.show();//洋服表示
//     $bottom2.hide();//ズボン非表示
//     setTimeout(function() {
//         $bottom2.removeClass("active");
//         $top2.addClass("active");
//     })
    
//     console.log("aaa")
// })

// $bottom1.on("click", function() {
//     $three.css({"margin-top": "0"});
//     $two.css({"height":"calc(100vh + 30px)"});

//     $bottom2.show();//ズボン表示
//     $top2.hide();//洋服非表示
//     setTimeout(function() {
//         $top2.removeClass("active");
//         $bottom2.addClass("active");
//     })
    
//     console.log("aaa")
// })
