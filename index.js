const links = [
  "http://stream1.addictradio.net/addictalternative.mp3",
  "http://stream1.addictradio.net/addictlounge.mp3",
  "http://stream1.addictradio.net/addictrock.mp3",
  "http://stream1.addictradio.net/addictstar.mp3",
  "http://start-adofm.ice.infomaniak.ch/start-adofm-high.mp3",
  "http://bayoublueradio.com:8000/live"
];

const radioList = document.querySelector("select");
let option;
for (let link of links) {
  option = document.createElement("option");
  option.value = link;
  option.textContent = link;
  radioList.appendChild(option);
}
console.log(radioList);
