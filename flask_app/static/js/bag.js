let count = 0;


function addBtn(a, b) {
    var price = document.getElementById("bag_item_price")
    var input = b.previousElementSibling;
    var value = parseInt(input.value,10);
    value = isNaN(value) ? 0 : value;
    
    value++;
    input.value = value;
}

function subtractBtn(a, b) {
    var input = b.nextElementSibling;
    var value = parseInt(input.value, 10);
    if (value > 1) {
    value = isNaN(value) ? 0 : value;
    value--;
    input.value = value;
    }
}



