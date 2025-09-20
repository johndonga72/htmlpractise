const john = setTimeout(function () { const transform = document.getElementById("title"); transform.style.color = 'red'; transform.style.fontSize = '5rem' }, 5000)

let k = function stop() {
    clearTimeout(john);
}