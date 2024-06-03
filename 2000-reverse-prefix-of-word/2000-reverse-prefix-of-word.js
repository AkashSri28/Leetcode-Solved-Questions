/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    let chIndex = word.indexOf(ch);
    let firstPart = word.substring(0, chIndex+1);
    let secondPart = word.substring(chIndex+1);
    let reverse = firstPart.split("").reverse().join("");
    return reverse+secondPart;
};