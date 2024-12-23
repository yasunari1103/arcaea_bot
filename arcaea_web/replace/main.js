function main() {
  const before = document.getElementById("before").value;
  const after = before.replace(/"/g, '\\"');
  console.log(after);
}
