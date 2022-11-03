/* Project specific Javascript goes here. */


function APICall(apirequest="", form, confirmation=""){
    
    if (confirmation != ""){
        var confirm_call = confirm(confirmation);
        if (!confirm_call){
            return false;
        }
    }

    var ajax_data = $(form).serializeArray();

    if ($(".checkbox-group:checked").length > 0){

        var groups = {}

        $(".checkbox-group:checked").each(function(){

            if ($(this).attr("name") in groups){
                groups[$(this).attr("name")].push($(this).val());
            }
            else{
                groups[$(this).attr("name")] = [];
                groups[$(this).attr("name")].push($(this).val());
            }

        });

        ajax_data.push({name:"checkbox_groups", value:JSON.stringify(groups)});
    
    }

    $.ajax({
        data: ajax_data, // get the form data
        type: "POST",
        url: apirequest,
        complete: function (response) {


        },
        
        // on success
        success: function (response) {
            console.log(response);

            if (typeof response == 'object') {

                if ("toast" in response) {
                    var alert_type = response["toast"][0]
                    var alert_message = response["toast"][1]

                    $(form).append("<div class='alert alert-"+alert_type+" alert-dismissible'>"+alert_message+"<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>");
                
                }
                else{
                 $(form).append("<div class='alert alert-dismissible alert-success'>Action Success<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>");

                }

            }

            if("refresh" in response){
                window.location.href = window.location.href;
          
            } 

        },
        // on error
        error: function (response) {
            // alert the error if any error occured
            $(form).append("<div class='alert alert-dismissible alert-danger'>Action Failed<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>");
            console.log(response);
            return false;
        }
    });

    return true;
}