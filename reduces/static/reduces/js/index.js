;(function($, undefined){
    $(document).ready(function() {
        setTimeout(function() {
            $('.message').slideUp("slow");
        }, 7000);

        $('#logo').on("mouseover", function() {
            $('#logo img').delay(300).animate({rotate: '20deg'}, 500);
        })

    });
})(jQuery);
