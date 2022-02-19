function check_label(input_name) {
    let inputs = document.getElementsByName(input_name);
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i];
        let input_id = input.id;
        let label = document.getElementById('label' + input_id.replace('input', ''));
        if (input.checked) {
            label.classList.add('my-label');
        }
        else {
            label.classList.remove('my-label');
        }
    }

}
