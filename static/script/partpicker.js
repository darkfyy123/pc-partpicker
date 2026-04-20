let build = [];

const searchCPU = document.getElementById("searchCPU");
const suggestionsCPU = document.getElementById("suggestionsCPU");

const searchGPU = document.getElementById("searchGPU");
const suggestionsGPU = document.getElementById("suggestionsGPU");

const searchRAM = document.getElementById("searchRAM");
const suggestionsRAM = document.getElementById("suggestionsRAM");

const searchMB = document.getElementById("searchMB");
const suggestionsMB = document.getElementById("suggestionsMB");

const searchDRIVE = document.getElementById("searchDRIVE");
const suggestionsDRIVE = document.getElementById("suggestionsDRIVE");

const searchFAN = document.getElementById("searchFAN");
const suggestionsFAN = document.getElementById("suggestionsFAN");

const searchPSU = document.getElementById("searchPSU");
const suggestionsPSU = document.getElementById("suggestionsPSU");

const searchCASE = document.getElementById("searchCASE");
const suggestionsCASE = document.getElementById("suggestionsCASE");


const popup = document.getElementById("popup");
const close_popup = document.getElementById("popup_close");
const overlay = document.getElementById("overlay");
const compare_btn = document.getElementById("compare");
const popup_text = document.getElementById("popup_text");


const saveContainer = document.getElementById("save_section");
const saveWrapper = document.getElementById("save_wrapper");
const save = document.getElementById("popup_save");

const suggestions = document.querySelectorAll('.suggestions-wrap');






const selected = {};

function SelectLog (type, model) {
  selected [type] = model;
  console.log("Selected", selected);
}











function setupSearch(inputEl, suggestionsEl, apiPath, type) { 
  // funkce přijímá vstupní pole, kontejner pro návrhy, cestu k API endpointu a kategorii jako parametry.
  const wrap = suggestionsEl.closest(".suggestions-wrap");

  inputEl.addEventListener("input", async () => { // Při každém stisku klávesy se spustí asynchronní vyhledávání
    const query = inputEl.value.trim();

    if (query.length < 1) {
        wrap.style.display = "none";
        return; // Pokud je pole prázdné, seznam návrhů se skryje a funkce se ukončí
    }
     // Asynchronní dotaz na API backend s enkódovaným dotazem
    const res = await fetch(`${apiPath}?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    suggestions.forEach(suggestion => {
      suggestion.classList.remove('hiden');
    });
    if (data.length === 0) {
      suggestionsEl.innerHTML = `<div class="no-results">Žádné výsledky</div>`;
      wrap.style.display = "block";
      return;
    }
    // Metoda .map() transformuje surová data o komponentách na HTML položky
    suggestionsEl.innerHTML = data
      .map(p => 
        `<div class="suggestion-item" data-model="${p.model}" data-brand="${p.brand}">
            <span class="model-text">${p.model}</span> 
            <span class="brand-label">(${p.brand})</span>
        </div>`
      )
      .join("");
    wrap.style.display = "block";
  });

  suggestionsEl.addEventListener("click", e => {
    const item = e.target.closest(".suggestion-item");
    if (!item) return;

  
    const modelValue = item.dataset.model;
    const brandValue = item.dataset.brand;

    
    inputEl.value = `${modelValue} (${brandValue})`;
    
    
    suggestionsEl.innerHTML = "";
    wrap.style.display = "none";

    
    SelectLog(type, modelValue, brandValue);

    inputEl.blur();
  });
}

  












setupSearch(
  searchCPU,
  suggestionsCPU,
  "/api/search/CPU",
  "CPU"
);

setupSearch(
  searchGPU,
  suggestionsGPU,
  "/api/search/GPU",
  "GPU"
);

setupSearch(
  searchRAM,
  suggestionsRAM,
  "/api/search/RAM",
  "RAM"
);

setupSearch(
  searchMB,
  suggestionsMB,
  "/api/search/MB",
  "MB"
);

setupSearch(
  searchDRIVE,
  suggestionsDRIVE,
  "/api/search/DRIVE",
  "DRIVE"
);

setupSearch(
  searchFAN,
  suggestionsFAN,
  "/api/search/FAN",
  "FAN"
);

setupSearch(
  searchPSU,
  suggestionsPSU,
  "/api/search/PSU",
  "PSU"
);

setupSearch(
  searchCASE,
  suggestionsCASE,
  "/api/search/CASE",
  "CASE"
);














compare_btn.onclick = async () => {
  saveWrapper.classList.add("hiden"); 
  popup_text.innerHTML = "Načítání..."; 
    
  popup.classList.add("active");
  overlay.classList.add("active");
  popup_text.innerHTML = "";


  const res = await fetch("/api/compare", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(selected)
  });

  const divider = document.querySelector(".divider");

  const data = await res.json();
  console.log(data);



  let errors = [];
  popup_text.innerHTML = "";
  if (data.socket_compatibility === false) 
    errors.push("Procesor a základní deska nejsou kompatibilní.");
  if (data.wattage_compatibility === false) 
    errors.push("Zdroj nemá dostatečný výkon.");
  if (data.ram_compatibility === false) 
    errors.push("RAM není kompatibilní se základní deskou.");
  if (data.disk_compatibility === false) 
    errors.push("Úložiště není kompatibilní se základní deskou.");
  if (data.mb_case_compatibility === false) 
    errors.push("Skříň není kompatibilní s deskou.");
  if (data.gpu_case_compatibility === false) 
    errors.push("Grafická karta se nevejde do skříně.");
  if (data.fan_cpu_compatibility === false) 
    errors.push("Chladič nesedí na procesor.");
  console.log("Errors found:", errors);



 
 if (errors.length === 0 && !data.missing) {
        popup_text.innerHTML = "Všechny komponenty jsou kompatibilní.";
        saveWrapper.classList.remove("hiden");
  } else {
        popup_text.innerHTML = data.missing || errors.join("<br>");
        saveWrapper.classList.add("hiden");
    }
};

close_popup.onclick = () => {
  popup.classList.remove("active");
  overlay.classList.remove("active");
};



save.onclick = async () => {
    try {
        const res = await fetch("/api/save_build", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(selected)
        });

        const data = await res.json();
        const alertBox = document.getElementById("alert-msg");

        
        if (data.message) {
            alertBox.innerText = data.message; 
            alertBox.style.display = "block";    
            
            
            alertBox.style.backgroundColor = res.ok ? "#4CAF50" : "#f44336";

            setTimeout(() => {
                alertBox.style.display = "none";
            }, 3000);
        }
    } catch (error) {
        console.error("Chyba při ukládání:", error);
    }
};



