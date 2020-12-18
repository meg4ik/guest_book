'use strict';

    (function (window, document, $) {
        function sendRequest() {
            var request = $.ajax({
                url: 'http://127.0.0.1:5000/comment/',
                data : $("#reqform"),
                dataType: 'json'
            });

            request.done(function (data, textStatus, jqXHR) {
                console.log("done!")
            });

            request.fail(function (jqXHR, textStatus, errorThrown) {
                console.log("fail!")
            });
        }

        $(document).ready(function() {
            $('#reqform').sumbit(function() {
                sendRequest();
            });
        });
    })(window, document, jQuery);