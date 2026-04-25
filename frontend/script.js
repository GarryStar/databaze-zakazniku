const API_URL = "http://10.0.0.18:8000/customers";

const form = document.getElementById("customerForm");
const list = document.getElementById("customerList");

/* NAČTENÍ ZÁKAZNÍKŮ */
async function loadCustomers() {
    const res = await fetch(API_URL);
    const data = await res.json();

    list.innerHTML = "";

    data.forEach(c => {
        const li = document.createElement("li");

        li.textContent = `
        ${c.first_name} ${c.last_name}
        ${c.city}
        📧 ${c.email || "-"}
        📞 ${c.phone || "-"}
        💳 ${c.bank_account || "-"}
        `;

        list.appendChild(li);
    });
}

/* ODESLÁNÍ FORMULÁŘE */
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const customer = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        street: document.getElementById("street").value,
        house_number: document.getElementById("house_number").value,
        city: document.getElementById("city").value,
        postal_code: document.getElementById("postal_code").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        bank_account: document.getElementById("bank_account").value,        
    };

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(customer)
    });

    form.reset();
    loadCustomers();
});

/* NAČTI PŘI STARTU */
loadCustomers();