brand = document.getElementById("brand")
model = document.getElementById("model")
type = document.getElementById("type")

cpu = document.getElementById("cpu")
gpu = document.getElementById("gpu")
mb = document.getElementById("mb")
ram = document.getElementById("ram")
case_ = document.getElementById("case")
psu = document.getElementById("psu")
fan = document.getElementById("fan")
drive = document.getElementById("drive")

button = document.getElementById("add")

cpu_socket = document.getElementById("cpu_socket")
cpu_usage = document.getElementById("cpu_usage")

gpu_lenght = document.getElementById("gpu_lenght")
gpu_slots = document.getElementById("gpu_slots")
gpu_usage = document.getElementById("gpu_usage")

mb_socket = document.getElementById("mb_socket")
mb_ram = document.getElementById("mb_ram")
mb_drive = document.getElementById("mb_drive")
mb_type = document.getElementById("mb_type")

ram_type = document.getElementById("ram_type")
ram_usage = document.getElementById("ram_usage")

psu_wattage = document.getElementById("psu_wattage")

fan_socket = document.getElementById("fan_socket")
fan_height = document.getElementById("fan_height")
fan_usage = document.getElementById("fan_usage")

case_mb_type = document.getElementById("case_mb_type")
case_gpu_lenght = document.getElementById("case_gpu_lenght")
case_slots = document.getElementById("case_slots")
case_fan_height = document.getElementById("case_fan_height")

drive_type = document.getElementById("drive_type")
drive_usage = document.getElementById("drive_usage")







async function update() {
    const res = await fetch("/api/current_update", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({"brand": brand.value, "model": model.value, "type": type.value})
    });
    const curent = await res.json();
    console.log(curent);

   
    const alertBox = document.getElementById("alert-msg");

    if (curent.result == "neplatny model nebo znacka") {
      alertBox.innerText = curent.result; 
      alertBox.style.display = "block";    
    
    
      alertBox.style.backgroundColor = curent.test === "uspesne nahrano" ? "#4CAF50" : "#f44336";

    
      setTimeout(() => {
          alertBox.style.display = "none";
      }, 3000);
}

    if (curent.test == "uspesne nahrano") {
        switch(type.value.toLowerCase()) {

            case "cpu":
                cpu_socket.value = curent.curent_socket;
                cpu_usage.value = curent.curent_usage;

                break

            case "gpu":
                gpu_lenght.value = curent.curent_lenght;
                gpu_slots.value = curent.curent_slots;
                gpu_usage.value = curent.curent_usage;

                break

            case "mb":
                mb_socket.value = curent.curent_socket;
                mb_ram.value = curent.curent_ram;
                mb_drive.value = curent.curent_drive;
                mb_type.value = curent.curent_type;

                break

            case "case":
                case_mb_type.value = curent.curent_mb_type;
                case_gpu_lenght.value = curent.curent_gpu_lenght;
                case_slots.value = curent.curent_slots;
                case_fan_height.value = curent.curent_fan_height;

                break

            case "psu":
                psu_wattage.value = curent.curent_wattage;

                break

            case "fan":
                fan_socket.value = curent.curent_socket;
                fan_height.value = curent.curent_height;
                fan_usage.value = curent.curent_usage;

                break
            case "ram":
                ram_type.value = curent.curent_type;
                ram_usage.value = curent.curent_usage;

                break

            case "drive":
                drive_type.value = curent.curent_type;
                drive_usage.value = curent.curent_usage;

                break
                
        }
    }
}

type.addEventListener("input", update)

 




type.addEventListener("input", function() {
    console.log(type.value)
    cpu.style.display = "none"
    gpu.style.display = "none"
    ram.style.display = "none"
    mb.style.display = "none"
    fan.style.display = "none"
    drive.style.display = "none"
    psu.style.display = "none"
    case_.style.display = "none"







    switch(type.value.toLowerCase()) {
        case "cpu":
            cpu.style.display = "block"
            break
        case "gpu":
            gpu.style.display = "block"
            break
        case "mb":
            mb.style.display = "block"
            break
        case "ram":
            ram.style.display = "block"
            break
        case "case":
            case_.style.display = "block"
            break  
        case "psu":
            psu.style.display = "block"
            break
        case "fan":
            fan.style.display = "block"
            break
        case "drive":
            drive.style.display = "block"
            break
    }
    
    
    



})



button.addEventListener("click", async() => {
    if (type.value.toLowerCase() == "cpu") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'cpu_socket':cpu_socket.value.toLowerCase(), 'cpu_usage':cpu_usage.value.toLowerCase()}
    }
    if (type.value.toLowerCase() == "gpu") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'gpu_lenght':gpu_lenght.value.toLowerCase(), 'gpu_slots':gpu_slots.value.toLowerCase(), 'gpu_usage':gpu_usage.value.toLowerCase()}
    }
    if (type.value.toLowerCase() == "mb") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'mb_type':mb_type.value.toLowerCase(), 'mb_socket':mb_socket.value.toLowerCase(), 'mb_ram':mb_ram.value.toLowerCase(), 'mb_drive':mb_drive.value.toLowerCase()}
    }        
    if (type.value.toLowerCase() == "case") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'case_slots':case_slots.value.toLowerCase(), 'case_mb_type':case_mb_type.value.toLowerCase(), 'case_gpu_lenght':case_gpu_lenght.value.toLowerCase(), 'case_fan_height':case_fan_height.value.toLowerCase()}
    }       
    if (type.value.toLowerCase() == "drive") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'drive_type':drive_type.value.toLowerCase(), 'drive_usage':drive_usage.value.toLowerCase()}
    }       
    if (type.value.toLowerCase() == "fan") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'fan_socket':fan_socket.value.toLowerCase(), 'fan_height':fan_height.value.toLowerCase(), 'fan_usage':fan_usage.value.toLowerCase()}
    }       
    if (type.value.toLowerCase() == "psu") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'psu_wattage':psu_wattage.value.toLowerCase()}
    }       
    if (type.value.toLowerCase() == "ram") {
        Select = {'brand':brand.value, 'model':model.value, 'type':type.value.toUpperCase(), 'ram_type':ram_type.value.toLowerCase(), 'ram_usage':ram_usage.value.toLowerCase()}
    }

const res = await fetch("/api/add", {
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

    alertBox.style.backgroundColor = res.ok ? "#4CAF50" : "#f44336";

    setTimeout(() => {
        alertBox.style.display = "none";
    }, 3000);
}
})  





