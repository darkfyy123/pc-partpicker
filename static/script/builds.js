const typeSelect = document.getElementById("type");
const container = document.getElementById("component-container");

window.addEventListener("DOMContentLoaded", async () => {
    const res = await fetch("/api/builds");
    const data = await res.json();

    if (data.message) {
        console.log(data.message)
    }
    

    container.innerHTML = "";

    if (data.builds && data.builds.length > 0) {

        const table = document.createElement("table");
        table.className = "build-table"; 
        
        const thead = document.createElement("thead");
        const tbody = document.createElement("tbody");

        const headers = ["id", "cpu", "gpu", "mb", "ram", "drive", "fan", "case", "psu"];
        const headerRow = document.createElement("tr");
        headers.forEach(key => {
            const th = document.createElement("th");
            th.textContent = key.toUpperCase();
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);


        data.builds.forEach(item => {
            const row = document.createElement("tr");
            headers.forEach(key => {
                const td = document.createElement("td");
                td.textContent = item[key];
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });

        table.appendChild(thead);
        table.appendChild(tbody);
        container.appendChild(table);
    } else {
        container.innerHTML = "<p>Nebyla nalazena žádná sestava</p>";
    }
});