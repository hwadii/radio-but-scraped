const radioList = document.querySelector("select");
const audio = document.querySelector("audio");

async function getRadios() {
  const result = await fetch("radios.json");
  return result.json();
}

function fillSelect() {
  getRadios().then(radios => {
    let option;
    for (let radio of radios) {
      option = document.createElement("option");
      option.value = radio.url;
      option.textContent = radio.title;
      radioList.appendChild(option);
    }
    radioList.onchange = ev => {
      audio.src = ev.target.value;
      audio.play();
      localStorage.setItem("current_radio", audio.src);
      localStorage.setItem("option_index", radioList.selectedIndex);
    };

    audio.src = localStorage.getItem("current_radio");
    radioList.selectedIndex = localStorage.getItem("option_index");
  });
}

fillSelect();

const video = document.querySelector("video");
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

function handleError(error) {
  console.log("getUserMedia error: ", error);
}
navigator.mediaDevices
  .getUserMedia({ video: true })
  .then(handleSuccess, handleError);
