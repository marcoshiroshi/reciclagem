$(document).ready(function() {

    $('.date').mask('00/00/0000');
    $('.datetime').mask('00/00/0000 00:00:00');
    $('.phone').mask('(00) 00000-0000');
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.cep').mask('00000000', {reverse: true});
    $('.cep_mask').mask('00000-000', {reverse: true});

});