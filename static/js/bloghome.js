function handleCardClick(blogid){
    window.location.href= `/bloghome/${blogid}`
};

const btn = document.querySelector("#btn");
let body = document.querySelector("body");

if (localStorage.getItem("theme") === "dark"){
    body.classList.add("dark");
    btn.innerHTML = "Light";
} else {
    body.classList.remove("dark");
    btn.innerHTML = "Dark";
}

btn.addEventListener("click", () => {
    if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        btn.innerHTML = "Dark";
        localStorage.setItem("theme","light");
    } else {
        body.classList.add("dark");
        btn.innerHTML = "Light";
        localStorage.setItem("theme" , "dark");
    }
})

// const buttons = document.querySelector("#button");
// let body1 = document.querySelector("body");


// if (localStorage.getItem("theme") === "dark") {
//     body.classList.add("dark-theme");
//     buttons.innerHTML = "Alice Mode";
// } else {
//     body.classList.remove("dark-theme");
//     buttons.innerHTML = "Dark Mode";
// }

// buttons.addEventListener("click", () => {
//     if (body.classList.contains("dark-theme")) {
//         body.classList.remove("dark-theme");
//         buttons.innerHTML = "Dark Mode";
//         localStorage.setItem("theme", "light"); 
//     } else {
//         body.classList.add("dark-theme");
//         buttons.innerHTML = "Alice Mode";
//         localStorage.setItem("theme", "dark"); 
//     }
// })
