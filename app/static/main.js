$(document).ready(function() {
    let inputIndex = 1;

    $('#add-input').click(function() {
        $('#inputs').append('<input type="text" name="input_' + inputIndex + '">');
        inputIndex++;
    });

    $('#dynamic-form').submit(function(event) {
        event.preventDefault();
        let recordId = $('#record-id').val();
        $.ajax({
            url: '/',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert('Данные сохранены: ' + JSON.stringify(response));
            }
        });
    });
});
