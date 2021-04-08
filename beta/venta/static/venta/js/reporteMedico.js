$(function () {
    obtenerComisiones();
    obtenerTotal();

    function obtenerComisiones() {
        var tds = $('[comision]')
        for (let i = 0; i < tds.length; i++) {
            var valor = $(tds[i]).attr('comision');
            var monto = $(tds[i]).attr('monto');
            var x = Number.parseFloat(valor / 100) * Number.parseFloat(monto)
            $(tds[i]).parent().find(".subtotal").text(x)
        }
    }

    function obtenerTotal() {
        var tds = $('.subtotal')
        var acum = 0;
        for (let i = 0; i < tds.length; i++) {
            acum += Number.parseFloat($(tds[i]).text());
        }
        $('.total>p').text("Total: $" + acum)
    }

})