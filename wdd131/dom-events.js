// events.js
 const listElement = document.querySelector("#todoList");
    const inputElement = document.querySelector("#todo");
    const submitButton = document.querySelector("#submitTask");

function newTask() {
  const task = inputElement.value.trim();
  if (task === "") return;
    
    listElement.innerHTML += `
      <li> ${task}
        <div>
          <span data-function="delete">❎</span>
          <span data-function="complete">✅</span>
        </div>
      </li>`
  }
  
  function manageTasks(e) {
    
    const parent = e.target.closest("li");
    if (!parent) return;

    const action = e.target.getAttribute('data-function');

      if (action === "delete") {
        parent.remove();
      }
      if (action === "complete") {
      parent.classList.toggle('strike');
      }
  }
  
  submitButton.addEventListener("click", newTask);
  listElement.addEventListener("click", manageTasks);