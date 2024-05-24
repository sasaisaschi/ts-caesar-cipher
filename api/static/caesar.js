document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('caesarForm').addEventListener('submit', function(event) {
        event.preventDefault();

        var cipher_direction = document.getElementById('cipher_direction').value;
        var start_text = document.getElementById('start_text').value;
        var shift_amount = document.getElementById('shift_amount').value;

        fetch('/caesar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                cipher_direction: cipher_direction,
                start_text: start_text,
                shift_amount: shift_amount
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = data.result;
        });
    });
});