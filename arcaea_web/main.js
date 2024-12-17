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
      const musicConstArray = [];
      let selectMusices = [];
      console.log(musicConstMax);
      console.log(musicConstMin);
      for (let i = musicConstMin * 10; i < musicConstMax * 10 + 1; i++) {
        musicConstArray.push(i);
      }
      console.log(data);
      console.log(musicConstArray);
      Object.entries(data).forEach(([musicName, musicConst]) => {
        if (musicConstArray.includes(musicConst * 10)) {
          console.log(musicName);
          selectMusices.push(musicName);
        }
      });
      let randomIndex = Math.floor(Math.random() * selectMusices.length);
      alert(selectMusices[randomIndex]);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
