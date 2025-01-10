// Get the initially selected country value
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}
// Event handler for the change of the country selection
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});