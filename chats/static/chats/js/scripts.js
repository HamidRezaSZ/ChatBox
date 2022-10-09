import { getCookie } from './cookie.js';

$(document).ready(function () {
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    $('.input-group-append').click(function () {
        $.ajax({
            url: "/chats/message/create/",
            type: "POST",
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Accept", "*/*");
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            data: { 'message': $('textarea.type_msg').val(), 'username': $('.active_chat span').text() },
            dataType: "json"
        })
            .done(function () {
                console.log("Done")
            })

            .fail(function (jqXHR, textStatus, errorThrown) {
                console.log("Fail")
            })
    })
});