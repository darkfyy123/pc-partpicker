del = document.getElementById("del")


del.addEventListener("click", async function() {
    const id_build = document.getElementById("build_id").value;
    console.log(id_build)
    const response = await fetch("/api/build_DELETE", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({'id_build': id_build})
    })
    const data = await response.json()
    console.log(data.message)

    const alertBox = document.getElementById("alert-msg");

    if (data.message) {
      alertBox.innerText = data.message; 
      alertBox.style.display = "block";    
    
    
      alertBox.style.backgroundColor = response.ok ? "#4CAF50" : "#f44336";

    
      setTimeout(() => {
          alertBox.style.display = "none";
      }, 3000);
}
})    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 