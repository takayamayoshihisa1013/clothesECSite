const $user = $(".user");
const $favorite = $(".favorite");
const $listing = $(".listing");
const $earnings = $(".earnings");
const $buyLog = $(".buyLog");
const $cart = $(".cart");

const $userpage = $(".userpage");
const $favoritepage = $(".favoritepage");
const $listingpage = $(".listingpage");
const $earningspage = $(".earningspage");
const $buyLogpage = $(".buyLogpage");
const $cartpage = $(".cartpage");


// alert("j")

$favoritepage.hide();
$listingpage.hide();
$earningspage.hide();
$buyLogpage.hide();
$cartpage.hide();


$user.on("click", function() {
    $userpage.show();
    $favoritepage.hide();
    $listingpage.hide();
    $earningspage.hide();
    $buyLogpage.hide();
    $cartpage.hide();
})

$favorite.on("click", function() {
    $userpage.hide();
    $favoritepage.show();
    $listingpage.hide();
    $earningspage.hide();
    $buyLogpage.hide();
    $cartpage.hide();
})

$listing.on("click", function() {
    $userpage.hide();
    $favoritepage.hide();
    $listingpage.show();
    $earningspage.hide();
    $buyLogpage.hide();
    $cartpage.hide();
})

$earnings.on("click", function() {
    $userpage.hide();
    $favoritepage.hide();
    $listingpage.hide();
    $earningspage.show();
    $buyLogpage.hide();
    $cartpage.hide();
})

$buyLog.on("click", function() {
    $userpage.hide();
    $favoritepage.hide();
    $listingpage.hide();
    $earningspage.hide();
    $buyLogpage.show();
    $cartpage.hide();
})

$cart.on("click", function() {
    $userpage.hide();
    $favoritepage.hide();
    $listingpage.hide();
    $earningspage.hide();
    $buyLogpage.hide();
    $cartpage.show();
})




$(document).ready(function () {
    // ページが読み込まれたときに実行されるコードを指定するためのdocument readyハンドラー
    
    var imgInput1 = $('#img1');
    var colorInput1 = $('#color1');
    var imgInput2 = $('#img2');
    var colorInput2 = $('#color2');
    var imgInput3 = $('#img3');
    var colorInput3 = $('#color3');
    var imgInput4 = $('#img4');
    var colorInput4 = $('#color4');
    var imgInput5 = $('#img5');
    var colorInput5 = $('#color5');
    var imgInput6 = $('#img6');
    var colorInput6 = $('#color6');
    var imgInput7 = $('#img7');
    var colorInput7 = $('#color7');
    
    // jQueryを使用して、id属性を持つ要素を取得し、変数に格納します。
    
    imgInput1.on('input', function () {
        if (imgInput1.val() !== '') {
            colorInput1.prop('required', true);
        } else {
            colorInput1.prop('required', false);
        }
    });
    
    // imgInputに対してinputイベントハンドラーを設定します。inputイベントは入力値が変更されたときに発生します。
    // imgInputの値が空でない場合、colorInputのrequiredプロパティをtrueに設定し、そうでない場合はfalseに設定します。
    
    colorInput1.on('input', function () {
        if (colorInput1.val() !== '') {
            imgInput1.prop('required', true);
        } else {
            imgInput1.prop('required', false);
        }
    });
    
    // colorInputに対しても同様のinputイベントハンドラーを設定し、colorInputの値に応じてimgInputのrequiredプロパティを設定します。



    imgInput2.on('input', function () {
        if (imgInput2.val() !== '') {
            colorInput2.prop('required', true);
        } else {
            colorInput2.prop('required', false);
        }
    });


    colorInput2.on('input', function () {
        if (colorInput2.val() !== '') {
            imgInput2.prop('required', true);
        } else {
            imgInput2.prop('required', false);
        }
    });


    imgInput3.on('input', function () {
        if (imgInput3.val() !== '') {
            colorInput3.prop('required', true);
        } else {
            colorInput3.prop('required', false);
        }
    });


    colorInput3.on('input', function () {
        if (colorInput3.val() !== '') {
            imgInput3.prop('required', true);
        } else {
            imgInput3.prop('required', false);
        }
    });


    imgInput4.on('input', function () {
        if (imgInput4.val() !== '') {
            colorInput4.prop('required', true);
        } else {
            colorInput4.prop('required', false);
        }
    });


    colorInput4.on('input', function () {
        if (colorInput4.val() !== '') {
            imgInput4.prop('required', true);
        } else {
            imgInput4.prop('required', false);
        }
    });


    imgInput5.on('input', function () {
        if (imgInput5.val() !== '') {
            colorInput5.prop('required', true);
        } else {
            colorInput5.prop('required', false);
        }
    });


    colorInput5.on('input', function () {
        if (colorInput5.val() !== '') {
            imgInput5.prop('required', true);
        } else {
            imgInput5.prop('required', false);
        }
    });


    imgInput6.on('input', function () {
        if (imgInput6.val() !== '') {
            colorInput6.prop('required', true);
        } else {
            colorInput6.prop('required', false);
        }
    });


    colorInput6.on('input', function () {
        if (colorInput6.val() !== '') {
            imgInput6.prop('required', true);
        } else {
            imgInput6.prop('required', false);
        }
    });


    imgInput7.on('input', function () {
        if (imgInput7.val() !== '') {
            colorInput7.prop('required', true);
        } else {
            colorInput7.prop('required', false);
        }
    });


    colorInput7.on('input', function () {
        if (colorInput7.val() !== '') {
            imgInput7.prop('required', true);
        } else {
            imgInput7.prop('required', false);
        }
    });



});

$(window).on("scroll", function(){
    // scrollHeight = $(document).height();
    // scrollPosition = $(window).height() + $(window).scrollTop();
    // footHeight = $("footer").innerHeight();
    // if (scrollHeight - scrollPosition <= footHeight) {
    //     // ページトップボタンがフッター手前に来たらpositionとfixedからabsoluteに変更
    //     $(".infoList").css({
    //     position: "absolute",
    //     bottom: "300px",
    //     });
    // } else {
    //     $(".infoList").css({
    //     position: "fixed",
    //     bottom: "0",
    //     });
    // }
})