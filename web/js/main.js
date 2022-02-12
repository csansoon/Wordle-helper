var letter = [];
for (var i = 0; i < 6; i++) {
  col = [];
  for (var j = 0; j < 5; j++) {
    col.push(document.getElementById("" + i + "-" + j));
  }
  letter.push(col);
}

var currentRow = 0;
var pointer = 0;

eel.new_game();

function show_empty_cells() {
  for (var i = pointer; i < 5; i++)
    letter[currentRow][i].classList.add("empty");
  setTimeout(() => {
    for (var i = pointer; i < 5; i++)
      letter[currentRow][i].classList.remove("empty");
  }, 500);
}

function show_wrong_word() {
  for (var i = pointer; i < 5; i++)
    letter[currentRow][i].classList.add("wrong");
  setTimeout(() => {
    for (var i = pointer; i < 5; i++)
      letter[currentRow][i].classList.remove("wrong");
  }, 500);
}

async function guess_word(word) {
  if (currentRow < 6) {
    word = "";
    for (var i = 0; i < 5; i++) word += letter[currentRow][i].innerHTML;
    r = await eel.guess(word)();
    if (r) {
      for (var i = 0; i < 5; i++) {
        letter[currentRow][i].classList.remove('blank');
        if (r[i] == 0) letter[currentRow][i].classList.add("blank");
        else if (r[i] == 1) letter[currentRow][i].classList.add("hint");
        else if (r[i] == 2) letter[currentRow][i].classList.add("correct");
      }
      pointer = 0;
      currentRow++;
    }
    else show_wrong_word();
  }
}

async function show_answer() {
  let answer = eel.get_answer();
  document.getElementById("errorMessage").innerHTML = "Answer was " + answer;
}

function clear_error_message() {
  document.getElementById("errorMessage").innerHTML = "";
}

document.addEventListener("keydown", function (event) {

  let key = event.key;
  var isLetter = (key.length == 1 && ((key >= "A" && key <= "Z") || (key >= "a") && key <= "z"));

  if (isLetter && pointer < 5) {
    letter[currentRow][pointer].innerHTML = key;
    letter[currentRow][pointer].classList.add("blank");
    pointer++;
  }

  else if (key == "Backspace" && pointer > 0) {
    clear_error_message();
    pointer--;
    letter[currentRow][pointer].innerHTML = "";
    letter[currentRow][pointer].classList.remove("blank");
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