// スライド
$(".slider1").slick({
    // autoplay: true,       //自動再生
    // autoplaySpeed: 2000,  //自動再生のスピード
    // speed: 800,           //スライドするスピード
    // dots: true,           //スライド下のドット
    arrows: false,         //左右の矢印
    // infinite: true,       //永久にループさせる
    autoplay: true,         //自動再生
    autoplaySpeed: 3,       //自動再生のスピード
    speed: 2500,            //追加（スライドスピード
    slidesToShow:3.0,        //追加（スライドの1スライドごとの表示枚数
    // cssEase: "linear",      //追加（スライドの動きを等速に
    pauseOnHover: true,    //追加（ホバーしても止まらないように
    pauseOnFocus: false,    //追加（フォーカスしても止まらないように
})

$(".slider2").slick({
    // autoplay: true,       //自動再生
    // autoplaySpeed: 2000,  //自動再生のスピード
    // speed: 800,           //スライドするスピード
    // dots: true,           //スライド下のドット
    // arrows: true,         //左右の矢印
    // infinite: true,       //永久にループさせる
    autoplay: true,         //自動再生
    autoplaySpeed: 3,       //自動再生のスピード
    speed: 100,            //追加（スライドスピード
    slidesToShow:4.0,        //追加（スライドの1スライドごとの表示枚数
    cssEase: "linear",      //追加（スライドの動きを等速に
    pauseOnHover: true,    //追加（ホバーしても止まらないように
    pauseOnFocus: false,    //追加（フォーカスしても止まらないように
})