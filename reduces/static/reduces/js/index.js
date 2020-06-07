;(function($, undefined){
    $(document).ready(function() {
        setTimeout(function() {
            $('.message').slideUp("slow");
        }, 7000);

        if ($('.error_block').contents().length != 0) {
            $('.form').addClass("form_error");
        } else if ($('.error_block .help_list .help_list_item').contents().length != 0) {
            $('.form').addClass("form_error");
        } else if ($('.error').contents().length != 0) {
            $('.form').addClass("form_error");
        } else {
            $('.form').removeClass("form_error");
        }

        // if ($('.error_block .help_list .help_list_item').contents().length != 0) {
        //     $('.form').addClass("form_error");
        // } else {
        //     $('.form').removeClass("form_error");
        // }
        //
        // if ($('.error').contents().length != 0) {
        //     $('.form').addClass("form_error");
        // } else {
        //     $('.form').removeClass("form_error");
        // }

    });
})(jQuery);
