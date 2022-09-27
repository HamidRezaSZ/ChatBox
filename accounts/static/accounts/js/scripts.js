$(document).ready(function () {

    function setCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    $('#signup-btn').on('click', function () {
        $('.home-div').css({ display: 'none' })
        $('.signup-div').css({ display: 'block' })
        $('.home-btn').css({ display: 'block' })
    });

    $('#login-btn').on('click', function () {
        $('.home-div').css({ display: 'none' })
        $('.login-div').css({ display: 'block' })
        $('.home-btn').css({ display: 'block' })
    });

    $('.home-btn').on('click', function () {
        $('.home-div').css({ display: 'block' })
        $('.login-div').css({ display: 'none' })
        $('.signup-div').css({ display: 'none' })
        $('.home-btn').css({ display: 'none' })
    });

    $('.signup-form-btn').on('click', function () {
        $.post("/accounts/register/", $('.signup-form').serialize())

            .done(function () {
                $('#message-div').prepend(`
                                <section id="success">
                <div class="icon">
                    <i class="fa fa-smile-o" aria-hidden="true"></i>
                </div>
                <h1>Account successfully created!</h1>
                <i class="fa fa-times succ" aria-hidden="true"></i>
                </section>
                `).ready(function () {
                    setTimeout(function () {
                        $('section').fadeOut(400);
                    }, 4000);
                    $('section').on('click', 'i', (e) => {
                        $(e.target).parent().remove();
                    });
                })
            })

            .fail(
                function () {
                    $('#message-div').prepend(`
                    <section id="fail">
                    <div class="icon">
                        <i class="fa fa-frown-o" aria-hidden="true"></i>
                    </div>
                    <h1>Oh! Something went wrong!</h1>
                    <i class="fa fa-times fail" arfailia-hidden="true"></i>
                    </section>`).ready(function () {
                        setTimeout(function () {
                            $('section').fadeOut(400);
                        }, 4000);
                        $('section').on('click', 'i', (e) => {
                            $(e.target).parent().remove();
                        });
                    })
                }
            );
    });

    $('.login-form-btn').on('click', function () {
        $.post("/accounts/login/", $('.login-form').serialize())

            .done(function (data, textStatus, jqXHR) {
                $('#message-div').prepend(`
                            <section id="success">
            <div class="icon">
                <i class="fa fa-smile-o" aria-hidden="true"></i>
            </div>
            <h1>Logged in successfully!</h1>
            <i class="fa fa-times succ" aria-hidden="true"></i>
            </section>
            `).ready(function () {
                    setTimeout(function () {
                        $('section').fadeOut(400);
                    }, 4000);
                    $('section').on('click', 'i', (e) => {
                        $(e.target).parent().remove();
                    });
                });
                setCookie('AccessToken', 'Bearer ' + data.access);
                setCookie('RefreshToken', 'Bearer ' + data.refresh);
            })

            .fail(
                function () {
                    $('#message-div').prepend(`
                    <section id="fail">
                <div class="icon">
                <i class="fa fa-frown-o" aria-hidden="true"></i>
                </div>
                <h1>Oh! Something went wrong!</h1>
                <i class="fa fa-times fail" aria-hidden="true"></i>
                </section>`).ready(function () {
                        setTimeout(function () {
                            $('section').fadeOut(400);
                        }, 4000);
                        $('section').on('click', 'i', (e) => {
                            $(e.target).parent().remove();
                        });
                    })
                }
            );
    });

});