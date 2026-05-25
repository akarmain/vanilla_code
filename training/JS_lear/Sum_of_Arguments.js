/**
 * @param {...number} numbers
 * @return {number}
 */
var sum = function(...numbers) {
    return numbers.reduce((acc, n) => acc + n, 0)
};

if (require.main === module){
	console.log(sum())
}