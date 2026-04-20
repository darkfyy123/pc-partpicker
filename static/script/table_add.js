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

gpu_length = document.getElementById("gpu_length")
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
case_gpu_length = document.getElementById("case_gpu_length")
case_slots = document.getElementById("case_slots")
case_fan_height = document.getElementById("case_fan_height")

drive_type = document.getElementById("drive_type")
drive_usage = document.getElementById("drive_usage")




type.addEventListener("input", function() {
    const selectedType = type.value.toLowerCase();
    console.log(selectedType);

    const sections = [cpu, gpu, ram, mb, fan, drive, psu, case_];
    sections.forEach(s => s.style.display = "none");

    switch (selectedType) {
        case "cpu":
            cpu.style.display = "block";
            break;
        case "gpu": 
            gpu.style.display = "block";   
            break;
        case "mb":    
            mb.style.display = "block";    
            break;
        case "case":  
            case_.style.display = "block"; 
            break;
        case "drive": 
            drive.style.display = "block"; 
            break;
        case "fan":   
            fan.style.display = "block";   
            break;
        case "psu":   
            psu.style.display = "block";   
            break;
        case "ram":   
            ram.style.display = "block";   
            break;
    }
});

button.addEventListener("click", async () => {
    
    let Select = {
        brand: brand.value,
        model: model.value,
        type: type.value.toUpperCase()
    };

    const typeKey = type.value.toLowerCase();

    switch (typeKey) {
        case "cpu":
            Select.cpu_socket = cpu_socket.value.toLowerCase();
            Select.cpu_usage = cpu_usage.value.toLowerCase();
            break;
        case "gpu":
            Select.gpu_length = gpu_length.value.toLowerCase();
            Select.gpu_slots = gpu_slots.value.toLowerCase();
            Select.gpu_usage = gpu_usage.value.toLowerCase();
            break;
        case "mb":
            Select.mb_type = mb_type.value.toLowerCase();
            Select.mb_socket = mb_socket.value.toLowerCase();
            Select.mb_ram = mb_ram.value.toLowerCase();
            Select.mb_drive = mb_drive.value.toLowerCase();
            break;
        case "case":
            Select.case_slots = case_slots.value.toLowerCase();
            Select.case_mb_type = case_mb_type.value.toLowerCase();
            Select.case_gpu_length = case_gpu_length.value.toLowerCase();
            Select.case_fan_height = case_fan_height.value.toLowerCase();
            break;
        case "drive":
            Select.drive_type = drive_type.value.toLowerCase();
            Select.drive_usage = drive_usage.value.toLowerCase();
            break;
        case "fan":
            Select.fan_socket = fan_socket.value.toLowerCase();
            Select.fan_height = fan_height.value.toLowerCase();
            Select.fan_usage = fan_usage.value.toLowerCase();
            break;
        case "psu":
            Select.psu_wattage = psu_wattage.value.toLowerCase();
            break;
        case "ram":
            Select.ram_type = ram_type.value.toLowerCase();
            Select.ram_usage = ram_usage.value.toLowerCase();
            break;
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
        
        // ZELENÁ pokud se vrátí HTTP 200-299, ČERVENÁ při chybě (např. 400, 500)
        alertBox.style.backgroundColor = res.ok ? "#4CAF50" : "#f44336";

        setTimeout(() => {
            alertBox.style.display = "none";
        }, 3000);
    }

})  





