const tarefas = [
  { id: 1, descricao: "Estudar a unidade Start da Alura", concluido: true },
  { id: 2, descricao: "Praticar manipulação de DOM com JS", concluido: false },
];

const listaContainer = document.getElementById("listaContainer");
const inputTarefa = document.getElementById("novaTarefa");
const btnAdicionar = document.getElementById("btnAdicionar");

function criarElementoTarefa(tarefa) {
  const li = document.createElement("li");
  li.textContent = tarefa.descricao;
  if (tarefa.concluido) {
    li.style.textDecoration = "line-through";
  }
  return li;
}

function renderizarTarefas() {
  listaContainer.innerHTML = ""; 
  tarefas.forEach(tarefa => {
    const elemento = criarElementoTarefa(tarefa);
    listaContainer.appendChild(elemento);
  });
}

function adicionarTarefa() {
  const texto = inputTarefa.value.trim();
  if (texto === "") {
    alert("Por favor, digite uma tarefa válida!");
    return;
  }
  const novaTarefaObj = {
    id: tarefas.length + 1,
    descricao: texto,
    concluido: false
  };
  tarefas.push(novaTarefaObj);
  inputTarefa.value = "";      
  renderizarTarefas();         
}

btnAdicionar.addEventListener("click", adicionarTarefa);
renderizarTarefas();