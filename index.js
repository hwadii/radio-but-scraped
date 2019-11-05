const radioList = document.querySelector("select");
const audio = document.querySelector("audio");

fetch("radios.json")
  .then(response => response.json())
  .then(radios => {
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
  })
  .then(() => {
    audio.src = localStorage.getItem("current_radio");
    radioList.selectedIndex = localStorage.getItem("option_index");
  });
