async function search() {
    const q = document.getElementById("search").value;

    const res = await fetch(`/api/ai/search?q=${q}`);
    const data = await res.json();

    const results = document.getElementById("results");
    results.innerHTML = "";

    data.results.forEach(r => {
        results.innerHTML += `
            <div class="card">
                <h3>${r.title}</h3>
                <p>${r.location}</p>
                <p>$${r.price}</p>
            </div>
        `;
    });
}
