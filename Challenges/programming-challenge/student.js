// Write your code here

const { f } = require("./bundle");

function myFirstFunction(bike) {
  forward(bike);
}

function twiceForward(bike) {
  forward(bike);
  forward(bike);
}

function thriceForward(bike) {
  forward(bike);
  forward(bike);
  forward(bike);
}

function forward4(bike) {
  forward(bike);
  forward(bike);
  forward(bike);
  forward(bike);
}

function forward5(bike) {
  forward(bike);
  forward(bike);
  forward(bike);
  forward(bike);
  forward(bike);
}

function forward10(bike) {
  let i = 0;
  while (i < 10) {
    forward(bike);
    i++;
  }
}

function right(bike) {
  turnRight(bike);
  forward(bike);
}

function ellShape(bike) {
  let i = 0;
  while (i < 9) {
    forward(bike);
    if (i == 4) {
      turnRight(bike);
    }
    i++;
  }
}

function uTurn(bike) {
  let i = 0;
  while (i < 15) {
    forward(bike);
    if (i == 2) {
      turnRight(bike);
    } else if (i == 12) {
      turnRight(bike);
    }
    i++;
  }
}

function forwardN(bike, n) {
  let i = 0;
  while (i < n) {
    forward(bike);
    i++;
  }
}

function crookedUTurn(bike) {
  forwardN(bike, 7);
  turnRight(bike);
  forwardN(bike, 9);
  turnRight(bike);
  forwardN(bike, 3);
}

function forwardUntilWall(bike) {
  while (!sensor(bike)) {
    forward(bike);
  }
}

function smartEllShape(bike) {
  forwardUntilWall(bike);
  turnRight(bike);
  forwardUntilWall(bike);
}

function spiral(car) {
  let end = false;
  while (!end) {
    forwardUntilWall(car);
    turnRight(car);
    if (sensor(car)) {
      end = true;
    }
  }
}

function turnLeft(vehicle) {
  let i = 0;
  while (i < 3) {
    turnRight(vehicle);
    i++;
  }
}

function turnBack(vehicle) {
  let i = 0;
  while (i < 2) {
    turnRight(vehicle);
    i++;
  }
}

function left(car) {
  turnLeft(car);
  forward(car);
}

function slalom(car) {
  let end = false;
  while (!end) {
    forwardUntilWall(car);
    turnRight(car);
    if (sensor(car)) {
      turnBack(car);
      if (sensor(car)) {
        end = true;
      }
    }
  }
}

function checkLeftRight(vehicle) {
  let end = false;
  if (sensor(vehicle)) {
    turnRight(vehicle);
    if (sensor(vehicle)) {
      turnBack(vehicle);
      if (sensor(vehicle)) {
        end = true;
      }
    }
  }
  return end;
}

function leftOrRight(car) {
  checkLeftRight(car);
  forwardUntilWall(car);
  checkLeftRight(car);
  forward(car);
}

function turnCorrect(vehicle) {
  while (sensor(vehicle)) {
    turnRight(vehicle);
  }
}

function incompleteU(car) {
  turnCorrect(car);
  while (!checkLeftRight(car)) {
    forwardUntilWall(car);
  }
}

function whichDirection(car) {
  turnCorrect(car);
  forwardUntilWall(car);
}

function checkTurn(vehicle, right) {
  let canturn;
  if (right) {
    turnRight(vehicle);
    canturn = !sensor(vehicle);
    turnLeft(vehicle);
  } else {
    turnLeft(vehicle);
    canturn = !sensor(vehicle);
    turnRight(vehicle);
  }
  return canturn;
}

function nthTurn(vehicle, right, n) {
  let goodturns = checkTurn(vehicle, right);
  while (goodturns < n) {
    forward(vehicle);
    goodturns = goodturns + checkTurn(vehicle, right);
  }
  turnRight(vehicle);
  if (!right) {
    turnBack(vehicle);
  }
  forward(vehicle);
}

function firstRight(car) {
  nthTurn(car, true, 1);
  forwardUntilWall(car);
}

function firstLeft(car) {
  nthTurn(car, false, 1);
  forwardUntilWall(car);
}

function zigZag(car) {
  firstRight(car);
  turnLeft(car);
  forward(car);
  firstLeft(car);
}

function nthTurnforward(vehicle, right, n) {
  nthTurn(vehicle, right, n);
  forwardUntilWall(vehicle);
}

function secondRight(car) {
  nthTurnforward(car, true, 2);
}

function thirdRight(car) {
  nthTurnforward(car, true, 3);
}

function fourthRight(car) {
  nthTurnforward(car, true, 4);
}

function fifthLeft(car) {
  nthTurnforward(car, false, 5);
}

function maze(car) {
  nthTurn(car, true, 2);
  nthTurn(car, false, 1);
  nthTurn(car, false, 2);
  nthTurn(car, false, 2);
  nthTurn(car, true, 4);
  nthTurn(car, true, 1);
  nthTurnforward(car, false, 3);
}

function driveBack(vehicle) {
  turnBack(vehicle);
  forward(vehicle);
  turnBack(vehicle);
}

function findDeadEnd(car) {
  let end = false;
  while (!end) {
    forward(car);
    end = checkLeftRight(car);
    if (!end) {
      driveBack(car);
      turnRight(car);
    }
  }
}

function follow(car) {
  while (!checkLeftRight(car)) {
    forwardUntilWall(car);
  }
}

function checkRight(car) {
  turnRight(car);
  if (sensor(car)) {
    turnLeft(car);
    if (sensor(car)) {
      turnLeft(car);
      if (sensor(car)) {
        return true;
      }
    }
  }
  return false;
}

function rightHand(car) {
  while (!checkRight(car)) {
    forward(car);
  }
}

function forwardUntilDestination(car) {
  while (!destinationReached(car)) {
    forward(car);
  }
}

function roomba(car) {
  let right = true;
  while (!destinationReached(car)) {
    if (sensor(car)) {
      turnRight(car);
      if (right) {
        forward(car);
        turnRight(car);
        right = false;
      } else {
        turnBack(car);
        forward(car);
        turnLeft(car);
        right = true;
      }
    } else {
      forward(car);
    }
  }
}
