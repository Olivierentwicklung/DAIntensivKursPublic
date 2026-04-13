let fruits = [];

async function loadFruits() {
  const url = "http://localhost:8000/fruits/";
  let responseData = await fetch(url);
  fruits = await responseData.json();
  console.log(fruits);
  render();
}

function render() {
  const fruitList = document.getElementById("fruitlist");
  fruitList.innerHTML = "";
  fruits.forEach((fruit) => {
    const newFruit = document.createElement("li");
    newFruit.innerHTML =
      "<strong>" +
      fruit.name +
      ":" +
      "</strong>" +
      " Gewicht - " +
      fruit.gewicht +
      "g, Farbe - " +
      fruit.farbe;
    fruitList.appendChild(newFruit);
  });
}
