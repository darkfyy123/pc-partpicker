brand = document.getElementById("brand")
model = document.getElementById("model")
type = document.getElementById("type")


button = document.getElementById("del")

















button.onclick =  async function() {



    Select = {Brand: brand.value, Model: model.value, Type: type.value.toUpperCase()}



const res = await fetch("/api/del", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(Select)
});

const answer = await res.json();
const alertBox = document.getElementById("alert-msg");

if (answer.result) {
    alertBox.innerText = answer.result;
    alertBox.style.display = "block";

    // Pokud HTTP status je 200-299, bude zelená, jinak červená
    alertBox.style.backgroundColor = res.ok ? "#4CAF50" : "#f44336";

    setTimeout(() => {
        alertBox.style.display = "none";
    }, 3000);
}