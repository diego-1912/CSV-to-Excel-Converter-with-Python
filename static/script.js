function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    let message = document.getElementById("message");

    if (fileInput.files.length === 0) {
        message.innerHTML = "Please select a CSV file first.";
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/convert", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "converted.xlsx";
        document.body.appendChild(a);
        a.click();
        a.remove();
        message.innerHTML = "Download complete!";
    })
    .catch(error => {
        message.innerHTML = "Error: " + error;
    });
}
