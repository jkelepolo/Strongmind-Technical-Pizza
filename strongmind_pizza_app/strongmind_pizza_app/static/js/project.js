/* Project specific Javascript goes here. */


function APICall(apirequest="", form, confirmation=""){
    
    if (confirmation != ""){
        var confirm_call = confirm(confirmation);
        if (!confirm_call){
            return false;
        }
    }

    $.ajax({
        data: $(form).serialize(), // get the form data
        type: "POST",
        url: apirequest,
        complete: function (response) {


        },
        
        // on success
        success: function (response) {
            $(form).append("<div class='alert alert-dismissible alert-success'>Action Success<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>");
            console.log(response);

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