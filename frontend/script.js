fetch("https://newsapi.org/v2/everything?q=space&apiKey=YOUR_API_KEY")
    .then(response => response.json())
    .then(data => {
        let newsDiv = document.getElementById("news");
        data.articles.forEach(article => {
            let item = document.createElement("p");
            item.innerHTML = `<strong>${article.title}</strong> - <a href="${article.url}">Read More</a>`;
            newsDiv.appendChild(item);
        });
    })
    .catch(error => console.error("Error fetching news:", error));
