function displayMessage(message) {
  const ul = document.getElementById("message-ul");
  const li = document.createElement("li");
  li.innerText = `${message.content}`;
  ul.appendChild(li);

  // const divMessage = document.getElementById("message-div");
  // divMessage.innerText = `${message.content}`;
}

async function readMessage() {
  const res = await fetch("/message-get");
  const jsonRes = await res.json();
  const ul = document.getElementById("message-ul");
  ul.innerHTML = "";
  console.log(jsonRes);
  jsonRes.forEach(displayMessage);
}

async function createMessage(value) {
  const res = await fetch("/message-send", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      id: new Date(),
      content: value,
    }),
  });
  readMessage();
  console.log(res.json);
}

function sendMessage(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    console.log("메시지가 전송됨");
    const MessageInput = document.getElementById("message-input");
    createMessage(MessageInput.value);
    MessageInput.value = "";
  }
}

function openMessenger() {
  console.log("메신저가 켜졌습니다");
  const messageWin = document.getElementById("messageWin");
  messageWin.style.display = "block";
  // messageWin.innerText = "안녕하세요? 건전한 대화를 해주세요.";

  const MessageInput = document.getElementById("message-input");
  MessageInput.style.display = "block";
  MessageInput.addEventListener("keydown", sendMessage);
  // messenger.addEventListener("click", closeMessenger);
}

// function closeMessenger() {
//   console.log("메신저가 꺼졌습니다!");
//   const messageWin = document.getElementById("messageWin");
//   const MessageInput = document.getElementById("message-input");
//   messageWin.style.display = "none";
//   MessageInput.style.display = "none";
//   return;
// }

const messenger = document.querySelector("#messenger");
messenger.addEventListener("click", openMessenger);
