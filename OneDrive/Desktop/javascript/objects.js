const john = {
    name: "John Doe",
    age: 30,
    isEmployed: true,
    skills: ["JavaScript", "HTML", "CSS"],
    address: {
        street: "123 Main St",
        city: "Anytown",
        country: "USA"
    },
}
document.write(john.address.city + "<br>");

let hi = new Object();
hi.name = "Hello World";
document.write(hi.name);