function randonMusicByConst() {
  let musicConstMin = document.getElementById("const_min").value;
  let musicConstMax = document.getElementById("const_max").value;
  fetch("musicList.json")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTPS error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(musicConstMax);
      console.log(musicConstMin);
      //forで配列作成    <= あとでやる
      console.log(data);
      //forEachで配列から取り出して実行    <= あとでやる
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
