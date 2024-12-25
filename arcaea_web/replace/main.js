function main() {
  const before = document.getElementById("before");
  const after = before.value.replace(/"/g, '\\"');
  console.log(after);
  const parser = new DOMParser();
  const doc = parser.parseFromString(
    "<xmp>"+after+"</xmp>",
    "text/html"
  );
  const iframeElement = doc.body.firstChild;
  document.body.appendChild(iframeElement);
}
