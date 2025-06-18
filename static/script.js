async function search() {
  const query = document.getElementById("searchBox").value.toLowerCase();
  const response = await fetch(`/search?query=${query}`);
  const data = await response.json();

  const resultList = document.getElementById("results");
  resultList.innerHTML = "";

  data.forEach(item => {
    const highlighted = item.title.replace(new RegExp(query, "gi"), match => `<span class="highlight">${match}</span>`);
    const li = document.createElement("li");
    li.innerHTML = `<a href="${item.url}" target="_blank">${highlighted}</a>`;
    resultList.appendChild(li);
  });
}
