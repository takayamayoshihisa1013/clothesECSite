document.addEventListener("DOMContentLoaded", function () {


    var address_check_tag = document.querySelectorAll("input[name=address_check]");
    const h_adr = document.querySelector(".h-adr");

    address_check_tag.forEach(function(radio) {
        radio.addEventListener("change", function()  {
            var address_check = this.value;
            console.log(address_check)
            if (address_check == "on") {
                h_adr.style.display = "block"
            }
            else {
                h_adr.style.display = "none"
            }
        })
    })

    


    const kart_click = document.getElementById("kart_click");
    const kart = document.getElementById("kart_contents");
    const buy_click = document.getElementById("buy_click");
    const buy = document.getElementById("buy_contents");



    kart_click.addEventListener("click", function() {
        console.log("kart");
        kart.style.display = "block";
        buy.style.display = "none";
        kart_click.style.backgroundColor = "#ffff";
        buy_click.style.backgroundColor = "#e6e6e6";
        kart_click.style.border = "1px solid#c0c0c0";
        buy_click.style.border = "none";
    })

    buy_click.addEventListener("click", function() {
        console.log("buy");
        kart.style.display = "none";
        buy.style.display = "block";
        kart_click.style.backgroundColor = "#e6e6e6";
        buy_click.style.backgroundColor = "#ffff";
        buy_click.style.border = "1px solid#c0c0c0";
        kart_click.style.border = "none";
    })


    // 各数量入力要素とイベントリスナーを取得
    var quantityInputs = document.querySelectorAll('.product-quantity');

    // 各チェックボックス要素とイベントリスナーを取得
    var checkBoxes = document.querySelectorAll('input[type="checkbox"]');

    // イベントリスナーを各数量入力要素に追加
    quantityInputs.forEach(function (quantityInput) {
        quantityInput.addEventListener('change', updateSubtotal);
    });

    // イベントリスナーを各チェックボックス要素に追加
    checkBoxes.forEach(function (checkBox) {
        checkBox.addEventListener('change', updateSubtotal);
    });

    function updateSubtotal() {
        var subtotal = 0;

        // 各商品ごとに小計を計算し、合計に加算
        document.querySelectorAll('.cart-item').forEach(function (cartItem, index) {
            var checkBox = document.getElementById('check' + index);

            // チェックボックスが選択されている場合のみ計算
            if (checkBox && checkBox.checked) {
                var quantity = parseInt(cartItem.querySelector('.product-quantity').value.split("_")[0].substring(5,6));
                console.log(cartItem.querySelector('.product-quantity').value.split("_")[0].substring(5,6))
                var unitPrice = parseInt(cartItem.querySelector('.item-total').innerText.replace('￥', '').replace(',', ''));
                subtotal += quantity * unitPrice;
            }
        });

        // 合計金額を表示
        var subtotalElement = document.getElementById('subtotal-value');
        subtotalElement.innerText = '￥' + subtotal.toLocaleString(); // 金額をカンマ区切りにする場合
    }
});
