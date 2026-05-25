/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
	is_called = false
	return function (...args) {
		if (!is_called) {
			is_called = true
			return fn(...args)
		}
	}
}

if (require.main === module) {
	let fn = (a, b, c) => a + b + c
	let onceFn = once(fn)
	console.log(onceFn(1, 2, 3)) // 6
	console.log(onceFn(2, 3, 6)) // returns undefined without calling fn
}
