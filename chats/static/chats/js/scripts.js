import { getCookie } from './cookie.js';

$(document).ready(function () {
    $('#action_menu_btn').click(function () {
        $('.action_menu').toggle();
    });

    $('.input-group-append').click(function () {
        $.ajax({
            url: "/chats/message/",
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

    $('.contacts').on('click', 'li', (e) => {
        if ($('.active_chat span')[0].innerText != $($(e.currentTarget).children().children()[1]).children()[0].innerText) {
            $('.chat-page').css({ display: 'block' });
            $('.active_chat span')[0].innerText = $($(e.currentTarget).children().children()[1]).children()[0].innerText;
            $('.img-chat').attr('src', $($($(e.currentTarget).children().children()[0]).children()[0]).attr('src'));

            $.ajax({
                url: "/chats/message/?user=" + $('.active_chat span')[0].innerText,
                type: "GET",
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("Accept", "*/*");
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },

            })
                .done(function (data) {
                    $.each(data, function (index, value) {
                        $('.message-div').append(`<div class="d-flex justify-content-start mb-4">
                <div class="img_cont_msg">
                  <img
                    src=""
                    class="rounded-circle user_img_msg"
                  />
                </div>
                <div class="msg_cotainer">
                  ${value.message}
                  <span class="msg_time">${value.created_at}</span>
                </div>
              </div>`)
                    });
                })

                .fail(function (jqXHR, textStatus, errorThrown) {
                    console.log("Fail")
                })
        }
    });

});