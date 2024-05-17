const num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
const pGroup = ["P1", "P2", "P3", "P4", "P5", "P6"];
let people = [];
let P1, P2, P3, P4, P5, P6;

const Quotes = [
    [],
    [
        ["Why is it so hard for you to believe me?!", "...", "Oh, right. The lying."],
        ["I couldn't help you even if I wanted to.", "But you don't want to.", "No, no I don't."],
        ["Bro do you lift?", "Yeah dude how did you know?", "Because you lift my heart whenever you're around", "Bro", "Bro"],
        [" walks into a dark room:", "Hmm. Like a good neighbour-", "...", "Statefarm is here"],
        ["It's too dangerous to go alone, take this!", " you're just holding out your hand.", "Yes."]
    ],
    [
        ["I swear, by the summer's end, thy will have taken thee to at least one party,", "! 'tis my mission for this summer!", "...still bitter that they chose ", " for the school play, are we?", "Shut up- you and I both know that the only reason that, that thing got the lead role of Juliette is because she was blowing the drama teacher"],
        ["Make no mistake. Not only am I party rocking, but I am also in the house tonight.", "But are you shuffling?", "Everyday.", "What language are you two speaking??"]
    ],
    [],
    [],
    []
];

function collectInputs() {
    const count = document.getElementById("count").value;
    const peopleInputs = document.getElementById("peopleInputs");
    peopleInputs.innerHTML = "";

    for (let i = 0; i < count; i++) {
        const label = document.createElement("label");
        label.textContent = `Character ${num[i]}: `;
        const input = document.createElement("input");
        input.type = "text";
        input.id = `person${i + 1}`;
        input.required = true;
        peopleInputs.appendChild(label);
        peopleInputs.appendChild(input);
    }

    document.querySelector('button[onclick="collectInputs()"]').style.display = "none";
    document.querySelector('button[onclick="generateConversation()"]').style.display = "inline-block";
}

function generateConversation() {
    const count = document.getElementById("count").value;
    people = [];
    for (let i = 0; i < count; i++) {
        const person = document.getElementById(`person${i + 1}`).value;
        people.push(person);
    }

    [P1, P2, P3, P4, P5, P6] = [null, null, null, null, null, null];
    let availablePeople = [...people];

    if (availablePeople.length > 0) {
        P1 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }
    if (availablePeople.length > 0) {
        P2 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }
    if (availablePeople.length > 0) {
        P3 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }
    if (availablePeople.length > 0) {
        P4 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }
    if (availablePeople.length > 0) {
        P5 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }
    if (availablePeople.length > 0) {
        P6 = availablePeople.splice(Math.floor(Math.random() * availablePeople.length), 1)[0];
    }

    const quoteList = Quotes[count - 1];
    const randomQuote = quoteList[Math.floor(Math.random() * quoteList.length)];
    const outputDiv = document.getElementById("output");

    let conversation = "";
    for (let i = 0; i < randomQuote.length; i++) {
        if (randomQuote[i].includes("P1")) {
            conversation += `${P1}: `;
        } else if (randomQuote[i].includes("P2")) {
            conversation += `${P2}: `;
        } else if (randomQuote[i].includes("P3")) {
            conversation += `${P3}: `;
        } else if (randomQuote[i].includes("P4")) {
            conversation += `${P4}: `;
        } else if (randomQuote[i].includes("P5")) {
            conversation += `${P5}: `;
        } else if (randomQuote[i].includes("P6")) {
            conversation += `${P6}: `;
        } else {
            conversation += randomQuote[i];
        }
        conversation += " ";
    }

    outputDiv.innerHTML = conversation;
    outputDiv.style.display = "block";
}
