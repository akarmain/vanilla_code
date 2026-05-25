/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
	const cash = new Map()
	return function (...args) {
		let key = JSON.stringify(args)
		if (cash.has(key)) {
			return cash.get(key)
		}
		const ans = fn(...args)
		cash.set(key, ans)
		return ans
	}
}

if (require.main === module) {
	let callCount = 0
	const memoizedFn = memoize(function (a, b) {
		callCount += 1
		return a + b
	})
	console.log(memoizedFn(2, 3)) // 5
	console.log(memoizedFn(2, 3)) // 5
	console.log(callCount) // 1
}
