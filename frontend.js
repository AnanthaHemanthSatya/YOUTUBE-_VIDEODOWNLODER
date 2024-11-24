document.getElementById('downloadForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    document.getElementById('status').innerText = "Downloading...";

    const response = await fetch('http://localhost:8000/download', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const result = await response.json();
        document.getElementById('status').innerText = result.status || "Download started!";
    } else {
        const errorDetail = await response.json();
        document.getElementById('status').innerText = `Error: ${errorDetail.detail || "Unable to download."}`;
    }
});
