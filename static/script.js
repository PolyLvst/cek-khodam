function cek_khodam() {
    event.preventDefault();
    var name_give = $("#name").val();
    if (name_give === ""){
        return;
    }
    $("#cekBtn").toggle();
    $("#ulangiBtn").toggle();
    $("#load-icon").toggle();
    $("#input-show").toggle();
    $("#result").empty();
    // Melakukan permintaan AJAX ke endpoint cek
    $.ajax({
        url: `/q?name=${name_give}`,
        method: 'GET',
        data: {},
        success: function (response) {
            $("#result").append(`<h1 class="is-size-2 has-text-centered has-text-khodam has-text-weight-bold mb-3">${response.khodam}</h1>`);
            $("#load-icon").toggle();
        },
    });
}
function enter_listener() {
    if (event.key === 'Enter') {
        cek_khodam()
    } else {
        return;
    }
}
function cek_ulangi_khodam_button_listener() {
    $("#cekBtn").click(function (event) {
        cek_khodam();
    });
    $("#ulangiBtn").click(function (event) {
        $("#cekBtn").toggle();
        $("#ulangiBtn").toggle();
        $("#input-show").toggle();
        $("#result").empty();
    });
}