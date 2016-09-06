var symbols = [];
var symbolTextSize = 20;

function setup() {
  createCanvas(screen.availWidth, screen.availHeight);
  background(0);
  makeSymbolStreams();
}

function draw() {
  drawSymbols();
}

function drawSymbols() {
  background(0);
  textSize(symbolTextSize);
  //textFont("");

  symbols.forEach(function(stream, index) {
    stream.forEach(function(symbol, index) {
      fill(symbol.r, symbol.g, symbol.b);
      text(symbol.value, symbol.x, symbol.y);
      symbol.scroll();
    });
  });
}

function makeSymbolStreams() {
  var x = 0;
  for (var i = 0; i < height / symbolTextSize; i++) {
    symbols.push(makeStream(x));
    x += symbolTextSize;
  }
}

function makeStream(x) {
  var stream = [];
  var r = 0;
  var g = 0;
  var b = 0;
  var y = random(symbolTextSize * 2, symbolTextSize * 15);
  var scrollRate = random(1, 5);
  var first = true;

  for (var s = 0; s < random(5, 30); s++) {
    if (first) {
      r = g = b = 255;
      first = false;
    } else {
      r = 0;
      g -= 30; // TODO optimize
      b = 0;
    }
    var symbol = new Symbol(x, y, r, g, b, scrollRate);
    stream.push(symbol);
    y -= symbolTextSize;
  }
  return stream;
}

function getRandomKatakana() {
  return String.fromCharCode(
    0x30A0 + Math.random() * (0x30FF-0x30A0+1)
  );
}

function Symbol(x, y, r, g, b, scrollRate) {
  this.value = getRandomKatakana();
  this.x = x;
  this.y = y;
  this.r = r;
  this.g = g;
  this.b = b;
  this.scrollRate = scrollRate
  return this;
}

Symbol.prototype.scroll = function() {
  return this.y += this.scrollRate;
}
