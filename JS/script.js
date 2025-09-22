
let N = 101;
for (let i= 0; i <= N; i++) {
  let output = "";
  if (i % 3 === 0 && i % 5 === 0) {
    output = "TicToc";
  } else if (i % 3 === 0) {
    output = "Tic";
  } else if (i % 5 === 0) {
    output = "Toc";
  } else {
    output = i;
  }
  const p = document.createElement("p");
  p.textContent = output;
  document.body.appendChild(p);
}