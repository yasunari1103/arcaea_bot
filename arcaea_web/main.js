//置換サイト => https://yasunari1103.github.io/arcaea_bot/arcaea_web/replace/

function randonMusicByConst() {
  let selectedSongtitle = document.getElementById("musicTitle");
  if (selectedSongtitle) {
    selectedSongtitle.remove();
  }
  let selectedSongIframe = document.getElementById("musicIframe");
  if (selectedSongIframe) {
    selectedSongIframe.remove();
  }

  let musicConstMin = document.getElementById("const_min").value;
  let musicConstMax = document.getElementById("const_max").value;
  fetch("musicListConst.json")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTPS error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      let musicConstArray = [];
      let selectMusices = [];
      console.log(musicConstMax);
      console.log(musicConstMin);
      for (let i = musicConstMin * 10; i < musicConstMax * 10 + 1; i++) {
        musicConstArray.push(i);
      }
      Object.entries(data).forEach(([musicName, musicConst]) => {
        if (musicConstArray.includes(musicConst * 10)) {
          console.log(musicName);
          selectMusices.push(musicName);
        }
      });
      let randomIndex = Math.floor(Math.random() * selectMusices.length);
      let selectedSongAndDificulity = selectMusices[randomIndex];
      let selectedSong = selectedSongAndDificulity.slice(
        0,
        selectedSongAndDificulity.length - 5
      );
      if (selectedSong) {
        fetch("musicListOfficialSoundSource.json")
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTPS error! Status: ${response.status}`);
            }
            return response.json();
          })
          .then((musicSource) => {
            console.log(selectedSong);
            console.log(musicSource[selectedSong]);
            let randomSelectHTML = document.getElementById("randomSelectMusic");
            let musicSoundSource = musicSource[selectedSong];

            if (selectedSongAndDificulity) {
              const parser1 = new DOMParser();
              const doc1 = parser1.parseFromString(
                "<h1>" + selectedSongAndDificulity + "</h1>",
                "text/html"
              );
              const h1Elemant = doc1.body.firstChild;
              h1Elemant.id = "musicTitle";
              randomSelectHTML.appendChild(h1Elemant);
            }

            if (musicSoundSource) {
              const parser2 = new DOMParser();
              const doc2 = parser2.parseFromString(
                musicSoundSource,
                "text/html"
              ); //html全体の文章を作る関数
              const iframeElement = doc2.body.firstChild; //iframeのみ取得
              iframeElement.id = "musicIframe";
              randomSelectHTML.appendChild(iframeElement);
            }
          });
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
