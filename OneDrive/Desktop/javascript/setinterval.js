const Animator = setInterval(sampleAnimation, 100);
let a = 0;
function sampleAnimation() {
    a = a + 1;
    const textanimation = document.getElementById('h1');
    textanimation.style.fontSize = a + 'rem';
}
