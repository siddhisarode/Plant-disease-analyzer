async function predictDisease() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];

    if (!file) {
        alert("Please upload an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("disease").innerText = data.prediction;
        document.getElementById("confidence").innerText = data.confidence;
        document.getElementById("description").innerText = data.description;

        const remediesList = document.getElementById("remedies");
        remediesList.innerHTML = "";
        data.remedies.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            remediesList.appendChild(li);
        });

        const careList = document.getElementById("careTips");
        careList.innerHTML = "";
        data.care_tips.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            careList.appendChild(li);
        });

        document.getElementById("result").classList.remove("hidden");

    } catch (error) {
        alert("Error connecting to server.");
        console.error(error);
    }
}
