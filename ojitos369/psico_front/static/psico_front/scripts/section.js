// just can select n options from a checkbox group

const check_selected = (checkbox_name, n) => {
    let selected = 0;
    let checkboxes = document.getElementsByName(checkbox_name);

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            selected++;
        }
    }
    if (selected > n) {
        let aviso = document.getElementById('select_alert');
        // get half of the width and height of the screen
        let x = window.innerWidth / 2;
        let y = window.innerHeight / 2;
        aviso.style.top = (y - aviso.offsetHeight / 4) + 'px';
        aviso.classList.remove('select_alert');
        aviso.classList.add('select_alert_2');
        setTimeout(() => {
            aviso.classList.remove('select_alert_2');
            aviso.classList.add('select_alert');
        }, 1000);
        for (let i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = false;
        }
    }

}