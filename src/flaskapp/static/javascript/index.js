"use strict";

let previousButton = document.getElementById("left-button")
let nextButton = document.getElementById("right-button")
let saveButton = document.getElementById("save-button")
let firstButton = document.getElementById("first-button")
let lastButton = document.getElementById("last-button")
let entryIDTextfield = document.getElementById("entry-id-textfield")
let maximumEntryIDSpan = document.getElementById("maximum-entry-id-span")
let systemTextarea = document.getElementById("system-textarea")
let userTextarea = document.getElementById("user-textarea")
let assistantTextarea = document.getElementById("assistant-textarea")


let send_command = (command) => {
    let message = {
        "entry_id": entryIDTextfield.value,
        "system_text": systemTextarea.value,
        "user_text": userTextarea.value,
        "assistant_text": assistantTextarea.value
    }

    fetch(`/${command}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        entryIDTextfield.value = data["entry_id"]
        maximumEntryIDSpan.textContent = data["maximum_entry_id"]
        systemTextarea.value = data["system_text"]
        userTextarea.value = data["user_text"]
        assistantTextarea.value = data["assistant_text"]
    });
}

previousButton.onclick = () => {
    send_command("previous");
}
nextButton.onclick = () => {
    send_command("next");
}
saveButton.onclick = () => {
    send_command("save");
}
entryIDTextfield.addEventListener('change', () => {
    send_command("change");
});
firstButton.onclick = () => {
    send_command("first");
}
lastButton.onclick = () => {
    send_command("last");
}

send_command("reload", {});
