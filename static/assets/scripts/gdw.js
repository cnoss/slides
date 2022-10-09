/* Config
============================================================================ */

const urlQuestions = "/assets/data/gdwFragen.json";


/* Functions
============================================================================ */

const fetchData = async function(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
  }

  return true;
}

const generateCurrentQuestion = (questions) => {
  const params = new URLSearchParams(window.location.search);
  const targetQuestion = document.getElementById("question");
  const targetQuestionCount = document.getElementById("questionCount");
  const targetBlock = document.getElementById("block");
  const blockID = params.has('block') ? params.get('block') - 1: 0;
  const questionID = params.has('question') ? params.get('question') - 1 : 0;
  const keys = Object.keys(questions);
  const block = keys[blockID];
  let question = questions[block][questionID];
  question = question.replace(/«(.*?)»/, (x) => { return `<span class="is-blue ">${x}</span>`; });

  targetQuestion.innerHTML = question;
  targetBlock.innerHTML = `<a href="/gdw-fragen-list/">${block}</a><span class="count">${blockID+1}</span>` ;
  targetQuestionCount.innerHTML = questionID+1;
}

const changeQuestion = (newQuestionID) => {
  const params = new URLSearchParams(window.location.search);
  const blockID = params.has('block') ? params.get('block') : 0;
  const pathname = window.location.pathname;

  const newURL = `${pathname}?block=${blockID}&question=${newQuestionID}`;
  window.location.replace(newURL);
}

const getRandomInt = (max) => {
  return Math.floor(Math.random() * max);
}

const generateQuestionDropdown = (questions) => {
  const params = new URLSearchParams(window.location.search);
  const targetQuestionSelector= document.getElementById("questionSelector");
  const blockID = params.has('block') ? params.get('block') - 1: 0;
  const keys = Object.keys(questions);
  const block = keys[blockID];
  let questionsHTML= ["<option>-</option>"];
  
  for (question in questions[block]) {
    const c = question * 1 + 1;
    questionsHTML.push(`<option>${c}</option>`)
  }
  questionsHTML.push(`<option>r</option>`)

  targetQuestionSelector.innerHTML = questionsHTML.join("\n");

  targetQuestionSelector.addEventListener("change", (event) => {
    let newQuestionID = event.target.value;

    if(newQuestionID === "r"){
      newQuestionID = getRandomInt(questions[block].length -1) + 1;
    }
    changeQuestion(newQuestionID);
  });

  document.addEventListener('keydown', (event) => {
    const keyName = event.key;
    if(keyName === "r"){
      const newQuestionID = getRandomInt(questions[block].length -1) + 1;
      changeQuestion(newQuestionID);
    }
  });

}



const getQuestions = async function () {
  const questions = await fetchData(urlQuestions);

  generateCurrentQuestion(questions);
  generateQuestionDropdown(questions);

  const frageHTML = [];
  /* praxisprojekte.forEach(item => {
    const praxisprojektCard = `
      <li class="image-card">
        <figure>
          <img loading="lazy" src="${item.bild}" alt="${item.bildcredits}">
          <figcaption>
            <h3 class="image-card__text">${item.title}</h3>

            <p class="image-card__meta">${item.date}, ${item.autor}</p>
          </figcaption>
        </figure>
      </li>
    `;
    praxisprojekteHTML.push(praxisprojektCard); 
  });

  const containerPraxisprojekte = document.getElementById("praxisprojekte");
  containerPraxisprojekte.innerHTML = praxisprojekteHTML.join(" ");
  new Expander(containerPraxisprojekte);*/
}

/* Main
============================================================================ */

document.addEventListener('DOMContentLoaded', () => {
  getQuestions();
});