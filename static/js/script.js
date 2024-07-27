// アカウント詳細表示
const $account = $(".account");












// ボタン押したら項目増えるやつ
const $two = $(".two");


const $top1 = $(".top1");
const $top2 = $(".top2");
const $bottom1 = $(".bottom1");
const $bottom2 = $(".bottom2");

const $three = $(".three")


console.log("aaa")










// アカウント詳細表示








// ボタン押したら項目増えるやつ

$top2.hide();
$bottom2.hide();

$top1.on("click", function() {
    $three.css({"margin-top": "0"});
    $two.css({"height":"calc(100vh + 30px)"});
    $top2.show();//洋服表示
    $bottom2.hide();//ズボン非表示
    setTimeout(function() {
        $bottom2.removeClass("active");
        $top2.addClass("active");
    })
    
    console.log("aaa")
})

$bottom1.on("click", function() {
    $three.css({"margin-top": "0"});
    $two.css({"height":"calc(100vh + 30px)"});

    $bottom2.show();//ズボン表示
    $top2.hide();//洋服非表示
    setTimeout(function() {
        $top2.removeClass("active");
        $bottom2.addClass("active");
    })
    
    console.log("aaa")
})
