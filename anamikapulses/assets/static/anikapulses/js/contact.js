$(document).ready(function(){
    // Limit input for age field
    $('#age').unbind('keyup change input paste').bind('keyup change input paste', function(e){
        var $this = $(this);
        var val = $this.val();
        var maxCount = 2;
        if(val.length > maxCount){
            $this.val(val.substring(0, maxCount));
        }
    });
  
    // Scroll to top behavior
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 100) {
            $('#return-to-top').fadeIn(200);
        } else {
            $('#return-to-top').fadeOut(200);
        }
    });
  
    $('#return-to-top').click(function() {
        $('body,html').animate({scrollTop: 0}, 500);
    });
  
    // File input behavior
    $(".custom-file-input").on("change", function() {
      var fileName = $(this).val().split("\\").pop();
      $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
    });
  
    // Validate file extension
    $('#validatedCustomFile').change(function () {
        var fileExtension = ['doc', 'pdf', 'docx'];
        if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
            $('.file-error').html("<div class='file-error'>Only pdf, doc, and docx files are allowed</div>");
            this.value = ''; // Clear file input
        } else {
            $('.file-error').html(''); // Clear error if valid
        }
    });
    
  
    // Form validation rules
    $("#contactusformcar").validate({
        errorElement: "div",
        rules: {
            name: {
                required: true,
            },
            email_id: {
                required: true,
            },
            contact_no: {
                required: true
            },
            area_of_interest: {
                required: true
            },
            message: {
                required: true
            },
            document: {
                required: function() {
                  // File upload is required only if "Careers" (value 1) is selected in Area of Interest
                  return $('#your-sud').val() === '1';
                }
              }
        },
        submitHandler: function(form) {
          // Captcha validation
          if (grecaptcha.getResponse() === "") {
            $('.catcha-error').html('<span class="error" style="color:#555555">Please Select Captcha</span>');
            return false;
          } else {
            $('.catcha-error').html('');
  
            // Serialize form data including file (use FormData for file uploads)
            var formData = new FormData(form);
  
            // Submit form via AJAX
            $.ajax({
              type: "POST",
              url: "/lead-create/",
              data: formData,
              processData: false,  // Important for file upload
              contentType: false,  // Important for file upload
              success: function (data) {
                if (data) {
                    $('#msg').html('<span>Thank you, Our Team will contact you soon!</span>');
              $('#msg').delay(3000).fadeOut();

              // Reset the form
              $("#contactusformcar")[0].reset();

              // Manually reset the file input field
              $('#validatedCustomFile').val(''); 

              // Reset reCAPTCHA
              grecaptcha.reset();

              // Optionally hide the file upload section if "Careers" is not selected
              $('#file-upload-section').hide();
                }
              },
            });
          }
        },
        messages: {
            document: {
              required: "Please upload a file if you are applying for Careers."
            }
        }
    });
  
    // Ensure CAPTCHA is selected before form submission
    jQuery('#contactusformcar').on('submit', function(e) {
        if(grecaptcha.getResponse() == "") {
            $('.catcha-error').html('<span class="error" style="color:#555555">Please Select Captcha</span>');
            e.preventDefault();
        }
    });
  });
  