/*
曲のclass => no-overflow
スコアのclass => ex-main EX+
*/

let getJSONButton = document.createElement("button");
getJSONButton.addEventListener("click", function () {
  let result = document.getElementsByClassName("card");
  musicList = {};

  for (let i = 1; i < 60; i += 2) {
    let musicName =
      result[i].getElementsByClassName("no-overflow")[0].textContent;
    let musicScore = parseInt(
      result[i]
        .getElementsByClassName("experince")[0]
        .textContent.replace(/[^0-9]/g, ""),
      10
    );
    difficultyLevel =
      result[i].getElementsByClassName("label small-label")[0].textContent;
    musicList[musicName + "[" + difficultyLevel + "]"] = musicScore;
  }
  JSON_score = JSON.stringify(musicList);

  // 3. Blobオブジェクトを作成
  const blob = new Blob([JSON_score], { type: "application/json" });

  // 4. ダウンロード用のリンクを作成
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "best_30.json";

  // 5. リンクをクリックしてファイルをダウンロード
  document.body.appendChild(a);
  a.click();

  // 6. リンクを削除してメモリを解放
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});
getJSONButton.textContent = "ベスト枠のJSONファイルをダウンロード！";
getJSONButton.className = "button";

//ボタンのcss
getJSONButton.style.width = "100%";
getJSONButton.style.height = "auto";
getJSONButton.style.background = "linear-gradient(to right, #B0FFFF, pink)";
getJSONButton.style.fontFamily =
  "Open Sans,Yu Gothic Medium,Yu Gothic,Noto Sans JP,sans-serif";
document.body.prepend(getJSONButton);

//////////////////////////////////////////////////////////////////////////////////////////

let checkBestPotentialButton = document.createElement("button");
checkBestPotentialButton.addEventListener("click", function () {
  const jsonPath = chrome.runtime.getURL("musicList.json"); //同梱されているJSONファイルの読み込み
  fetch(jsonPath)
    .then((response) => response.json())
    .then((data) => {
      let bestMusicList = [];
      let result = document.getElementsByClassName("card");
      for (let i = 1; i < 60; i += 2) {
        let musicName =
          result[i].getElementsByClassName("no-overflow")[0].textContent;
        let musicScore = parseInt(
          result[i]
            .getElementsByClassName("experince")[0]
            .textContent.replace(/[^0-9]/g, ""),
          10
        );
        let difficultyLevel =
          result[i].getElementsByClassName("label small-label")[0].textContent;
        bestMusicList.push({
          number: i / 2 + 0.5,
          name: musicName + "[" + difficultyLevel + "]",
          score: musicScore,
        });
      }
      console.log(bestMusicList);
      bestMusicList.forEach((element) => {
        Object.entries(data).forEach(([key, value]) => {
          if (element.name === key) {
            /////ここから修正
            let Const = value;
            let Score = element.score;
            console.log(element.number, key, value, element.score);
          }
        });
      });
    })
    .catch((error) => {
      console.error("Error loading JSON:", error);
    });
});
checkBestPotentialButton.textContent = "ベスト枠を確認！";
checkBestPotentialButton.className = "button";

//ボタンのcss
checkBestPotentialButton.style.width = "100%";
checkBestPotentialButton.style.height = "auto";
checkBestPotentialButton.style.background =
  "linear-gradient(to right, #B0FFFF, pink)";
checkBestPotentialButton.style.fontFamily =
  "Open Sans,Yu Gothic Medium,Yu Gothic,Noto Sans JP,sans-serif";
document.body.prepend(checkBestPotentialButton);
