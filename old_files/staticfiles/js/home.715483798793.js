$(document).ready(function() {

    var compare_os_hash = [],
        compare_object_hash = {},
        postUrl = '/analyser/',
        $checkboxVar = $('input[type="checkbox"]');

        $(".Packages-button").on('click', function() {
            if (Object.keys(compare_object_hash).length == 1 && compare_object_hash['object'] !== 'packages') {
                compare_object_hash['object'] = 'packages';
                $('.Packages-button').addClass("active");
                $checkboxVar.attr("checked", "checked");
                $('.Users-button').removeClass("active");
                $checkboxVar.removeAttr("checked", "checked");
                $('.Volumes-button').removeClass("active");
                $checkboxVar.attr("checked", "checked");
            } else if (Object.keys(compare_object_hash).length == 0) {
               compare_object_hash['object'] = 'packages';
               $('.Packages-button').addClass("active");
               $checkboxVar.attr("checked", "checked");
            }
        });

        $(".Users-button").on('click', function() {
            if (Object.keys(compare_object_hash).length == 1 && compare_object_hash['object'] !== 'users') {
                compare_object_hash['object'] = 'users';
                $('.Users-button').addClass("active");
                $checkboxVar.attr("checked", "checked");
                $('.Packages-button').removeClass("active");
                $checkboxVar.removeAttr("checked", "checked");
                $('.Volumes-button').removeClass("active");
                $checkboxVar.attr("checked", "checked");
            }  else if (Object.keys(compare_object_hash).length == 0) {
                compare_object_hash['object'] = 'users';
                $('.Users-button').addClass("active");
                $('input[type="checkbox"]').attr("checked", "checked");
            }
        });
        $(".Volumes-button").on('click', function() {
            if (Object.keys(compare_object_hash).length == 1 && compare_object_hash['object'] !== 'volumes') {
                compare_object_hash['object'] = 'volumes';
                $('.Volumes-button').addClass("active");
                $('input[type="checkbox"]').attr("checked", "checked");
                $('.Packages-button').removeClass("active");
                $('input[type="checkbox"]').removeAttr("checked", "checked");
                $('.Users-button').removeClass("active");
            }  else if (Object.keys(compare_object_hash).length == 0) {
                compare_object_hash['object'] = 'volumes';
                $('.Volumes-button').addClass("active");
                $('input[type="checkbox"]').attr("checked", "checked");
            }
        });
        $(".Debian-button").on('click', function(event) {
            event.preventDefault();
            var exist = false;
            for (var i = 0; i < compare_os_hash.length; i++) {
                if (compare_os_hash[i] == 'debian') {
                    exist = true;
                }
            }
            setArray(exist, 'debian');
        });

        $(".Ubuntu-button").on('click', function(event) {
            event.preventDefault();
            var exist = false;
            for (var i = 0; i < compare_os_hash.length; i++) {
                if (compare_os_hash[i] == 'ubuntu') {
                    exist = true;
                    delete compare_os_hash[i];
                }
            }
            setArray(exist, 'ubuntu');
        });

        $(".Mac-button").on('click', function(event) {
            event.preventDefault();
            var exist = false;
            for (var i = 0; i < compare_os_hash.length; i++) {
                if (compare_os_hash[i] == 'mac') {
                    exist = true;
                    delete compare_os_hash[i];
                }
            }
            setArray(exist, 'mac');
        });

        $(".Centos-button").on('click', function(event) {
            event.preventDefault();
            var exist = false;
            for (var i = 0; i < compare_os_hash.length; i++) {
                if (compare_os_hash[i] == 'centos') {
                    exist = true;
                    delete compare_os_hash[i];
                }
            }
            setArray(exist, 'centos');
        });

        $(".next-page-button").on('click', function() {
           if (compare_os_hash.length >= 2 && Object.keys(compare_object_hash).length == 1) {
               console.log("Next button clicked");
               $.ajax({
                url: postUrl,
                type: "POST",
                data: {object: compare_object_hash, os_types: compare_os_hash},

                success: function () {
                    console.log("success"); // another sanity check
                },
                // handle a non-successful response
                error: function (xhr) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }

               });

                setTimeout(function() {
                    window.location.href = postUrl;
                }, 300);

           } else {
               $('.alert-danger').css("display", "block");
               return false;
           }
        });

        function setArray(boolean, val){
            var newVal = '.' + val.charAt(0).toUpperCase() + val.slice(1) + '-button';
            if (boolean !== true) {
             compare_os_hash[compare_os_hash.length] = val;
              $(newVal).addClass("active");
              $checkboxVar.attr("checked", "checked");
            }
            else if (boolean == true) {
                if (compare_os_hash.indexOf(val) == 0) {
                    compare_os_hash.shift();
                } else {
                    compare_os_hash.splice(compare_os_hash.indexOf(val), 0);
                    compare_os_hash = compare_os_hash.filter(Boolean);
                }
                $(newVal).removeClass("active");
                $checkboxVar.removeAttr("checked");
            }
        };
});