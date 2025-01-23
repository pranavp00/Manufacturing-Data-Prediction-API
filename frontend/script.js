const apiBase = "http://127.0.0.1:5000";

async function uploadCSV() {
    const fileInput = document.getElementById("csvFile");
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a CSV file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch(`${apiBase}/upload`, {
            method: "POST",
            body: formData,
        });
        const result = await response.json();
        alert(result.message || "File uploaded successfully!");
    } catch (error) {
        alert("Error uploading file.");
    }
}

document.getElementById("predictForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const temperature = parseFloat(document.getElementById("temperature").value);
    const runtime = parseFloat(document.getElementById("runtime").value);

    const data = { Temperature: temperature, Run_Time: runtime };

    try {
        const response = await fetch(`${apiBase}/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        alert(`Prediction: ${result.Downtime}, Confidence: ${result.Confidence}`);
    } catch (error) {
        alert("Error making prediction.");
    }
});
