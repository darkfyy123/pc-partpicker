const typeSelect = document.getElementById("type");
const container = document.getElementById("component-container");

typeSelect.addEventListener("input", async function() {

    if (!typeSelect.value) {
        container.innerHTML = "<p>Zadej kategorii</p>";
        return;
    }

    const res = await fetch("/api/show_components", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "category": typeSelect.value }) 
    });

    const data = await res.json();
    

    container.innerHTML = "";

    if (data.components) {

        const table = document.createElement("table");
        table.className = "component-table"; 
        
        const thead = document.createElement("thead");
        const tbody = document.createElement("tbody");

     
        const headers = Object.keys(data.components[0]);
        const headerRow = document.createElement("tr");
        headers.forEach(key => {
            const th = document.createElement("th");
            th.textContent = key.toUpperCase();
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);



        data.components.forEach(item => {
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
    } 
});