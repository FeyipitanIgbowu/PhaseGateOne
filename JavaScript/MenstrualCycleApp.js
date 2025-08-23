const prompt = require('prompt-sync')();

function dateCollection(monthName, dayNumber){
  const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  monthName = monthName[0].toUpperCase() + monthName.slice(1).toLowerCase();
 let year = 2025;
   
let date = new Date(`${monthName} ${dayNumber} ${year}`);
return date.toLocaleDateString();
}

function checkNextPeriod(startDate, cycleLength){
	nextPeriod = startDate + cycleLength
return nextPeriod.toLocaleDateString();

}

function ovulationDate(startDate, cycleLength){
  let ovulationDay = startDate + (cycleLength - 14);
return ovulationDay;
}

function fertileWindow(startDate, cycleLength){
	let ovulationDate = startDate + (cycleLength - 14);
	start = ovulationDate - 2
	end = ovulation_date + 2
return start, end
}



let response = (dateCollection("August", 1));
console.log(response)

let nextPeriod1 = prompt("When was your Period Start Date: ")
let nextPeriod2 = prompt("What is your Cycle Length: ")
console.log(dateCollection(nextPeriod1, nextPeriod2))

let ovulationDate1 = prompt("When was your Period Start Date: ")
let ovulationDate2 = prompt("What is your Cycle Length: ")
console.log(ovulationDate(ovulationDate1, ovulationDate2))

let fertileWindow1 = prompt("When was your Period Start Date: ")
let fertileWindow2 = prompt("What is your Cycle Length: ")
console.log(fertileWindow(fertileWindow1, fertileWindow2))


