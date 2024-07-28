$(document).ready(function(){
  // 結果の件数
  const $count = $("#count");
  // ページ番号を増やす
  const $page = $("#page");

  // 全ての .productForm 要素を取得
  const forms = $("article .productForm");

  // 件数の読み取り
  const countPage = Math.trunc($count.text() / 50) + 1;


  const reviewStar = $(".star");



  // pageの中のボタンタグの設定
  let addButton = "";
  for (let i = 0; i < countPage; i++) {
    addButton += `<button class='form${i}'>${i + 1}</button>`;

    // フォームの表示制御
    if (i !== 0) {
      forms.eq(i).hide();
      
    }



  }

  

  // 設定したボタンの追加
  $page.html(addButton);

  let $pushButton = $("#page button");

  let last_count_button = 0;

  forms.each(function(index) {
    // console.log(index)
    let first_button = $(`.form${index}`);
    if (index == 0 || index == 1 || index == 2  ) {
      first_button.show();
      console.log(index)
    }
    else {
      first_button.hide();

    }
    last_count_button += 1;
  })



  // last_first_button = $(`.form${last_count_button - 1}`);
  // last_first_button.show();
  // console.log(last_count_button, "last");



  $pushButton.on("click", function() {
    // 押されたformを表示させるコード
    let showForm = $(this).attr("class");
    // console.log(this)
    // console.log(this)

    
    

    last_count_button = 0;
    forms.each(function(index) {
      if (index == showForm.slice(4)) {
        $(this).show();

        // 今押したボタンは表示
        let $this_button = $(`.form${index}`);
          $this_button.show();
          // console.log(index,"or")

        // console.log("show" + index);
      } else {
        $(this).hide();
          // console.log(this)
        // console.log("hide" + index);

        // 押されたボタンのひとつ前、一つ後、一番最初、一番最後を表示
        if (index == parseInt(showForm.slice(4)) - 1 || index == parseInt(showForm.slice(4)) - 2 || index == parseInt(showForm.slice(4)) + 1 || index == parseInt(showForm.slice(4)) + 2){
          // console.log(index,"or")
          let $this_button = $(`.form${index}`);
          $this_button.show();
          // console.log(showForm.slice(4), "plus")
          // console.log("show" + index);

        }
        else {
          let $this_button = $(`.form${index}`);
          // console.log("hide" + index);
          $this_button.hide();
          
        }
      }
      last_count_button = index
    });

    // let $this_button = $(`.form${last_count_button}`);
    // $this_button.show();
    // console.log("last", $this_index)

    $("html, body").animate({scrollTop : 0}, 1000);
  });

  const $NarrowDownButton = $(".NarrowDownButton");
  const $NarrowDownForm = $(".NarrowDown form");
  let narrowJudge = false;

  $NarrowDownButton.on("click", function() {
    if (narrowJudge) {
      $NarrowDownForm.css({
        "display":"none"
      });
      console.log(narrowJudge);
    } else {
      $NarrowDownForm.css({
        "display":"block"
      });
    }
    narrowJudge = !narrowJudge;
  });


  // $('.star').raty({
  //   // オプション設定
  //   // 星の数、評価を受け付けるかどうか、イベントの処理など
  //   // 詳細はraty.jsのドキュメントを参照
  // });
    
  

});
