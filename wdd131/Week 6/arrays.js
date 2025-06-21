//  arrays.js
const steps = ["one", "two", "three"];
function listTemplate(step) {
  return `<li>${step}</li>` //the html string made from step
}
const stepsHtml = steps.map(listTemplate);// use map to convert the list from strings to HTML
document.querySelector("#myList").innerHTML = stepsHtml.join();// set the innerHTML

const grades = ['A', 'B', 'C', 'D', 'F'];
function findGpa(grade) {
    let points = 0; 
    if (grade === 'A') {
        points = 4;
    } else if (grade === 'B') {
        points = 3;
    } else if (grade === 'C') {
        points = 2;
    } else if (grade === 'D') {
        points = 1;
    } else if (grade === 'F') {
        points = 0;
    }
    return points; 
}
const gpaPoints = grades.map(findGpa);
const averageGpaPoints = gpaPoints.reduce((total, points) => total + points, 0) / grades.length;
console.log(`Average GPA Points: ${averageGpaPoints.toFixed(2)}`);

const fruits = ['watermelon', 'banana', 'apple', 'orange', 'grape'];
console.log(fruits.filter(fruit => fruit.length < 6)); // ['apple', 'grape']

const numbers = [12, 34, 21, 54]
let luckyNumber = 21; 
console.log(`Index of ${luckyNumber}: ${numbers.indexOf(luckyNumber)}`); // Index of 21: 2