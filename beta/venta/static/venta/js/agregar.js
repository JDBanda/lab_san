//variables globales
var servicio, descuento, medico, cantidad;
var suma = 0;
var bandera = true;
var cont = 0;
//Esperando a que el documento cargue para después ejecutar jQuery
$(function () {
    //RECUPERAR VALORES DE LA VENTANA MODAL
    //valores del servicio
    function recuperarDatos() {
        servicio = []; //id, nombre y precio
        servicio.push($('#select-servicio>option:checked').val());
        servicio.push($('#select-servicio>option:checked').text());
        servicio.push($('#select-servicio>option:checked').attr('price'));
        //valor de descuento
        descuento = $('#modal-descuento').val();
        //Valores del médico
        medico = [] //id, nombre
        medico.push($('#select-medico>option:checked').val());
        medico.push($('#select-medico>option:checked').text());
        //valor de cantidad
        cantidad = $('#modal-cantidad').val();
    }

    //BOTÓN del modal, básicamente añade renglones a la tabla que después serán añadidos a la bd
    //var table = document.querySelector('#table-renglon>tbody')
    //Crear evento en el boton modal para agregar los datos a la tabla
    $('#obtener-monto').click(function () {
        //añadir uno al contador de filas
        cont++;
        //llamando a la función
        recuperarDatos()
        //Creando elementos
        var elements = '<tr id="tr-' + cont + '">';
        var monto = Number.parseFloat(cantidad) * Number.parseFloat(servicio[2] - servicio[2] * (descuento / 100));
        elements += '<td><button class="btn btn-danger"><i class="bx bxs-trash-alt">' +
            '</i></button><button class="btn btn-warning"><i class="bx bxs-edit-alt"></i></button></td >' +
            '<td medico="' + medico[0] + '" >' + medico[1] + '</td>' +
            '<td servicio="' + servicio[0] + '" >' + servicio[1] + '</td>' +
            '<td cantidad="' + cantidad + '">' + cantidad + '</td>' +
            '<td>$' + servicio[2] + '</td>' +
            '<td descuento="' + descuento + '" >%' + descuento + '</td>' +
            '<td monto="' + monto + '" class="monto">$<span>' + monto + '</span></td>';
        elements += "</tr>";
        //agregar al tbody
        $('#table-renglon').append(elements);
        //Funciones
        total();
        eliminar();
        actualizar();
    });

    //sumar los montos
    function total() {
        suma = 0;
        if ($('.monto>span').length) {
            $('.monto>span').each(function () {
                suma += Number.parseFloat($(this).text());
                //console.log($(this).text);
            });
        }
        $('#sumaTotal').text("Total a pagar: $" + suma)
        $('#sumaTotal').attr('suma', suma)
    }

    //Eliminar renglon
    function eliminar() {
        $('.btn-danger').each(function () {
            $(this).on("click", function () {
                $(this).parent().parent().remove();
                total();
            });
        });
    }

    //Actualizar el renglón
    function actualizar() {
        $('.btn-warning').each(function () {
            $(this).on("click", function () {
                //modo editar
                bandera = false;
                //Obteniendo el tr que contiene al botón
                var tr = $(this).parent().parent();
                //Colocando al select de servicios la opción del td
                $("#select-medico").val($(tr).find("td[medico]").attr("medico"));
                $("#select-servicio").val($(tr).find("td[servicio]").attr("servicio"));
                $("#modal-cantidad").val($(tr).find("td[cantidad]").attr("cantidad"));
                $("#modal-descuento").val($(tr).find("td[descuento]").attr("descuento"));
                //Aparecer la modal
                $('#exampleModal').modal('show');
                //Cambiar su botón
                editarTr($(tr).attr("id"));
                obtenerRenglones();
            });
        });

        function editarTr(trId) {
            $('#editar-renglon').on("click", function () {
                //actualizando contenido de la fila actual
                //console.log(trId);
                recuperarDatos();
                //Datos del medico
                $('#' + trId + '>td[medico]').text(medico[1]);
                $('#' + trId + '>td[medico]').attr("medico", medico[0]);
                //Datos del servicio
                $('#' + trId + '>td[servicio]').text(servicio[1]);
                $('#' + trId + '>td[servicio]').attr("servicio", servicio[0]);
                //Datos de cantidad
                $('#' + trId + '>td[cantidad]').text(cantidad);
                $('#' + trId + '>td[cantidad]').attr("cantidad", cantidad);
                //Datos de descuento
                $('#' + trId + '>td[descuento]').text("%" + descuento);
                $('#' + trId + '>td[descuento]').attr("descuento", descuento);
                //Monto
                var monto = Number.parseFloat(cantidad) * Number.parseFloat(servicio[2] - servicio[2] * (descuento / 100));
                $('#' + trId + '>td[monto]').text("$" + monto);
                $('#' + trId + '>td[monto]').attr("monto", monto);
                total();
            });
        }


    }

    //Solicitud AJAX de tipo POST para guardar la nota
    $('#nota').submit(function (e) {
        var url = $('#nota').attr('action_url')
        //Datos que se pasan para guardar de la nota
        const postData = {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
            NotaPaciente: $('#NotaPaciente').val(),
            NotaFecha: $('#NotaFecha').val(),
            NotaModoPago: $('#NotaModoPago').val(),
            NotaPago: $('#NotaPago').val(),
            NotaStatus: $('#NotaStatus').val(),
            NotaRecibe: $('#NotaRecibe').val(),
            NotaUsuario: $('#usuario').attr('user'),
            NotaTotal: $('#sumaTotal').attr('suma'),
            renglones: obtenerRenglones(),
        };
        $.post(url, postData, function (response) {
            var r = confirm("Deseas imprimir la nota")
            if (r) {
                window.location.href = "/caja/nota/pdf"
            } else {
                window.location.href = "/caja/"
            }
        });
        e.preventDefault();
    });

    function obtenerRenglones() {
        //Gracias al valor de cont, se sabe cuantos renglones hay
        // y se puede recorrer cada tr en busca de los datos
        var a = [];
        for (let i = 1; i <= cont; i++) {
            //Solo no se pasa el id de la nota, porque aun no ha sido creada
            var elemento = {
                "cantidad": $('#tr-' + i + '>td[cantidad]').attr('cantidad'),
                "servicio": $('#tr-' + i + '>td[servicio]').attr('servicio'),
                "descuento": $('#tr-' + i + '>td[descuento]').attr('descuento'),
                "medico": $('#tr-' + i + '>td[medico]').attr('medico'),
                "monto": $('#tr-' + i + '>td[monto]').attr('monto'),
            };
            a.push(elemento);
        }
        return JSON.stringify(a);
    }
})