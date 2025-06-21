function getGrades(inputSelector) {
 const grades = document.querySelector(inputSelector).value 
 const splitGrades = grades.split(',')
 const cleanGrades = splitGrades.map(grade => grade.trim().toUpperCase())
 return cleanGrades;
}

function lookupGrade(grade) {
  if (grade == 'A') {
    return 4; 
  } else if (grade == 'B') {
    return 3;
  } else if (grade == 'C') {
    return 2;
  } else if (grade == 'D') {
    return 1;
  } else if (grade == 'F') {
    return 0;
  } else {
    return null; 
  }
}

function calculateGpa(grades) {
  const gpaPoints = grades.map(grade => lookupGrade(grade))
  const averageGpa = gpaPoints.reduce((total, points) => total + points, 0) / gpaPoints.length;
  return averageGpa; 
}

function outputGpa(gpa, selector) {
  const targetElement = document.querySelector(selector)
  targetElement.textContent = `Your GPA is: ${gpa.toFixed(2)}`; 
}

function clickHandler() {
  const grades = getGrades("#grades");
  const gpa = calculateGpa(grades);
  outputGpa(gpa, "#output");
}

document
  .querySelector("#submitButton")
  .addEventListener("click", clickHandler);