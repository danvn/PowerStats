var fs = require('fs');
var Converter = require("csvtojson").Converter;
var converter = new Converter({});

// call the fromFile function which takes in the path to your
// csv file as well as a callback function

function chunkArray(myArray, chunk_size){
    var index = 0;
    var arrayLength = myArray.length;
    var tempArray = [];

    for (index = 0; index < arrayLength; index += chunk_size) {
        myChunk = myArray.slice(index, index+chunk_size);
        // Do something if you want with the group
        tempArray.push(myChunk);
    }

    return tempArray;
}

var boxScores = []
converter.fromFile("./data/playerBoxScore17-18.csv",function(err,result){
    if(err){
        console.log("An Error Has Occured");
        console.log(err);
    }

    var boxScores = result;
    // console.log(json[32]);
    boxScores.forEach(function(boxScore){
    // 2014-04-12T19:10:39.205Z
      var dateArray = boxScore["gmDate"].split('/')
      var newDate = ""
      newDate = "20" + dateArray[2]
      newMonth = "-0"
      if (dateArray[0].length < 2){
        newMonth = newMonth + dateArray[0]
      }
      else{
        newMonth = "-" + dateArray[0]
      }
      newDate = newDate + newMonth
      newDay = "-0"
      if (dateArray[1].length < 2){
        newDay = newDay + dateArray[1]
      }
      else{
        newDay = "-" + dateArray[1]
      }
      newDate = newDate + newDay + "T19:10:39.205Z"
      boxScore["keen"] = {}
      boxScore["keen"]["timestamp"] = newDate
      // console.log(boxScore["gmDate"])
      // console.log(boxScore["keen"]["timestamp"])
    });
    // console.log(boxScores)

    var result = chunkArray(boxScores, 8703);
    console.log(result.length)


    fs.writeFile("data/AllTeamsBoxScore_short1.json", JSON.stringify(result[0]), function(err) {
      console.log(boxScores.length)
        if (err) {
            console.log(err);
        }
    });

    fs.writeFile("data/AllTeamsBoxScore_short2.json", JSON.stringify(result[1]), function(err) {
      console.log(boxScores.length)
        if (err) {
            console.log(err);
        }
    });

    fs.writeFile("data/AllTeamsBoxScore_short3.json", JSON.stringify(result[2]), function(err) {
      console.log(boxScores.length)
        if (err) {
            console.log(err);
        }
    });
});







// fs.writeFile("3teamzies.json", JSON.stringify(boxScores), function(err) {
//     if (err) {
//         console.log(err);
//     }
// });
