var is_clicked = false;

document.getElementById("like").onclick = add_rating;

function add_rating() {
    var num = parseInt(document.getElementById("rating_num").innerHTML);
    if (is_clicked == false) {
        document.getElementById("rating_num").innerHTML = num + 1;
        is_clicked = true;
    } else {
        document.getElementById("rating_num").innerHTML = num - 1;
        is_clicked = false;
    }
}
