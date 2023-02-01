$( document ).ready(function() {
    $('#submit-order').submit( function(e) {
        e.preventDefault();
        let csrftoken = $.cookie('csrftoken');
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        let form_data = $('#submit-order').serializeArray().reduce(function(obj, item) {
            obj[item.name] = item.value;
            return obj;
        }, {});
        console.log(form_data);
        // let payload = {
        //     "customer":"test",
        //     "product":1,
        //     "email":"email@mail.com"
        // };
        
        $.ajax({
                 url : "",
                 contentType: "application/json",
                 data:JSON.stringify(form_data),
                 dataType: "json",
                 type: "POST",
                 success: function (arg) {
                        
                          alert(data);
                        },
                failure: function(errMsg){
                    alert(errMsg);
                }
                     });
                });
            });