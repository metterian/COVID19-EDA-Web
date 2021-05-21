const title = document.getElementById("title");

function changeColor(e) {
  console.log(e);
}

function init() {
  title.addEventListener("click", changeColor);
}

init();
