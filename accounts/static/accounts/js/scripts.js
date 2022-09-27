$(document).ready(function () {
    $('.fail').on('click', function () {
        $('#fail h1,#fail p,#fail .fail').css({ display: 'none' });

        $('#fail').animate({
            width: '0',
        }, 250, function () {
            $('#fail .icon').animate({
                borderRadius: '50%',
            }, 250, function () {

                $('#fail .icon').animate({
                    opacity: 0
                }, 250);
            });
        });
    });
    $('.succ').on('click', function () {
        $('#success h1,#success p,#success .succ').css({ display: 'none' });

        $('#success').animate({
            width: '0',
        }, 250, function () {
            $('#success .icon').animate({
                borderRadius: '50%',
            }, 250, function () {

                $('#success .icon').animate({
                    opacity: 0
                }, 250);
            });
        });
    });
});