// from data.js
const tableData = data;

// function to display track,artist and pop rating.
function prediction(trackname) {
    console.log(trackname)
    let bigCities = tableData.filter(function (e) {
        return e.track == trackname;
    });
    let songlist = Object.values(bigCities[0]);
    document.getElementById('trackname').value = songlist[0];
    document.getElementById('artist').value = songlist[1];
    document.getElementById('Acousticness').value = songlist[2];
    document.getElementById('Danceability').value = songlist[3];
    document.getElementById('Energy').value = songlist[4];
    document.getElementById('Instrumentalness').value = songlist[5];
    document.getElementById('Liveness').value = songlist[6];
    document.getElementById('Speechiness').value = songlist[7];
    document.getElementById('Tempo').value = songlist[8];
    document.getElementById('Valence').value = songlist[9];
    document.getElementById('key_A').value = songlist[10];
    document.getElementById('key_A#').value = songlist[11];
    document.getElementById('key_B').value = songlist[12];
    document.getElementById('key_C').value = songlist[13];
    document.getElementById('key_C#').value = songlist[14];
    document.getElementById('key_D').value = songlist[15];
    document.getElementById('key_D#').value = songlist[16];
    document.getElementById('key_E').value = songlist[17];
    document.getElementById('key_F').value = songlist[18];
    document.getElementById('key_F#').value = songlist[19];
    document.getElementById('key_G').value = songlist[20];
    document.getElementById('key_G#').value = songlist[21];
    
  };

// function to display Track details
function tableDisplay(songlist) {
  var tbody = d3.select("tbody");
  songlist.forEach((songrecord) => {
    var row = tbody.append("tr");
    Object.entries(songrecord).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.html(value);
    });
  });
};

// clear the table for new data
function deleteTbody() {
  d3.select("tbody")
    .selectAll("tr").remove()
    .selectAll("td").remove();
};

// initial display of all songs
tableDisplay(tableData);

// 'Filter Table' button
var button = d3.select("#filter-btn");

// filter the database and display
button.on("click", function(event) {
  d3.event.preventDefault();
  deleteTbody();
  var trackinput = d3.select("#songname").property("value");
  if (trackinput.trim() === "" ) {
    // display the whole database if the date field has no date
    var filteredData = tableData;    
    document.getElementById('songname').style.borderColor = "red";
    document.getElementById('songname').focus();
    document.getElementById("songname").placeholder = "Enter Track Name";
    
  } else {
    // otherwise, display the filtered dataset  
    // console.log(trackinput);
   
    var filteredData = tableData;
    console.log(filteredData);
    var filteredData = tableData.filter(songdata => 
      songdata.track === trackinput.trim());
      console.log(filteredData);
    // var test = "testest";
  };

  // display message if no records found
  if (filteredData.length == 0) {
    console.log(filteredData);
    d3.select("tbody")
      .append("tr")
      .append("td")
        .attr("colspan", 7)
        .html("<h4>Track not found! Press F5 to refresh page.</h4>");
  };
 
  tableDisplay(filteredData);
  prediction(trackinput);
});

// function myFunction() {
//   document.getElementById("songname").placeholder = "Enter Track Name";
// }





