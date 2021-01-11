let img = document.querySelector('#changer')
let btn = document.querySelector('#btn')

if ("{{ message }}" === "blur") {
    btn.addEventListener('click', () => {
        img.src = "static/blurred.jpg";
    })
}else if ("{{ message }}" === "grayscale") {
    btn.addEventListener('click', () => {
        img.src = "static/grayscale.jpg";
    })
}else if ("{{ message }}" === "invert") {
    btn.addEventListener('click', () => {
        img.src = "static/inverted.jpg";
    })
}else if ("{{ message }}" === "reflect") {
    btn.addEventListener('click', () => {
        img.src = "static/reflected.jpg";
    })
}else if ("{{ message }}" === "recolor") {
    btn.addEventListener('click', () => {
        img.src = "static/_siggraph17.png";
    })
}else if ("{{ message }}" === "glitch") {
    btn.addEventListener('click', () => {
        img.src = "static/glitched.gif";
    })
}