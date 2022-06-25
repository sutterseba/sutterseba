// This is the "raw" version which has not been bundled by Browserify yet
const bip39 = require('bip39');

window.onload = function () {
    document.getElementById('mnemonic').addEventListener('input', update);
}

function update () {
    const input = document.getElementById('mnemonic').value.trim().toLowerCase();
    const output = document.getElementById('output');

    let valid = [];

    if (!input) {
        output.innerHTML = "";
        return;
    }

    if (bip39.validateMnemonic(input)) {
        output.innerHTML = "<div class='valid'>ALREADY VALID</div><div class='note'>You entered a valid " + input.split(" ").length + " word mnemonic</div>";
        return;
    }

    for (const word of bip39.wordlists.english) {
        if (bip39.validateMnemonic((input + " " + word), bip39.wordlists.english)) {
            valid.push(word);
        }
    }

    if (valid.length > 0) {
        output.innerHTML = "<div class='valid'>CHOOSE ANY OF THESE WORDS</div><div class='note'>To complete your " + (input.split(" ").length + 1) + " word mnemonic</div><br>";

        for (const word of valid) {
            output.innerHTML += word + ", ";
        }
        output.innerHTML = output.innerHTML.slice(0, -2);
    }
    else {
        output.innerHTML = "<div class='invalid'>INVALID INPUT</div><div class='note'>Check for spelling mistakes or incorrect amount of words</div>";
    }
}
