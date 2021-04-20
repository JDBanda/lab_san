$(function () {
    obtenerTotal();

    function obtenerTotal() {
        var tds = $('.subtotal')
        var ant = $('.anticipo')
        var acum = 0, acum2 = 0;
        for (let i = 0; i < tds.length; i++) {
            acum += Number.parseFloat($(tds[i]).attr('subtotal'));
            acum2 += Number.parseFloat($(ant[i]).attr('subtotal'));
        }
        $('#total-teorico').text("$" + acum);
        $('#anticipo-teorico').text("$" + acum2);
    }
})