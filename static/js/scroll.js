// スクロールトップのリンクがクリックされたときの処理
document.getElementById('scroll-to-top').addEventListener('click', function (e) {
    e.preventDefault(); // デフォルトのクリック動作をキャンセル
    scrollToTop(); // スクロールトップの関数を呼び出し
});

const scroll_top_button = document.getElementById("scroll_top_button");

document.getElementById("scroll-to-top").addEventListener("mouseenter", function() {
    scroll_top_button.setAttribute("src", "static/images/logo/okiteru.png");
});

document.getElementById("scroll-to-top").addEventListener("mouseleave", function() {
    scroll_top_button.setAttribute("src", "static/images/logo/neteru.png")
})

// スクロールトップの関数
function scrollToTop() {
    // スクロール位置をトップに移動するアニメーション
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // スムーススクロールを有効にする
    });
}