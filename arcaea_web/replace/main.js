//作業用URL => https://yasunari1103.github.io/arcaea_bot/arcaea_web/replace/

function main() {
  const before = document.getElementById("before");
  const after = before.value.replace(/"/g, '\\"');
  console.log(after);
  const parser = new DOMParser();
  const doc = parser.parseFromString("<xmp>" + after + "</xmp>", "text/html");
  const copyTarget = doc.body.firstChild;
  document.body.appendChild(copyTarget);
  navigator.clipboard
    .writeText(copyTarget.textContent || after)
    .then(() => {})
    .catch((err) => {
      console.error("コピーに失敗しました：", err);
    });
}
