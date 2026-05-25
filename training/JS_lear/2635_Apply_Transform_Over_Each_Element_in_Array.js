/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
	let ans = []
	for (let i = 0; i < arr.length; i++) {
		ans.push(fn(arr[i], i))
	}
	return ans
}

if (require.main === module) {
	arr = [1, 2, 3]
	fn = function plusI(i) {
		return  123
	}
	console.log(map([1, 2, 3], fn))
}
