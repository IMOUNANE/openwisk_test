function main() {
  var min = 10;
  var max = 20;

  var value = Math.round(Math.random() * (max - min) + min);

  return {
    msg: "Hello, this is initial value: " + Number(value),
    initialValue: value,
  };
}
