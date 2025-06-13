window.onload = () => {
  fetch('/api/quote')
    .then(res => res.json())
    .then(data => document.getElementById('quote').innerText = data.quote);

  fetch('/api/weather')
    .then(res => res.json())
    .then(data => {
      document.getElementById('weather').innerText =
        `${data.city}: ${data.temperature}°C, ${data.description}`;
    });

  fetch('/api/news')
    .then(res => res.json())
    .then(data => {
      let list = document.getElementById('news');
      data.forEach(article => {
        let li = document.createElement('li');
        li.innerText = article.title;
        list.appendChild(li);
      });
    });
};

function prioritize() {
  const tasks = document.getElementById("taskInput").value.split(',');
  fetch('/api/prioritize', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tasks: tasks })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("priorityOutput").innerText = data.prioritized_tasks;
  });
}
