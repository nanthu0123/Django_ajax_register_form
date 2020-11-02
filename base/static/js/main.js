// jquery form validation

$.validator.setDefaults({
    submitHandler: function () {
        // jquery ajax method for send form data to server
        $.ajax({
            type: 'POST',
            url: '/register/',
            headers: {
                "X-CSRFToken": '{{csrf_token}}'
            },

            data: $('#register_form').serialize(),

            success: function () {
                alert('user registered!')
            }
        });
    }
})

$('#register_form').validate({
    rules: {
        username: 'required',
        email: {
            required: true,
            email: true
        },
        password1: {
            required: true,
            minlength: 4
        },
        password2: {
            required: true,
            minlength: 4,
            equalTo: '#password1'

        },
        datefilter: 'required',
    },

    messages: {
        username: 'user name is mandatory',
        email: {
            required: 'email address is mandatory',
            email: 'enter valid email address'
        },
        password1: {
            required: 'password is mandatory',
            minlength: 'enter atleast 4 char'

        },
        password2: {
            required: 're-enter the password',
            minlength: 'enter atleast 4 char',
            equalTo: 'password does not match'

        },
        datefilter: 'date is mandatory',
    }
});