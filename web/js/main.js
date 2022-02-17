var letter = [];

answers = document.getElementById("answers");
guesses = document.getElementById("guesses");

for (var i = 0; i < 6; i++) {
  col = [];
  for (var j = 0; j < 5; j++) {
    col.push(document.getElementById("" + i + "-" + j));
  }
  letter.push(col);
}

currentRow = 0;
pointer = 0;

restart_game();

function add_delay(i, j, delay) {
  letter[i][j].classList.add("delay-" + delay);
}

function remove_delay(i, j) {
  letter[i][j].classList.remove("delay-1");
  letter[i][j].classList.remove("delay-2");
  letter[i][j].classList.remove("delay-3");
  letter[i][j].classList.remove("delay-4");
  letter[i][j].classList.remove("delay-5");
}

function restart_game() {
  for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 5; j++) {
      letter[i][j].innerHTML = "";
      letter[i][j].classList.remove("selected");
      letter[i][j].classList.remove("empty");
      letter[i][j].classList.remove("wrong");
      letter[i][j].classList.remove("neutral");
      letter[i][j].classList.remove("hint");
      letter[i][j].classList.remove("correct");
      letter[i][j].classList.remove("filled");
      remove_delay(i, j);
    }
  }
  show_answer();
  currentRow = 0;
  pointer = 0;
  eel.new_game();
  update_answers();
  letter[0][0].classList.add("selected");
  stopConfetti();
}

function show_empty_cells() {
  for (var i = pointer; i < 5; i++) {
    letter[currentRow][i].classList.add("empty");
    add_delay(currentRow, i, i - pointer + 1);
    setTimeout(() => {
      remove_delay(currentRow, i);
      letter[currentRow][i].classList.remove("empty");
    }, 200 * (i - pointer));
  }
}

function select_all() {
  for (var i = 0; i < 5; i++) letter[currentRow][i].classList.add("selected");
}

function unselect_all() {
  for (var i = 0; i < 5; i++) letter[currentRow][i].classList.remove("selected");
}

function show_wrong_word() {
  for (var i = 0; i < 5; i++)
    letter[currentRow][i].classList.add("wrong");
    for (var i = 0; i < 5; i++) setTimeout(() => letter[currentRow][i].classList.remove("wrong"), 200 * i);
}

function win()
{
  unselect_all();
  for (var i = 0; i < 5; i++) letter[currentRow][i].classList.add("win");
  currentRow = 6;
  pointer = 5;
  startConfetti();
}

async function guess_word(word) {
  if (currentRow < 6) {
    word = "";
    for (var i = 0; i < 5; i++) word += letter[currentRow][i].innerHTML;
    r = await eel.guess(word)();
    if (r) {
      all_correct = true;
      for (var i = 0; i < 5; i++) {
        letter[currentRow][i].classList.remove("filled");
        if (r[i] == 0) letter[currentRow][i].classList.add("neutral");
        else if (r[i] == 1) letter[currentRow][i].classList.add("hint");
        else if (r[i] == 2) letter[currentRow][i].classList.add("correct");
        if (r[i] != 2) all_correct = false;
        update_answers();
      }
      if (all_correct) win();
      else {
        pointer = 0;
        unselect_all();
        currentRow++;
        if (currentRow < 6) letter[currentRow][0].classList.add("selected");
        else show_answer();
      }
    }
    else show_wrong_word();
  }
}

async function show_answer() {
  solution = await eel.get_answer()();
  if (solution) document.getElementById("errorMessage").innerHTML = "Answer was " + solution;
}

function clear_error_message() {
  document.getElementById("errorMessage").innerHTML = "";
}

document.addEventListener("keydown", function (event) {

  let key = event.key;
  var isLetter = (key.length == 1 && ((key >= "A" && key <= "Z") || (key >= "a") && key <= "z"));

  if (isLetter && pointer < 5) {
    clear_error_message();
    letter[currentRow][pointer].innerHTML = key;
    letter[currentRow][pointer].classList.add("filled");
    letter[currentRow][pointer].classList.remove("empty");
    letter[currentRow][pointer].classList.remove("wrong");
    letter[currentRow][pointer].classList.remove("selected");
    pointer++;
    if (pointer < 5) letter[currentRow][pointer].classList.add("selected");
    else select_all();
  }

  else if (key == "Backspace" && pointer > 0) {
    clear_error_message();
    if (pointer < 5) letter[currentRow][pointer].classList.remove("selected");
    else unselect_all();
    pointer--;
    letter[currentRow][pointer].innerHTML = "";
    letter[currentRow][pointer].classList.remove("filled");
    letter[currentRow][pointer].classList.add("selected");
  }

  else if (key == "Enter") {
    if (pointer != 5) {
      show_empty_cells();
    }
    else {
      guess_word()
      if (currentRow >= 6) show_answer();
    }

  }

});

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

eel.expose(show_error);
function show_error(message) {
  document.getElementById("errorMessage").innerHTML = message;
}

eel.expose(console_log);
function console_log(message) {
  console.log(message);
}

eel.expose(set_answers);
function set_answers(words) {
  answers.innerHTML = '';
  for (let word of words) {
    var div = document.createElement('div');
    div.className = "col-12 text-center possible-answer";
    div.innerHTML = word;
    answers.appendChild(div);
  }
}

eel.expose(set_guesses);
function set_guesses(words) {
  guesses.innerHTML = '';
  for (let word of words) {
    var div = document.createElement('div');
    div.className = "col-12 text-center";
    div.innerHTML = word.word + ": " + word.score;
    guesses.appendChild(div);
  }
}

eel.expose(set_guess_loading);
function set_guesses_loading() {
  guesses.innerHTML = "";
  var div = document.createElement("div");
  div.className = "loader text-center";
  guesses.appendChild(div);
}

function update_best_guess() {
  set_guesses_loading();
  eel.update_best_guesses();
}

function update_answers() {
  eel.update_possible_words();
}