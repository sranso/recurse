var symbols = [];
var symbolTextSize = 22;
var colorFadeRate = 8;

function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  background(0);
  makeSymbolStreams();
}

function draw() {
  background(0);
  textSize(symbolTextSize);
  textFont('Monaco5');
  drawSymbols();
}

function makeSymbolStreams() {
  var x = 0;
  for (var i = 0; i < width / symbolTextSize; i++) {
    symbols.push(makeStream(x));
    x += symbolTextSize;
  }
}

function makeStream(x) {
  var stream = [];
  var r = 0;
  var g = 224;
  var b = 80;
  var y = random(symbolTextSize, symbolTextSize * 15);
  var yStart = y / 2;
  var scrollRate = random(2, 6);
  var first = true;

  for (var i = 0; i < random(10, 30); i++) {
    if (first) {
      stream.push(new Symbol(x, y, 255, 255, 255, scrollRate, yStart));
      first = false;
    } else {
      stream.push(new Symbol(x, y, r, g, b, scrollRate, yStart));
      g -= colorFadeRate;
      b -= colorFadeRate;
    }
    y -= symbolTextSize;
  }
  return stream;
}

function drawSymbols() {
  symbols.forEach(function(stream, index) {
    stream.forEach(function(symbol, index) {
      fill(symbol.r, symbol.g, symbol.b);
      text(symbol.character, symbol.x, symbol.y);
      symbol.scroll();
      symbol.maybeChangeCharacter();
      if (symbol.y > height) {
        symbol.y = symbol.yStart;
      }
    });
  });
}

function getRandomKatakana() {
  return String.fromCharCode(
    0x30A0 + Math.random() * (0x30FF-0x30A0+1)
  );
}

function Symbol(x, y, r, g, b, scrollRate, yStart) {
  this.character = getRandomKatakana();
  this.x = x;
  this.y = y;
  this.r = r;
  this.g = g;
  this.b = b;
  this.scrollRate = scrollRate
  this.yStart = yStart;
  return this;
}

Symbol.prototype.scroll = function() {
  return this.y += this.scrollRate;
}

Symbol.prototype.maybeChangeCharacter = function() {
  if (random(0, 1) < 0.01) {
    this.character = getRandomKatakana();
  }
}
