let name = prompt("enter your name")
let marks = prompt("enter your marks")
switch (true) {
    case marks > 90 && marks <= 100:
        result = "great you are the topper"
        break;
    case marks >= 65 && marks <= 90:
        result = "congratualitions you got first class"
        break;
    case marks > 40 && marks <= 65:
        result = "you got second class"
        break;
    case marks > 40 && marks <= 65:
        result = "you got second class"
        break;
    default:
        result = "please enter your marks"
        break

}
document.write("hello" + name + "<h2>" + result + "</h2>")
